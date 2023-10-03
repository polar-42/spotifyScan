import pandas
from srcs.classes import Spotify, Song, Podcast


def openAllFiles(argv) -> []:
    argv.pop(0)
    files = []
    try:
        for i in argv:
            files.append(open(i))
    except FileNotFoundError:
        print(i, "file cannot be open")
        return None
    return files


def openAllDatas(files) -> []:
    datas = []
    try:
        for i in files:
            datas.append(pandas.read_json(i))
    except ValueError:
        print("Error found in a file")
        return None
    return datas


def readAllDatas(datas) -> Spotify:
    spotify = Spotify()
    wait = 0
    i = 0
    while (i < len(datas)):
        x = 0
        while x < len(datas[i]):
            if int(datas[i].iloc[x][3]) > 30000:
                name = datas[i].iloc[x][7]
                artist = datas[i].iloc[x][8]
                album = datas[i].iloc[x][9]
                nameEpisode = datas[i].iloc[x][11]
                podcastName = datas[i].iloc[x][12]
                msPayed = int(datas[i].iloc[x][3])
                if name is not None and artist is not None \
                        and album is not None:
                    song = Song(name, artist, album, msPayed)
                    spotify.addSong(song)
                    spotify.addArtist(song)
                    spotify.addAlbum(song)
                elif nameEpisode is not None \
                        and podcastName is not None:
                    spotify.addPodcast(Podcast(podcastName, msPayed))

                if wait < 1000:
                    print("\rWaiting.\r", end="")
                elif wait > 1000 and wait < 2000:
                    print("\rWaiting..\r", end="")
                elif wait > 2000 and wait < 3000:
                    print("\rWaiting...\r", end="")
                if wait > 3000:
                    print("\r          \r", end="")
                    wait = 0
                wait = wait + 1
            x = x + 1
        i = i + 1
    print("\r          \r", end="")
    return spotify
