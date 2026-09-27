# Exercise 8-08: User Album

def make_album(artist, title, tracks=None):
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album

# While loop to let users enter albums
while True:
    print("\nEnter album information (or type 'quit' to stop):")
    
    artist = input("Artist name: ")
    if artist.lower() == 'quit':
        break
    
    title = input("Album title: ")
    if title.lower() == 'quit':
        break

    tracks_input = input("Number of tracks (press Enter to skip): ")
    if tracks_input.lower() == 'quit':
        break
    
    # Convert tracks to integer if provided
    tracks = int(tracks_input) if tracks_input else None
    
    # Call the function with user input
    album_info = make_album(artist, title, tracks)
    
    # Print the dictionary created
    print("Album dictionary:", album_info)
