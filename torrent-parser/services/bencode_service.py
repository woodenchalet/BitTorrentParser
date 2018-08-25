import sys


class BencodeService():
    def __init__(self):
        self.decode_func = {
            'l': self.decode_list,
            'd': self.decode_dict,
            'i': self.decode_int,
            '0': self.decode_string,
            '1': self.decode_string,
            '2': self.decode_string,
            '3': self.decode_string,
            '4': self.decode_string,
            '5': self.decode_string,
            '6': self.decode_string,
            '7': self.decode_string,
            '8': self.decode_string,
            '9': self.decode_string
        }

    def decode(self, bencode):
        try:
            result, length = self.decode_func[bencode[0]](bencode, 0)
        except (IndexError, KeyError, ValueError):
            sys.exit("not a valid bencoded string")
        if length != len(bencode):
            sys.exit("invalid bencoded value (data after valid prefix)")
        return result

    def decode_int(self, bencode, start):
        start += 1
        new_start = bencode.index('e', start)
        number = int(bencode[start:new_start])

        if bencode[start] == '-':
            if bencode[start + 1] == '0':
                raise ValueError
        elif bencode[start] == '0' and new_start != start+1:
            raise ValueError

        return (number, new_start+1)

    def decode_string(self, bencode, start):
        colon = bencode.index(':', start)
        string_length = int(bencode[start:colon])
        if bencode[start] == '0' and colon != start+1:
            raise ValueError
        colon += 1
        return (bencode[colon:colon+string_length], colon+string_length)

    def decode_list(self, bencode, start):
        result, start = [], start+1
        while bencode[start] != 'e':
            value, start = self.decode_func[bencode[start]](bencode, start)
            result.append(value)
        return (result, start + 1)

    def decode_dict(self, bencode, start):
        result, start = {}, start+1
        while bencode[start] != 'e':
            key, start = self.decode_string(bencode, start)
            result[key], start = self.decode_func[bencode[start]](
                bencode, start)
        return (result, start + 1)
