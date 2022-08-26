from repository.SongRepository import SongRepository
from service.SongService import SongService
from UI.UI import UI
from repository.PlaylistRepository import PlaylistRepository
from domain.Playlist import Playlist


playlist = Playlist("initplaylist", [])
song_repository = SongRepository()
playlist_repository = PlaylistRepository(playlist)
song_service = SongService(song_repository, playlist_repository)
UI = UI(song_service)
UI.run()
