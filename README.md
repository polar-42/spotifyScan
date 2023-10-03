# SpotifyScan
This project is a tool made in python to read and recap a Spotify streaming history.

## How to use this program
First of all you need to use python (3.10.12) and some librairies.


Now, in a terminal use the command "git clone git@github.com:polar-42/spotifyScan.git". It should create a "spotifyScan" folder.
Copy all the JSON streaming history audio files in the folder.
#
Now it's finish you can launch python:
- "python spotify.py AllStreamingHistoryFiles". It read the whole file and you can read the result in a history.txt file. All songs, artists and albums that you listen for more than 30 seconds will be here. You'll hade to tell if you prefer ranking by listening time of number of time played and the size of the ranking.
Example: "python spotify.py, Streaming_History_Audio_2018_0.json"
