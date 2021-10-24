from datetime import date

import requests
from bs4 import BeautifulSoup

from helper_methods import clean_data, create_dataset_csv


def create_billboard_top_100_training_set():
    """
    CREATE TRAINING DATA SET FROM TOP 100 SONG LIST FROM 2011-2020
    NOTE:
        - no #7 listed for year 2011
        - no #87 listed for year 2016
        - making list total 998 instead of 1000
        """

    years = [year for year in range(2011, 2021)]  # years 2011-2020
    all_titles = []  # list of all titles for each song, inorder
    all_artists = []  # list of all artists for each song, inorder
    all_ranks = []  # list of all ranks for each song, inorder
    all_years = []  # list of all years for each song, inorder increasing/incremented
    csv_location = '../datasets/billboard_top_100_songs.csv'

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
        print(f'Number of songs on top list for {year}: {len(song_ranks)}')
    create_dataset_csv(all_artists, all_ranks, all_titles, all_years, csv_location)


def create_billboard_top_100_testing_set():
    """CREATE TESTING DATA SET FROM CURRENT DATE OF YEAR"""
    current_date = date.today()
    current_year = int(current_date.year)

    csv_location = '../datasets/current_billboard_top_100_songs.csv'

    response = requests.get(f"https://www.billboard.com/charts/hot-100")
    soup = BeautifulSoup(response.text, 'html.parser')

    song_ranks = soup.find_all("span", class_="chart-element__rank__number",
                               text=True)
    song_ranks = clean_data(song_ranks)

    song_titles = soup.find_all("span", class_="chart-element__information__song text--truncate color--primary",
                                text=True)
    song_titles = clean_data(song_titles)

    song_artists = soup.find_all("span", class_="chart-element__information__artist text--truncate color--secondary",
                                 text=True)
    song_artists = clean_data(song_artists)

    current_year_list = [current_year] * len(song_ranks)
    print(f'Number of songs on current top songs for {current_year}: {len(song_ranks)}')
    # print(song_ranks)
    # print(song_titles)
    # print(song_artists)
    # print(current_year_list)
    create_dataset_csv(song_artists, song_ranks, song_titles, current_year_list, csv_location)

