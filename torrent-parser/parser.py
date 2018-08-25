import sys

from torrent_parser import TorrentParser

torrent_filename = sys.argv[1]

torrent_file = open(torrent_filename, "rb")
try:
    torrent = torrent_file.read()
    parser = TorrentParser(torrent)
    metainfo = parser.get_metadata()
    print(metainfo)
except:
    sys.exit(torrent_filename + " is not a valid *.torrent file\n")