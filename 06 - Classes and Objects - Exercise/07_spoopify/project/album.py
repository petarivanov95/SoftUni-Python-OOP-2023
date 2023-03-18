from project.song import Song
from typing import Tuple, List
from project.song import Song


class Album:
    def __init__(self, name: str, *songs: Tuple[Song]):
        self.name = name
        self.songs = list(songs)
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)

        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        try:
            song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

        self.songs.remove(song)

        return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self):
        result = [f"Album {self.name}"]
        [result.append(f"== {s.get_info()}") for s in self.songs]

        return "\n".join(result)
# class Album:
#
#     def __init__(self, name, *songs):
#         self.name = name
#         self.songs = list(*songs)
#         self.published = False
#
#     def add_song(self, song):
#         if self.published:
#             return f"Cannot add songs. Album is published."
#         elif song.single:
#             return f"Cannot add {song.name}. It's a single"
#         elif song in self.songs:
#             return f"Song is already in the album."
#         else:
#             self.songs.append(song)
#             return f"Song {song.name} has been added to the album {self.name}."
#
#     def remove_song(self, song_name: str) -> str:
#         try:
#             song = next(filter(lambda s: s.name == song_name, self.songs))
#         except StopIteration:
#             return "Song is not in the album."
#         if self.published:
#             return "Cannot remove songs. Album is published."
#         self.songs.remove(song)
#         return f"Removed song {song_name} from album {self.name}."
#
#     def publish(self):
#         if self.published:
#             return f"Album {self.name} is already published."
#
#         self.published = True
#         return f"Album {self.name} has been published."
#
#     def details(self):
#         info_list = []
#         for song in self.songs:
#             info_list.append(f'== {song.get_info()}\n')
#         info = "".join(info_list)
#         return f'Album {self.name}\n{info}'



