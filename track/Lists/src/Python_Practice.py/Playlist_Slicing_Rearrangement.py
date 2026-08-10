songs=[
    "Song A",
    "Song B",
    "Song C",
    "Song D",
    "Song E",
    "Song F",
    "Song G",
    "Song H"
]
print("Complete Playlist:")
print(songs)
print("First 3 Sings:")
print(songs[:3])
print("Last 3 Songs:")
print(songs[-3:])
print("Songs from Position 3 to 6:")
print(songs[2:6])
print("Reverse Playlist:")
print(songs[::-1])
print("Every Alternate Song:")
print(songs[::2])
print("Playlist Without First and Last Song:")
print(songs[1:-1])
short_playlist=songs[2:6]
short_playlist[1]="New Song"
print("Original Playlist:")
print(songs)
print("Short Playlist:")
print(short_playlist)
'''
Output:
Complete Playlist:
['Song A', 'Song B', 'Song C', 'Song D', 'Song E', 'Song F', 'Song G', 'Song H']
First 3 Sings:
['Song A', 'Song B', 'Song C']
Last 3 Songs:
['Song F', 'Song G', 'Song H']
Songs from Position 3 to 6:
['Song C', 'Song D', 'Song E', 'Song F']
Reverse Playlist:
['Song H', 'Song G', 'Song F', 'Song E', 'Song D', 'Song C', 'Song B', 'Song A']
Every Alternate Song:
['Song A', 'Song C', 'Song E', 'Song G']
Playlist Without First and Last Song:
['Song B', 'Song C', 'Song D', 'Song E', 'Song F', 'Song G']
Original Playlist:
['Song A', 'Song B', 'New Song', 'Song D', 'Song E', 'Song F', 'Song G', 'Song H']
Short Playlist:
['Song C', 'New Song', 'Song E', 'Song F']
'''

