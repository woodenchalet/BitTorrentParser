import unittest
import os

from torrent_parser.torrent_parser import TorrentParser


class TorrentParserTestCases(unittest.TestCase):
    def test_torrent_parser_test_case(self):
        """
        To ensure that the TorrentParser works as expected.
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = dir_path + '/Jimmy Dirtnail-The Complete Collection.torrent'

        torrent = TorrentParser(path).output_torrent_object()

        expected_title = 'JimmyDirtnail-TheCompleteInstrumentals'
        expected_created_by = 'ia_make_torrent'
        expected_announce_list_length = 2
        expected_size = '512 kB'
        expected_file_number = 119

        self.assertEquals(expected_title, torrent.title)
        self.assertEquals(expected_created_by, torrent.created_by)
        self.assertEquals(expected_announce_list_length,
                          len(torrent.announce_list))
        self.assertEquals(expected_size, torrent.size)
        self.assertEquals(expected_file_number, len(torrent.files))
