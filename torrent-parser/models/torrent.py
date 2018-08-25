import time
from math import log

from models.torrent_descriptor_file_path import TorrentDescriptorFilePath


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

        return self._calculate_formatted_size(piece_length)

    @staticmethod
    def _calculate_formatted_size(num):
        """Human friendly file size"""
        unit_list = zip(['bytes', 'kB', 'MB', 'GB', 'TB', 'PB'], [
                        0, 0, 1, 2, 2, 2])
        if num > 1:
            exponent = min(int(log(num, 1024)), len(unit_list) - 1)
            quotient = float(num) / 1024**exponent
            unit, num_decimals = unit_list[exponent]
            format_string = '{:.%sf} {}' % (num_decimals)
            return format_string.format(quotient, unit)
        if num == 0:
            return '0 bytes'
        if num == 1:
            return '1 byte'
