

class Torrent():
    def __init__(self, files, title, creation_date,
                 created_by, announce_list, size):
        self.files = files
        self.title = title
        self.creation_date = creation_date
        self.created_by = created_by
        self.announce_list = announce_list
        self.size = size
