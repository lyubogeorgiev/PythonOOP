from project.song import Song


class Album:
    def __init__(self, name: str, *args: Song):
        self.name = name
        self.songs = [x for x in args]
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f'Cannot add {song.name}. It\'s a single'

        if self.published:
            return f'Cannot add songs. Album is published.'

        if song in self.songs:
            return f'Song is already in the album.'

        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if self.published:
            return f'Cannot remove songs. Album is published.'

        try:
            song_to_remove = next(filter(lambda x: x.name == song_name, self.songs))
            self.songs.remove(song_to_remove)
            return f'Removed song {song_name} from album {self.name}.'
        except StopIteration:
            return f'Song is not in the album.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'

        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        song_list = '\n'.join([x.get_info() for x in self.songs])
        return f'Album {self.name}' \
            f'{song_list}'
