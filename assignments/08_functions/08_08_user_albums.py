# 8-8, user albums, pg 180


def make_album (artist, title, tracks=0):
    """Building a dictionary containg information about albums"""
    album_dict ={
        'artist' : artist.title(),
        'title' : title.title()
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict
title_prompt = "\n What album are you thinking of?"
artist_prompt = "Who's the artist?"

print("Enter 'quit' to stop")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)
