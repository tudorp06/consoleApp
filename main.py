from repository.SongRepository import SongRepository
from service.SongService import SongService
from UI.UI import UI

song_repository = SongRepository()
song_service = SongService(song_repository)
UI = UI(song_service)
UI.run()
