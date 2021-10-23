import pandas as pd
import requests
from bs4 import BeautifulSoup


def clean_data(data_list):
    data_list = [(data.getText()) for data in data_list]
    data_list = [data.strip('\n') for data in data_list]
    data_list = [data.replace('\n', ' ') for data in data_list]
    data_list = [data.replace('"', '') for data in data_list]
    return data_list


years = [year for year in range(2011, 2021)]  # years 2011-2020
all_titles = []  # list of all titles for each song, inorder
all_artists = []  # list of all artists for each song, inorder
all_ranks = []  # list of all ranks for each song, inorder
all_years = []  # list of all years for each song, inorder increasing/incremented

for year in years:
    response = requests.get(f"https://www.billboard.com/charts/year-end/{year}/hot-100-songs")
    soup = BeautifulSoup(response.text, 'html.parser')

    song_ranks = soup.find_all("div", class_="ye-chart-item__rank")
    song_ranks = clean_data(song_ranks)
    all_ranks += song_ranks

    song_titles = soup.find_all("div", class_="ye-chart-item__title", text=True)
    song_titles = clean_data(song_titles)
    all_titles += song_titles

    song_artists = soup.find_all("div", class_="ye-chart-item__artist")
    song_artists = clean_data(song_artists)
    all_artists += song_artists

    all_years += [year] * len(song_ranks)
    print(f'number of songs for {year}: {len(song_ranks)}')

df = pd.DataFrame()
df['Title'] = all_titles
df['Artist'] = all_artists
df['Year'] = all_years
df['Rank'] = all_ranks
print(df)

"""
- no #7 listed for year 2011
- no #87 listed for year 2016
- making list total 998 instead of 1000
"""

df.to_csv('datasets/billboard_top_100_songs.csv')

# will create new data set to use as test data with current year's stats
# will use spotipy to grab genre and additional song metrics for each song in list

# response = requests.get(f"https://www.billboard.com/charts/year-end/{year}/hot-100-songs")
# soup = BeautifulSoup(response.text, 'html.parser')

# get/clean song ranks
# song_ranks = soup.find_all("div", class_="ye-chart-item__rank")
# song_ranks = clean_data(song_ranks)

# get/clean song titles
# song_titles = soup.find_all("div", class_="ye-chart-item__title")
# song_titles = clean_data(song_titles)

# get/clean song artists
# song_artists = soup.find_all("div", class_="ye-chart-item__artist")
# song_artists = clean_data(song_artists)


# df = pd.DataFrame()
# df['Title'] = song_titles
# df['Artist'] = song_artists
# df['Year'] = current_year
# df['Rank'] = song_ranks
# print(df)

# for i in range(id_count, len(song_ranks)):
#     test_dict[i] = list(song_titles[i], song_artists[i], year, song_ranks[i])
# id_count += 1

# print(test_dict)
#
# print(song_titles)
# print(song_artists)

#
# for year in years:
#     response = requests.get(f"https://www.billboard.com/charts/year-end/{year}/hot-100-songs")
#     soup = BeautifulSoup(response.text, 'html.parser')
