from models.torrent_descriptor_file_path import TorrentDescriptorFilePath
from services.path_parser_service import PathParserService

PATH = 'path'


class MultipleFileParseService(PathParserService):
    def __init__(self, file_info):
        super(MultipleFileParseService, self).__init__(file_info)

    def _fetch_paths(self):
        """
        Output the file size in formatted output.

        :return: file size in formatted output.
        """
        paths = self._file_info.get(PATH)
        result = []

        if not paths:
            return result

        for path in paths:
            result.append(unicode(path))

        return result

    def parse_descriptor_file_path(self):
        """
        Output the result of TorrentDescriptorFilePath object.

        :return: The Object of result TorrentDescriptorFilePath.
        :rtype class:`TorrentDescriptorFilePath`
        """
        return TorrentDescriptorFilePath(
            self._fetch_size(),
            self._fetch_paths(),
            self._fetch_crc_checksum())
