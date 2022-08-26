from datetime import datetime


class Song:
    """
    Song class, which stores Song type objects, that can have attributes such as name, artist, genre and duration.
    """
    def __init__(self, name, artist, genre, duration):
        self.__name = name
        self.__artist = artist
        self.__genre = genre
        self.__duration = duration

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_artist(self):
        return self.__artist

    def set_artist(self, new_artist):
        self.__artist = new_artist

    def get_genre(self):
        return self.__genre

    def set_genre(self, new_genre):
        self.__genre = new_genre

    def get_duration(self):
        return self.__duration

    def set_duration(self, new_duration):
        self.__duration = new_duration

    def __str__(self):
        return "Song " + self.get_name() + " by " + self.get_artist() + ", genre: " + self.get_genre() + ", duration: " + str(
            self.get_duration())
