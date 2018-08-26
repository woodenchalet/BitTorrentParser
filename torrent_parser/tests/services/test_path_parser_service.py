import unittest


from torrent_parser.services.path_parser_service import PathParserService


class PathServiceTestCase(unittest.TestCase):
    def test_parse_descriptor_file_path(self):
        """ """
        file_info = {
            "length": 21312,
            "path": ["Good one"],
            "crc32": "4054c82c"
        }

        path = PathParserService().parse_descriptor_file_path(file_info)
        self.assertEquals(path, True)
