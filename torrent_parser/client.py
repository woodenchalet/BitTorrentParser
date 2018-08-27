import sys
import json

from torrent_parser import TorrentParser

"""
This is an example, output result as json format.
"""

path = sys.argv[1]

with TorrentParser(path) as parser:
    torrent = parser.output_torrent_object()
    json_output = json.dumps(torrent, default=lambda o: o.__dict__,
                             sort_keys=True, indent=4)
    print json_output
