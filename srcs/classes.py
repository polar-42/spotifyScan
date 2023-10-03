from srcs.sharedFunction import getTimeReadable


class Spotify:
    def __init__(self) -> None:
        self.totalSong = 0
        self.totalSongMsPlayed = 0
        self.totalPodcastMsPlayed = 0
        self.totalDifferentSong = 0
        self.totalDifferentArtist = 0
        self.totalDifferentAlbum = 0
        self.songs = []
        self.artists = []
        self.albums = []
        self.podcasts = []

    def addSong(self, song):
        self.totalSong = self.totalSong + 1
        self.totalSongMsPlayed = self.totalSongMsPlayed + song.msPlayed

        for x in self.songs:
            if x.name == song.name and x.album == song.album:
                x.nTimePlayed = x.nTimePlayed + 1
                x.msPlayed = x.msPlayed + song.msPlayed
                return
        self.totalDifferentSong = self.totalDifferentSong + 1
        self.songs.append(song)

    def addArtist(self, song):
        for x in self.artists:
            if x.name == song.artist:
                x.nTimePlayed = x.nTimePlayed + song.nTimePlayed
                x.msPlayed = x.msPlayed + song.msPlayed
                return
        self.totalDifferentArtist = self.totalDifferentArtist + 1
        self.artists.append(Artist(song.artist, song.msPlayed))

    def addAlbum(self, song):
        for x in self.albums:
            if x.name == song.album:
                x.nTimePlayed = x.nTimePlayed + song.nTimePlayed
                x.msPlayed = x.msPlayed + song.msPlayed
                return
        self.totalDifferentAlbum = self.totalDifferentAlbum + 1
        self.albums.append(Album(song.album, song.artist, song.msPlayed))

    def addPodcast(self, podcast):
        self.totalPodcastMsPlayed = self.totalPodcastMsPlayed + \
                                    podcast.msPlayed

        for x in self.podcasts:
            if x.name == podcast.name:
                x.nTimePlayed = x.nTimePlayed + 1
                x.msPlayed = x.msPlayed + podcast.msPlayed
                return
        self.podcasts.append(Podcast(podcast.name, podcast.msPlayed))


class Song:
    def __init__(self, name, artist, album, msPlayed, nTimePlayed=1) -> None:
        self.name = name
        self.artist = artist
        self.album = album
        self.msPlayed = msPlayed
        self.nTimePlayed = nTimePlayed

    def __repr__(self) -> str:
        return '{' + self.name + ', ' + self.artist + ', ' + self.album + \
                ', ' + self.msPlayed + ', ' + self.nTimePlayed + '}'

    def __str__(self) -> str:
        return f"Song is {self.name}, made by {self.artist}, on {self.album}, \
listen for {getTimeReadable(self.msPlayed)}, for a total of \
{self.nTimePlayed} times"


class Artist:
    def __init__(self, name, msPlayed, nTimePlayed=1) -> None:
        self.name = name
        self.msPlayed = msPlayed
        self.nTimePlayed = nTimePlayed

    def __repr__(self) -> str:
        return '{' + self.name + ', ' + self.msPlayed + \
                ', ' + self.nTimePlayed + '}'

    def __str__(self) -> str:
        return f"Artist is {self.name}, listen for \
{getTimeReadable(self.msPlayed)}, for a total of \
{self.nTimePlayed} times"


class Album:
    def __init__(self, name, artist, msPlayed, nTimePlayed=1) -> None:
        self.name = name
        self.artist = artist
        self.msPlayed = msPlayed
        self.nTimePlayed = nTimePlayed

    def __repr__(self) -> str:
        return '{' + self.name + ', ' + self.msPlayed + ', ' \
                + self.nTimePlayed + '}'

    def __str__(self) -> str:
        return f"Album is {self.name}, made by {self.artist}, \
listen for {getTimeReadable(self.msPlayed)}, \
for a total of {self.nTimePlayed} times"


class Podcast:
    def __init__(self, name, msPlayed, nTimePlayed=1) -> None:
        self.name = name
        self.msPlayed = msPlayed
        self.nTimePlayed = nTimePlayed

    def __repr__(self) -> str:
        return '{' + self.name + ', ' + self.msPlayed + ', ' \
                + self.nTimePlayed + '}'

    def __str__(self) -> str:
        return f"Podcast is {self.name} \
listen for {getTimeReadable(self.msPlayed)}, \
for a total of {self.nTimePlayed} times"
