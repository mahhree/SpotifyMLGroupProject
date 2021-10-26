import pandas as pd

from get_song_info import get_song_genres, get_song_id_and_artists


def add_genres_to_csv(csv_location, new_location):
    df = pd.read_csv(csv_location)
    artists = df['Artist'].tolist()
    titles = df['Title'].tolist()

    song_genres = []
    song_spotify_ids = []
    for artist, title in zip(artists, titles):
        # print(title, artist, sep='\nby: ')
        song_info = get_song_id_and_artists(title, artist)

        # song_id = song_info[0]
        if song_info[0] is not None:
            song_spotify_ids.append(str(song_info[0]))
        else:
            song_spotify_ids.append('-')

        # artists_ids = song_info[1]
        if song_info[1] is not None:
            song_genre_list = get_song_genres(song_info[1])
            if song_genre_list is not None:
                song_genre_string = ', '.join([str(genre) for genre in song_genre_list])
            else:
                song_genre_string = '-'
            song_genres.append(song_genre_string)
        else:
            song_genre_string = '-'
            song_genres.append(song_genre_string)

    print('Song Genres:\n')
    print(*song_genres, sep='\n')

    print('---------------------------------------------------------------------')
    print('Song IDs:\n')
    print(*song_spotify_ids, sep='\n')

    df['Genre'] = song_genres
    df['Spotify Song ID'] = song_spotify_ids
    df.to_csv(new_location, index=False)

    # print(df)


# add_genres_to_csv('../datasets/current_billboard_top_100_songs.csv',
#                   '../datasets/top_100_2021_with_genres.csv')

add_genres_to_csv('../datasets/billboard_top_100_songs.csv',
                  '../datasets/top_100_2011-2020_with_genres.csv')

df = pd.read_csv('../datasets/top_100_2011-2020_with_genres.csv')
print(df)
