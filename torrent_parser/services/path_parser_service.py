from services.file_service import FileService
from models.torrent_descriptor_file_path import TorrentDescriptorFilePath

LENGTH = 'length'
PATH = 'path'
CRC_CHECKSUM = 'crc32'


class PathParserService():
    """
    The service class to fetch the file information descripted
    in torrent.
    """
    def __init__(self, file_info):
        self._file_info = file_info

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

    def _fetch_size(self):
        """
        Output the file size in formatted output.

        :return: file size in formatted output.
        """
        length = self._file_info.get(LENGTH)
        if not length:
            return None

        return FileService.calculate_formatted_size(length)

    def _fetch_paths(self):
        """
        Output the file size in formatted output.

        :return: file size in formatted output.
        """
        result = []
        paths = self._file_info.get(PATH)

        if not paths:
            return result

        for path in paths:
            result.append(unicode(path))

        return result

    def _fetch_crc_checksum(self):
        """
        Output the CRC checksum.

        :return: The CRC checksum.
        """
        return self._file_info.get(CRC_CHECKSUM)
