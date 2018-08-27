class TorrentDescriptorFilePath():
    """
    The value object of the torrent descriptor file path.
    """

    def __init__(self, size, paths, crc_checksum):
        self.size = size
        self.paths = paths
        self.crc_checksum = crc_checksum
