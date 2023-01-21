from repository.SongRepository import SongRepository
from repository.PlaylistRepository import PlaylistRepository


class PlaylistService:
    def __init__(self, playlist_repository: PlaylistRepository):
        self._playlist_repository = playlist_repository

    def create_playlist(self,playlist_name):
        self._playlist_repository.create_playlist(playlist_name)

    def show_playlist(self, playlist_name):
        self._playlist_repository.show_playlist(playlist_name)

    def add_song(self, song, playlist_name):
        self._playlist_repository.add_song(song, playlist_name)
