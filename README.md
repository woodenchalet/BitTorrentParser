# Torrent Parser

Author: Yi Luo

[![Build Status](https://travis-ci.com/woodenchalet/BitTorrentParser.svg?branch=master)](https://travis-ci.com/woodenchalet/BitTorrentParser)

A simple parser for .torrent file.

## Installation

Include `torrent-parser` within your project's libary directory, often
`/lib`.  If that does not make sense to you, simply include the `torrent-parser`
subdirectory within your application's root directory

## Usage

```python

import sys

from torrent_parser import TorrentParser

path = sys.argv[1]

parser = TorrentParser(path)

torrent = parser.output_torrent_object()

```

## Workflows via Contexts

Contexts allow you to build workflows easily,

```python
import sys

from torrent_parser import TorrentParser

path = sys.argv[1]

with TorrentParser(path) as parser:
    torrent = parser.output_torrent_object()
```
