import logging

BENCODE_LIST_TYPE = 'l'
BENCODE_DICTONARY_TYPE = 'd'
BENCODE_INTEGER_TYPE = 'i'
BENCODE_STRING_TYPE_ZERO = '0'
BENCODE_STRING_TYPE_ONE = '1'
BENCODE_STRING_TYPE_TWO = '2'
BENCODE_STRING_TYPE_THREE = '3'
BENCODE_STRING_TYPE_FOUR = '4'
BENCODE_STRING_TYPE_FIVE = '5'
BENCODE_STRING_TYPE_SIX = '6'
BENCODE_STRING_TYPE_SEVEN = '7'
BENCODE_STRING_TYPE_EIGHT = '8'
BENCODE_STRING_TYPE_NINE = '9'

BENCODE_FILE_START_POSITION = 0
ERROR_START_ZERO = '0'
END_MARK = 'e'
COLON = ':'
DASH = '-'


class BencodeService(object):
    """
    The service class to decode bencode string.
    """

    def __init__(self):
        self.decode_func = {
            BENCODE_LIST_TYPE: self._decode_list,
            BENCODE_DICTONARY_TYPE: self._decode_dict,
            BENCODE_INTEGER_TYPE: self._decode_int,
            BENCODE_STRING_TYPE_ZERO: self._decode_string,
            BENCODE_STRING_TYPE_ONE: self._decode_string,
            BENCODE_STRING_TYPE_TWO: self._decode_string,
            BENCODE_STRING_TYPE_THREE: self._decode_string,
            BENCODE_STRING_TYPE_FOUR: self._decode_string,
            BENCODE_STRING_TYPE_FIVE: self._decode_string,
            BENCODE_STRING_TYPE_SIX: self._decode_string,
            BENCODE_STRING_TYPE_SEVEN: self._decode_string,
            BENCODE_STRING_TYPE_EIGHT: self._decode_string,
            BENCODE_STRING_TYPE_NINE: self._decode_string
        }

    def decode(self, bencode):
        """
        Decode bencode to object.

        :param bencode: The bencode string.
        :type bencode: str

        :return: The decoded bencode output.
        """
        try:
            result, length = self.decode_func[
                bencode[BENCODE_FILE_START_POSITION]
            ](bencode, BENCODE_FILE_START_POSITION)
        except (IndexError, KeyError, ValueError):
            logging.exception("not a valid bencoded string")
        if length != len(bencode):
            logging.exception(
                "invalid bencoded value (data after valid prefix)")
        return result

    def _decode_int(self, bencode, start):
        """
        Slice the bencode string and decode as integer.

        :param bencode: The bencode string.
        :type bencode: str

        :param start: The start position of bencode.
        :type start: int

        :return: The decoded bencode integer output.
        """
        start += 1
        new_start = bencode.index(END_MARK, start)
        number = int(bencode[start:new_start])

        if bencode[start] == DASH:
            if bencode[start + 1] == ERROR_START_ZERO:
                raise ValueError
        elif bencode[start] == ERROR_START_ZERO and new_start != start+1:
            raise ValueError

        return (number, new_start+1)

    def _decode_string(self, bencode, start):
        """
        Slice the bencode string and decode as string.

        :param bencode: The bencode string.
        :type bencode: str

        :param start: The start position of bencode.
        :type start: int

        :return: The decoded bencode string output.
        """
        colon = bencode.index(COLON, start)
        string_length = int(bencode[start:colon])
        if bencode[start] == ERROR_START_ZERO and colon != start+1:
            raise ValueError
        colon += 1
        return (bencode[colon:colon+string_length], colon+string_length)

    def _decode_list(self, bencode, start):
        """
        Slice the bencode string and decode as list.

        :param bencode: The bencode string.
        :type bencode: str

        :param start: The start position of bencode.
        :type start: int

        :return: The decoded bencode list output.
        """
        result, start = [], start+1
        while bencode[start] != END_MARK:
            value, start = self.decode_func[bencode[start]](bencode, start)
            result.append(value)
        return (result, start + 1)

    def _decode_dict(self, bencode, start):
        """
        Slice the bencode string and decode as dictionary.

        :param bencode: The bencode string.
        :type bencode: str

        :param start: The start position of bencode.
        :type start: int

        :return: The decoded bencode dictionary output.
        """
        result, start = {}, start+1
        while bencode[start] != END_MARK:
            key, start = self._decode_string(bencode, start)
            result[key], start = self.decode_func[bencode[start]](
                bencode, start)
        return (result, start + 1)
