from service.SongService import SongService
import os


class UI:
    def __init__(self, song_service: SongService):
        self._song_service = song_service

    def clear(self):
        os.system('CLS')

    def view_all(self):
        self._song_service.show_song_list()

    def add(self):
        name = input("Enter song name: ")
        artist = input("Enter artist: ")
        genre = input("Enter genre: ")
        duration = int(input("Enter duration: "))
        self._song_service.add_song(name, artist, genre, duration)
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

    def go_back(self):
        comm = input("Press any key to go back: ")
        self.main_menu()

    def main_menu(self):
        print("Welcome to Tudor's music listening app! Please choose one of the following options:")
        print("1) Add a song")
        print("2) Remove a song")
        print("3) Update a song's details")
        print("4) View song list")
        while True:
            command = input(">")
            if command == "1":
                self.clear()
                self.add()
                self.go_back()

            if command == "2":
                self.clear()
                self.remove()
                self.go_back()

            if command == "3":
                self.clear()
                self.update()
                self.go_back()

            if command == "4":
                self.clear()
                self.view_all()
                self.go_back()

    def run(self):
        self.main_menu()
