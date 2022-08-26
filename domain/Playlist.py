class Playlist:
    def __init__(self, name, playlist):
        self.__name = name
        self.__playlist = []

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_playlist(self):
        return self.__playlist