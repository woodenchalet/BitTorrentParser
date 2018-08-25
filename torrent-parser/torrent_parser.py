from services.bencode_service import BencodeService

class TorrentParser():
    def __init__(self, torrent):
        self.torrent = torrent
        self.bencodeService = BencodeService()
    
    def get_metadata(self):
        return self.bencodeService.decode(self.torrent)