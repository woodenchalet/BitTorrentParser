from models.torrent_descriptor_file_path import TorrentDescriptorFilePath
from services.path_parser_service import PathParserService

NAME = 'name'


class SingleFileParseService(PathParserService):
    def __init__(self, file_info):
        super(SingleFileParseService, self).__init__(file_info)

    def parse_descriptor_file_path(self):
        """
        Output the result of TorrentDescriptorFilePath object.

        :return: The Object of result TorrentDescriptorFilePath.
        :rtype class:`TorrentDescriptorFilePath`
        """
        return TorrentDescriptorFilePath(
            self._fetch_size(),
            self._fetch_name(),
            self._fetch_crc_checksum())

    def _fetch_name(self):
        """
        Output the file size in formatted output.

        :return: file size in formatted output.
        """
        return self._file_info.get(NAME)
