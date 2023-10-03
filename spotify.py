import sys
import warnings
from srcs.filesFunction import openAllDatas, openAllFiles, readAllDatas
from srcs.sharedFunction import getTimeReadable

warnings.filterwarnings("ignore")


def printResult(spotify, val):

    f = open("history.txt", "w")

    recap = ""
    i = 0
    if len(spotify.songs) > 0 and int(val) < len(spotify.songs):
        recap = recap + "Your top " + val + " songs is:\n"
    else:
        recap = recap + "Your top " + str(len(spotify.songs)) + " songs is:\n"
    while i < int(val) and i < len(spotify.songs):
        recap = recap + str(spotify.songs[i]) + "\n"
        i = i + 1

    i = 0
    if len(spotify.artists) > 0 and int(val) < len(spotify.songs):
        recap = recap + "\n\nYour top " + val + " artists is:\n"
    else:
        recap = recap + "\n\nYour top " + \
            str(len(spotify.artists)) + " artists is:\n"
    while i < int(val) and i < len(spotify.artists):
        recap = recap + str(spotify.artists[i]) + "\n"
        i = i + 1

    i = 0
    if len(spotify.albums) > 0 and int(val) < len(spotify.albums):
        recap = recap + "\n\nYour top " + val + " albums is:\n"
    else:
        recap = recap + "\n\nYour top " + \
            str(len(spotify.albums)) + " albums is:\n"
    while i < int(val) and i < len(spotify.albums):
        recap = recap + str(spotify.albums[i]) + "\n"
        i = i + 1

    i = 0
    if len(spotify.podcasts) > 0 and int(val) < len(spotify.podcasts):
        recap = recap + "\n\nYour top " + val + " podcasts is:\n"
    else:
        recap = recap + "\n\nYour top " + str(len(spotify.podcasts)) + \
            " podcasts is:\n"
    while i < int(val) and i < len(spotify.podcasts):
        recap = recap + str(spotify.podcasts[i]) + ".\n"
        i = i + 1

    recap = recap + "\n\nRecap:\n"
    recap = recap + "You listen to " + str(spotify.totalSong) + " songs, "
    recap = recap + "for a total of " + str(spotify.totalDifferentSong) \
                    + " differents songs. And " + str(len(spotify.podcasts)) \
                    + " podcasts\n"
    recap = recap + "You listen to " + str(spotify.totalDifferentArtist) \
                    + " differents artists"
    recap = recap + " and listen " + str(spotify.totalDifferentAlbum) \
                    + " differents albums.\n"
    recap = recap + "You listen to music for " \
                    + str(getTimeReadable(spotify.totalSongMsPlayed)) \
                    + "and podcasts for " \
                    + str(getTimeReadable(spotify.totalPodcastMsPlayed)) + "\n"
    recap = recap + "You listen to Spotify for " \
                    + str(getTimeReadable(spotify.totalSongMsPlayed +
                                          spotify.totalPodcastMsPlayed)) \
                    + "\n"
    f.write(recap)
    f.close


def main():
    if len(sys.argv) < 2:
        print("Error, not enough args")
        return

    files = openAllFiles(sys.argv)
    if files is None:
        return
    datas = openAllDatas(files)
    if datas is None:
        return

    r = input("Do you prefer rank by listening time or \
number of time played (1 or 2): ")
    if r.isnumeric() is False or int(r) != 1 and int(r) != 2:
        print("Error, answer is not 1 or 2")
        return

    val = input("How many ranks you want: ")
    if val.isnumeric() is False or int(val) < 1:
        print("Error, not numeric or < 1")
        return

    spotify = readAllDatas(datas)

    if int(r) == 1:
        spotify.songs.sort(key=lambda x: x.msPlayed, reverse=True)
        spotify.artists.sort(key=lambda x: x.msPlayed, reverse=True)
        spotify.albums.sort(key=lambda x: x.msPlayed, reverse=True)
        spotify.podcasts.sort(key=lambda x: x.msPlayed, reverse=True)
    else:
        spotify.songs.sort(key=lambda x: x.nTimePlayed, reverse=True)
        spotify.artists.sort(key=lambda x: x.nTimePlayed, reverse=True)
        spotify.albums.sort(key=lambda x: x.nTimePlayed, reverse=True)
        spotify.podcasts.sort(key=lambda x: x.nTimePlayed, reverse=True)

    printResult(spotify, val)
    print("Finish, have a look on history.txt")


if __name__ == "__main__":
    main()
