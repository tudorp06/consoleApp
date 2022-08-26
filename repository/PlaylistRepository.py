from domain.Playlist import Playlist


class PlaylistRepository:
    def __init__(self, playlist: Playlist):
        self.playlist = playlist

    def add_song(self, song):
        self.playlist.get_playlist().append(song)
