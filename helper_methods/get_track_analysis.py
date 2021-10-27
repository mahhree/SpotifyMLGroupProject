import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from credentials import client_id, client_secret

# provide api credentials
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret))


def add_track_analysis(csv_location, new_csv_location):
    """Pretty much need to take list of song ID's from csv chosen and iterate through song IDs
    to map their unique track analysis to another list to be added to the csv.
    We can do this by either saving in order
    """
    # step 1: read csv we need track analysis for
    df = pd.read_csv(csv_location)

    # step 2: pull column relative to song IDs, save as list
    artists = df['Spotify Song ID'].tolist()

    # step 3: determine if dictionary or list of best feature columns best to use, initialize them here
    danceability = []  # example

    # step 4: format and save each returned call to get_track_analysis(song_id) to list or dictionary
    ...

    # step 5: update column
    df['Danceability'] = danceability  # example

    # step 6: create a new csv with added columns to prevent errors in original datasets
    # and be able to fix later if needed
    df.to_csv(new_csv_location, index=False)


def get_track_analysis(song_id):
    """
    reference:
    https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features
    """

    # confirm if we use sp.audio_features or sp.

    # or we can define this method to pass in a list of song id's max length 100 IDS
    results1 = sp.audio_features(song_id)

    results2 = sp.audio_analysis(song_id)

    # step 2: confirm which portion of API response contains relevant info, separate, and return to 'add_track_analysis()'
    # we should only need one or the other depending on whats returned by each
    track_analysis = results1['']  # something like this => results['tracks']['items'][0]['uri']
    track_features = results2['']

    # step 3: reformat info obtain from step 3
    ...

    # step 4: return formatted list of features for each song
    return track_features
