import sys

from torrent_parser import TorrentParser

path = sys.argv[1]

# with TorrentParser(path) as parser:
#     torrent = parser.output_torrent_object()

parser = TorrentParser(path)
torrent = parser.output_torrent_object()
