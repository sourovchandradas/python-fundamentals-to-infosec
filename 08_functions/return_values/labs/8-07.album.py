# Exercise 8-07: Album

def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title':title}

    # If the number of tracks is provided, add it to the dictionary
    if tracks:
        album["tracks"] = tracks

    return album

# Create albums without track numbers
print(make_album("The beatles", "Abbey Road"))
print(make_album("Pink Floyd", "The Dark Side"))

# Create album with track numbers included
print(make_album("Linkin Park", "Hybrid Theory", 12))
print(make_album("Arijit Singh", "Tum Hi Ho", 8))
