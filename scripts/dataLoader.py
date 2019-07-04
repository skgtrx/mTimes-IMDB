# required packages
import pandas as pd
import re

# read movies data
movies = pd.read_csv("movies_data.csv"))

# query with movie name
def query_name(name):
    # Exact Match
    global movies
    exactRes = movies[movies["title"].apply(lambda x: True if name.lower() == x.lower() else False)].to_dict('record')
    # Related Results
    relRes = movies[movies["title"].apply(lambda x: True if re.search(name, x, re.IGNORECASE) else False)].to_dict('record')
    return [exactRes,relRes]

# query with movie id
def query_id(imdbId):
    global movies
    return movies[movies["imdbid"].apply(lambda x: True if x==imdbId else False)].to_dict('record')

