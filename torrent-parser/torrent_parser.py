from services.bencode_service import BencodeService
from models.torrent import Torrent


class TorrentParser():
    def __init__(self, path):
        self.path = path
        self.bencodeService = BencodeService()
        self.file = open(self.path, "rb")

    def __enter__(self):
        metainfo = self._decode(self.file.read())

        return Torrent(metainfo)

    def __exit__(self, typ, value, tb):
        if typ is not None:
            print '** Exception %s: %r' % (typ.__name__, value)

        self.file.close()

    def _decode(self, raw):
        return self.bencodeService.decode(raw)
