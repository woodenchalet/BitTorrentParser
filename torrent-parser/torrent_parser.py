from services.bencode_service import BencodeService
from services.torrent_parser_service import TorrentParseService


class TorrentParser():
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, "rb")

    def __enter__(self):
        metainfo = BencodeService().decode(self.file.read())

        return TorrentParseService(metainfo)

    def __exit__(self, typ, value, tb):
        if typ is not None:
            print '** Exception %s: %r' % (typ.__name__, value)

        self.file.close()
