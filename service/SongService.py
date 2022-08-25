from domain.Song import Song
from repository.SongRepository import SongRepository


class SongService:
    def __init__(self, song_repository: SongRepository):
        self._song_repository = song_repository

    def update_song(self, name, new_name, new_artist, new_genre, new_duration):
        ok = 0
        for x in self._song_repository.get_entity_list():
            if x.get_name() == name and ok == 0:
                ok = 1
                x.set_name(new_name)
                x.set_artist(new_artist)
                x.set_genre(new_genre)
                x.set_duration(new_duration)

    def add_song(self, name, artist, genre, duration):
        song = Song(name, artist, genre, duration)
        self._song_repository.add_entity(song)

    def show_song_list(self):
        for x in self._song_repository.get_entity_list():
            print(str(x))

    def remove_song(self, name):
        ok = 0
        for x in self._song_repository.get_entity_list():
            if x.get_name() == name and ok == 0:
                ok = 1
                self._song_repository.get_entity_list().remove(x)
