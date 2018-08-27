import time

from models.torrent import Torrent
from services.file_service import FileService
from services.multiple_file_parse_service import MultipleFileParseService
from services.single_file_parse_service import SingleFileParseService


INFO = 'info'
FILES = 'files'
TITLE = 'title'
CREATION_DATE = 'creation date'
CREATE_BY = 'created by'
ANNOUNCE_LIST = 'announce-list'
PIECE_LENGTH = 'piece length'


class TorrentParseService(object):
    """
    The service class to fetch the torrent information
    from matadata dictory.
    """

    def __init__(self, metainfo):
        self._metainfo = metainfo
        self.torrent = Torrent(
            self._fetch_files(),
            self._fetch_title(),
            self._fetch_creation_date(),
            self._fetch_created_by(),
            self._fetch_announce_list(),
            self._fetch_size())

    def _fetch_files(self):
        """
        Output the result of file paths infomation.

        :return: The list of torrent file paths information.
        :rtype class:`list`
        """
        file_paths = []

        info = self._metainfo.get(INFO)
        if not info:
            return None

        files = info.get(FILES)
        if not files:
            file_paths.append(SingleFileParseService(info)
                              .parse_descriptor_file_path())
            return file_paths
        else:
            for torrent_file in files:
                file_paths.append(MultipleFileParseService(torrent_file)
                                  .parse_descriptor_file_path())

        return file_paths

    def _fetch_title(self):
        """
        Output the torrent title.

        :return: The torrent title.
        :rtype string
        """
        return self._metainfo.get(TITLE)

    def _fetch_creation_date(self):
        """
        Output the torrent creation date

        :return: The torrent creation date
        :rtype string
        """
        date = self._metainfo.get(CREATION_DATE)

        return time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(date))

    def _fetch_created_by(self):
        """
        Output the client create the torrent.

        :return: The client create the torrent.
        :rtype string
        """
        return self._metainfo.get(CREATE_BY)

    def _fetch_announce_list(self):
        """
        Output the list of tracker URL

        :return: The list of tracker URL
        :rtype list
        """
        return self._metainfo.get(ANNOUNCE_LIST)

    def _fetch_size(self):
        """
        Output the size of the torrent size.

        :return: the formatted size of torrent
        :rtype string
        """
        info = self._metainfo.get(INFO)
        if not info:
            return None

        piece_length = info.get(PIECE_LENGTH)
        if not piece_length:
            return None

        return FileService.calculate_formatted_size(piece_length)

    def output_torrent_object(self):
        """
        Output the parsed torrent object.

        :return: The parsed torrent object.
        :rtype class:`Torrent`
        """
        return self.torrent
