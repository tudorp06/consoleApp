from domain.Song import Song
from repository.SongRepository import SongRepository


class SongService:
    def __init__(self, song_repository: SongRepository):
        self._song_repository = song_repository

    def check_existence(self, song_name):
        for song in self._song_repository.get_entity_list():
            if song.get_name() == song_name:
                raise Exception("This song is already in your list!")

    def update_song(self, name, new_name, new_artist, new_genre, new_duration):
        if not self._song_repository.get_entity_list():
            print("The list is empty!")
        else:
            ok = 0
            for x in self._song_repository.get_entity_list():
                if x.get_name() == name and ok == 0:
                    ok = 1
                    x.set_name(new_name)
                    x.set_artist(new_artist)
                    x.set_genre(new_genre)
                    x.set_duration(new_duration)

        if ok == 0:
            raise Exception("The song you are trying to update does not exist!")

    def add_song(self, song):
        self._song_repository.add_entity(song)

    def show_song_list(self):
        for x in self._song_repository.get_entity_list():
            print(str(x))

        if not self._song_repository.get_entity_list():
            print("The list is empty!")

    def remove_song(self, name):
        if not self._song_repository.get_entity_list():
            print("The list is empty!")
        else:
            ok = 0
            for x in self._song_repository.get_entity_list():
                if x.get_name() == name and ok == 0:
                    ok = 1
                    self._song_repository.get_entity_list().remove(x)

        if ok == 0:
            raise Exception("The song you are trying to remove does not exist!")
