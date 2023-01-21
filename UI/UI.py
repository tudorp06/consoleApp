from service.SongService import SongService
import os
import sys
from domain.Song import Song
from domain.Playlist import Playlist


class UI:
    def __init__(self, song_service: SongService):
        self._song_service = song_service

    def clear(self):
        os.system('CLS')

    def view_all(self):
        self._song_service.show_song_list()

    def add(self):
        name = input("Enter song name: ")
        self._song_service.check_existence(name)
        artist = input("Enter artist: ")
        genre = input("Enter genre: ")
        duration = int(input("Enter duration: "))
        song = Song(name, artist, genre, duration)
        self._song_service.add_song(song)
        print("Added " + name)

    def update(self):
        name = input("Which song would you like to update? ")
        new_name = input("Enter the new name: ")
        new_artist = input("Enter the new artist: ")
        new_genre = input("Enter the new genre: ")
        new_duration = int(input("Enter the new duration: "))
        self._song_service.update_song(name, new_name, new_artist, new_genre, new_duration)
        print("Successfully updated song")

    def remove(self):
        name = input("Which song would you like to remove? ")
        self._song_service.remove_song(name)
        print("Successfully removed " + name)

    def view_by_artist(self):
        artist_name = input("Enter the name of the artist: ")
        self._song_service.view_by_artist(artist_name)
        
    def create_playlist(self):
        name = input("Enter the name of your new playlist: ")
        list = []
        playlist = Playlist(name,list)
        print("Succesfully created" + name + "! You can start adding songs now.")

    def add_to_playlist(self):
        song_name = input("Enter the name of the song you would like to add: ")
        self._song_service.add_to_playlist(song_name)
        print("Successfully added " + song_name)

    def go_back(self):
        comm = input("Press any key to go back: ")
        self.main_menu()

    def exit(self):
        sys.exit("Exiting program... ")

    def main_menu(self):
        print("Welcome to Tudor's music listening app! Please choose one of the following options:")
        print("1) Add a song")
        print("2) Remove a song")
        print("3) Update a song's details")
        print("4) View song list")
        print("5) View songs by artist")
        print("6) Create a playlist")
        print("7) Add song to an existing playlist")
        try:
            command = input(">")
            if command == "1":
                self.clear()
                self.add()
                self.go_back()
            elif command == "2":
                self.clear()
                self.remove()
                self.go_back()
            elif command == "3":
                self.clear()
                self.update()
                self.go_back()
            elif command == "4":
                self.clear()
                self.view_all()
                self.go_back()
            elif command == "5":
                self.clear()
                self.view_by_artist()
                self.go_back()
            elif command == "6":
                self.clear()
                self.create_playlist()
                self.go_back()
            elif command == "7":
                self.clear()
                self.add_to_playlist()
                self.go_back()
            elif command == "0":
                self.exit()

        except Exception as ex:
            print('\n', ex)

    def run(self):
        self.main_menu()
