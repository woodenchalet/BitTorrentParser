import time

from models.torrent_descriptor_file_path import TorrentDescriptorFilePath
from services.file_service import FileService

class Torrent():
    def __init__(self, metainfo):
        self._metainfo = metainfo

    @property
    def files(self):
        file_paths = []

        info = self._metainfo.get('info')
        if not info:
            return None

        files = info.get('files')
        if not files:
            return None

        for torrent_file in files:
            file_paths.append(TorrentDescriptorFilePath(torrent_file))
        
        return file_paths

    @property
    def title(self):
        return self._metainfo.get('title')

    @property
    def creation_date(self):
        date = self._metainfo.get('creation date')
        if type(date) != type(1):
            return ""
        else:
            return time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(date))

    @property
    def created_by(self):
        return self._metainfo.get('created by')

    @property
    def announce_list(self):
        return self._metainfo.get('announce-list')

    @property
    def size(self):
        info = self._metainfo.get('info')
        if not info:
            return None

        piece_length = info.get('piece length')
        if not piece_length:
            return None

        return FileService.calculate_formatted_size(piece_length)
