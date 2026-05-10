import os

class Song:
    def __init__(self, file_path, title=None):
        if title:
            self.title = title
        else:
            self.title = os.path.basename(file_path)
        self.artist = None
        self.album = None
        self.date = None
        self.genre = None
        self.duration = None
        self.__file_path = file_path
    
    @property
    def file_path(self):
        return self.__file_path
