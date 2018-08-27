from services.file_service import FileService

LENGTH = 'length'
CRC_CHECKSUM = 'crc32'


class PathParserService(object):
    """
    The service class to fetch the file information descripted
    in torrent.
    """
    def __init__(self, file_info):
        self._file_info = file_info

    def _fetch_size(self):
        """
        Output the file size in formatted output.

        :return: file size in formatted output.
        """
        length = self._file_info.get(LENGTH)
        if not length:
            return None

        return FileService.calculate_formatted_size(length)

    def _fetch_crc_checksum(self):
        """
        Output the CRC checksum.

        :return: The CRC checksum.
        """
        return self._file_info.get(CRC_CHECKSUM)
