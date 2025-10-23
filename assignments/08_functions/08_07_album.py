# 8-7, album, pg 180


def make_album (artist, title):
    """Building a dictionary containg information about albums"""
    album_dict ={
        'artist' : artist.title(),
        'title' : title.title()
    }
    return album_dict

album = make_album ('drake', 'views')
print(album)

album = make_album ('j.cole', 'the off-season')
print(album)
