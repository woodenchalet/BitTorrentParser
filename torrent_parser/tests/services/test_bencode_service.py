import unittest

from torrent_parser.services.bencode_service import BencodeService


class BencodeServiceTestCase(unittest.TestCase):

    def test_decode_integer(self):
        """To ensure decode integer works."""
        knownValue = ((0, 'i0e'),
                      (1, 'i1e'),
                      (10, 'i10e'),
                      (42, 'i42e'),
                      )

        for plain, encoded in knownValue:
            result = BencodeService().decode(encoded)
            self.assertEqual(plain, result)

    def test_decode_negative_integer(self):
        """To ensure decode integer works."""
        plain = -42
        encoded = 'i-42e'

        result = BencodeService().decode(encoded)
        self.assertEqual(plain, result)

    def test_decode_string(self):
        """To ensure decode string works."""
        knownValue = (('spam', '4:spam'),
                      ('parrot sketch', '13:parrot sketch'))

        for plain, encoded in knownValue:
            result = BencodeService().decode(encoded)
            self.assertEqual(plain, result)

    def test_decode_list(self):
        """To ensure decode list works."""
        plain = ['parrot sketch', 42]
        encoded = 'l13:parrot sketchi42ee'

        result = BencodeService().decode(encoded)

        self.assertEqual(plain, result)

    def test_decode_dictionary(self):
        """To ensure decode dictionary works."""
        plain = {
            'foo': 42,
            'bar': 'spam'
        }

        encoded = 'd3:bar4:spam3:fooi42ee'

        result = BencodeService().decode(encoded)
        self.assertEqual(plain, result)

    def test_decode_with_error_format(self):
        """To ensure appropriate error raised with wrong format."""
        encoded = 'i042e'
        bencodeService = BencodeService()

        self.assertRaises(UnboundLocalError, bencodeService.decode, encoded)
