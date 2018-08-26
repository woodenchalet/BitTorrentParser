import unittest

from torrent_parser.services.file_service import FileService


class FileServiceTestCase(unittest.TestCase):

    def test_calculate_formatted_size_with_one_kb(self):
        """To ensure calculate formatted size with one kb works."""
        actual = FileService.calculate_formatted_size(1204)
        expect = '1 kB'
        self.assertEqual(expect, actual)

    def test_calculate_formatted_size_with_larger_size(self):
        """To ensure calculate formatted size with larger size works."""
        actual = FileService.calculate_formatted_size(123412412)
        expect = '117.7 MB'
        self.assertEqual(expect, actual)

    def test_calculate_formatted_size_with_very_big_size(self):
        """To ensure calculate formatted size with very big size works."""
        actual = FileService.calculate_formatted_size(32423423423423)
        expect = '29.49 TB'
        self.assertEqual(expect, actual)
