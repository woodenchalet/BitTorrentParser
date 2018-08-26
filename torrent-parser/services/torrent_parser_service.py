import time
import json

from models.torrent import Torrent
from services.file_service import FileService
from services.path_parser_service import PathParserService


class TorrentParseService():

    def __init__(self, metainfo):
        self._metainfo = metainfo
        self.torrent = Torrent(
            self._fetch_files(),
            self._fetch_title(),
            self._fetch_creation_date(),
            self._fetch_created_by(),
            self._fetch_announce_list(),
            self._fetch_size())

    def _fetch_files(self):
        file_paths = []

        info = self._metainfo.get('info')
        if not info:
            return None

        files = info.get('files')
        if not files:
            return None

        for torrent_file in files:
            file_paths.append(PathParserService(torrent_file)
                              .parse_descriptor_file_path())

        return file_paths

    def _fetch_title(self):
        return self._metainfo.get('title')

    def _fetch_creation_date(self):
        date = self._metainfo.get('creation date')

        return time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(date))

    def _fetch_created_by(self):
        return self._metainfo.get('created by')

    def _fetch_announce_list(self):
        return self._metainfo.get('announce-list')

    def _fetch_size(self):
        info = self._metainfo.get('info')
        if not info:
            return None

        piece_length = info.get('piece length')
        if not piece_length:
            return None

        return FileService.calculate_formatted_size(piece_length)

    def output_dict(self):
        self.torrent.__dict__

    def output_json(self):
        return json.dumps(vars(self.torrent))
