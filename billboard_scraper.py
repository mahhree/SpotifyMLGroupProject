from bs4 import BeautifulSoup
import requests
import pandas

df = pandas.read_csv

years = [year for year in range(2011, 2021)] # years 2011-2020

# for year in years:
#     response = requests.get(f"https://www.billboard.com/charts/year-end/{year}/hot-100-songs")
