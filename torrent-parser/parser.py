import sys

from torrent_parser import TorrentParser

path = sys.argv[1]

with TorrentParser(path) as parser:
    print(parser.output_json())
