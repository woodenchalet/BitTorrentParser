from services.file_service import FileService


class TorrentDescriptorFilePath():
    def __init__(self, file_info):
        self._file_info = file_info
    
    @property
    def size(self):
        length = self._file_info.get('length')
        if not length:
            return None
        
        return FileService.calculate_formatted_size(length)

    @property
    def paths(self):
        result = []
        paths = self._file_info.get('path')

        if not paths:
            return result
        
        for path in paths:
            result.append(unicode(path))
    
    @property
    def crc_checksum(self):
        return self._file_info.get('crc32')
