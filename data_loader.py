import pandas as pd
from utils import clean_title, fix_name_encoding

def load_and_clean_data(csv_path):
    anime = pd.read_csv(csv_path)
    anime['name'] = anime['name'].apply(fix_name_encoding)
    anime['name'] = anime['name'].apply(clean_title)
    anime = anime.dropna(subset=['genre'])
    anime = anime.drop_duplicates(subset='name', keep='first')
    anime['rating'] = anime['rating'].fillna(0)
    return anime