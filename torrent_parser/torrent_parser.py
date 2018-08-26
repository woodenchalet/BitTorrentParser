import logging

from errors import TorrentFormatError
from services.bencode_service import BencodeService
from services.torrent_parser_service import TorrentParseService


class TorrentParser():
    """
    The parser to parse raw torrent to formatted output.
    """
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, 'rb')

    def output_torrent_object(self):
        """
        Output the parsed formatted torrent object output.

        :return: Formatted torrent object output.
        :rtype class:`Torrent`
        """
        metainfo = self._decode_bencode()

        return TorrentParseService(metainfo).output_torrent_object()

    def output_dict(self):
        pass

    def output_json(self):
        pass
        # return json.dumps(vars(self.torrent).)

    def __enter__(self):
        """
        The setup to enter the context manager and produce a parser
        object to generate a formatted output.

        :return: The TorrentParseService togenerate a formatted output.
        :rtype class:`TorrentParseService`
        """
        metainfo = self._decode_bencode()

        return TorrentParseService(metainfo)

    def __exit__(self, typ, value, tb):
        """
        The setup to exit the context manager.
        """

        if typ is not None:
            logging.exception('** Exception %s: %r' % (typ.__name__, value))

        self.file.close()

    def _decode_bencode(self):
        """
        Decode the bencode and output the formatted meta info.
        """
        metainfo = BencodeService().decode(self.file.read())
        if not isinstance(metainfo, dict):
            raise TorrentFormatError(
                'The format of the torrent is not proper.')

        return metainfo
