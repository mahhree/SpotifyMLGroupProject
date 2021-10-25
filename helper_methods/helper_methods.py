import pandas as pd


def clean_data(data_list):
    data_list = [(data.getText()) for data in data_list]
    data_list = [data.strip('\n') for data in data_list]
    data_list = [data.replace('\n', ' ') for data in data_list]
    data_list = [data.replace('"', '') for data in data_list]
    return data_list


def create_dataset_csv(all_artists, all_ranks, all_titles, all_years, csv_location):
    df = pd.DataFrame()
    df['Title'] = all_titles
    df['Artist'] = all_artists
    df['Year'] = all_years
    df['Rank'] = all_ranks
    print(df)
    df.to_csv(csv_location)

