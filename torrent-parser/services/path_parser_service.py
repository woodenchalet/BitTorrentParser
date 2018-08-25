from services.file_service import FileService
from models.torrent_descriptor_file_path import TorrentDescriptorFilePath


class PathParserService():
    def __init__(self, file_info):
        self._file_info = file_info

    def parse_descriptor_file_path(self):
        return TorrentDescriptorFilePath(
            self._fetch_size(),
            self._fetch_paths(),
            self._fetch_crc_checksum())

    def _fetch_size(self):
        length = self._file_info.get('length')
        if not length:
            return None

        return FileService.calculate_formatted_size(length)

    def _fetch_paths(self):

        result = []
        paths = self._file_info.get('path')

        if not paths:
            return result

        for path in paths:
            result.append(unicode(path))

        return result

    def _fetch_crc_checksum(self):
        return self._file_info.get('crc32')
