def extract_artist(song_title):
    dash_pos = song_title.index("-")
    return song_title[dash_pos+2:]   # +2 ताकि dash और space skip हो जाए

print(extract_artist("Shape of You - Ed Sheeran"))
