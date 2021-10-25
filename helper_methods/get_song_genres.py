import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from credentials import client_id, client_secret

# provide api credentials
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret))


def get_song_id(name_of_song, correct_artist):
    # step 1: encode artists name and pass to search query
    results = sp.search(
        q=name_of_song.replace(' ', '%'),  # song searched
        limit=5
    )

    # step 2: save id of song for later comparison
    song_id = results['tracks']['items'][0]['uri']
    song_id = song_id.replace('spotify:track:', '')
    #
    # song_dict = results['tracks']['items'][0]
    # for key in song_dict.keys():
    #     print(key)

    # step 3: save artists of song of first result
    song_artists_list = results['tracks']['items'][0]['artists']

    # step 4: create dictionary mapping each artist name key to the spotify id
    artist_info_dict = {}
    for artist in song_artists_list:
        artist_info_dict[artist['name']] = artist['id']

    lowercase_artists = [artist.casefold() for artist in artist_info_dict.keys()]

    # step 5 confirm if correct artist is in artists on song
    if correct_artist.casefold() in lowercase_artists \
            or any(correct_artist.casefold().find(artist)
                   for artist in lowercase_artists):
        print(f'Song ID: {song_id}')
        return song_id
    else:
        print('Song ID not found.')
        print(f'{correct_artist} not found in song artists:')
        for artist in artist_info_dict.keys():
            print(artist)
        return None


get_song_id('You Should Probably Leave', 'Chris Stapleton')



# step 1: encode artists name query
# artist_name = "down on me"
# print(artist_name)

# step 2 pass name of artist to search query, save results of first
# results = sp.search(
#     q=artist_name.replace(' ', '%'),  # song searched
#     limit=1
# )

# step 3 collect list of artists on song
# artists_list = results['tracks']['items'][0]['artists']

# song_id = results['tracks']['items'][0]['uri']
# song_id = song_id.replace('spotify:track:', '')

# print(f'Song id: {song_id}')

# artist_info_dict = {}
# for artist in artists_list:
#     artist_info_dict[artist['name']] = artist['id']
#
# for key, value in artist_info_dict.items():
#     print(f'{key}: {value}')
# if artist_name in artist_info_dict.keys():
#     print(f'Correct Key: {artist_info_dict[artist_name]}')
# else:
#     print('artist id not found.')
# print(artist_info_dict.items())

# print(artists_list[0])
# print(artists_list[0]['name'])
# artist_id1 = artists_list[0]['id']
# print(artists_list[1])
# print(artists_list[1]['name'])
# artist_id2 = artists_list[1]['id']


# artist1 = dict(sp.artist(artist_id1))
# for key in artist1:
#     print(key)
# # print(artist1)
# artist2_id = sp.artist(artist_id2)['uri']
# artist2_name = sp.artist(artist_id2)['name']
# print(artist2_id)
# print(artist2_name)

# new_dict = dict(results['tracks']['items'][0]['artists'][1])
# for key in new_dict.keys():
#     print(key)
# print(new_dict['uri'])
#
# artist = sp.artist(new_dict['uri'])
# print(artist)
#
# artist_dict = artist
# for key in artist_dict.keys():
#     print(key)
# print(artist_dict['name'])

# for track in results['tracks']['items']:
#     print(track)

# new_dict = {
#     "tracks": {
#         "href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20\n",
#         "items": [
#             {}
#         ],
#         "limit": 20,
#         "next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
#         "offset": 0,
#         "previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
#         "total": 4
#     },
#     "artists": {
#         "href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20\n",
#         "items": [
#             {}
#         ],
#         "limit": 20,
#         "next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
#         "offset": 0,
#         "previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
#         "total": 4
#     },
#     "albums": {
#         "href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20\n",
#         "items": [
#             {}
#         ],
#         "limit": 20,
#         "next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
#         "offset": 0,
#         "previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
#         "total": 4
#     },
#     "playlists": {
#         "href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20\n",
#         "items": [
#             {}
#         ],
#         "limit": 20,
#         "next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
#         "offset": 0,
#         "previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
#         "total": 4
#     },
#     "shows": {
#         "href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20\n",
#         "items": [
#             {}
#         ],
#         "limit": 20,
#         "next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
#         "offset": 0,
#         "previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
#         "total": 4
#     },
#     "episodes": {
#         "href": "https://api.spotify.com/v1/me/shows?offset=0&limit=20\n",
#         "items": [
#             {}
#         ],
#         "limit": 20,
#         "next": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
#         "offset": 0,
#         "previous": "https://api.spotify.com/v1/me/shows?offset=1&limit=1",
#         "total": 4
#     }
# }
