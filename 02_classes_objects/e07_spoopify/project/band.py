from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'

        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        try:
            album_to_remove = next(filter(lambda x: x.name == album_name, self.albums))
            if album_to_remove.published:
                return f'Album has been published. It cannot be removed.'

            self.albums.remove(album_to_remove)
            return f'Album {album_name} has been removed.'
        except StopIteration:
            return f'Album {album_name} is not found.'

    def details(self):
        album_list = '\n'.join([x.details() for x in self.albums])
        return f'Band {self.name}' \
            f'{album_list}'


# band = Band("Death")
# album = Album("The Sound of Perseverance")
# message = band.remove_album("The Sound of Perseverance")