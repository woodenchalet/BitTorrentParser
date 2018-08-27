import sys

from torrent_parser import TorrentParser

"""
This is an example.
"""

path = sys.argv[1]

with TorrentParser(path) as parser:
    torrent = parser.output_torrent_object()
