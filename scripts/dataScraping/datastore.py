# imported modules
import scraper
import os
# package required
import pandas as pd

# Empty dataframe
movie_data = pd.DataFrame(columns=['imdbid','title','rating','director','cast','duration','descripton'])

# reading data from imdbId.csv into list
imdbId_list = pd.read_csv("imdbid.csv", names = ["id"], header = None)
imdbId_list = list(imdbId_list.id)

count = 1
for i in imdbId_list[-5000:]:
    print(count)
    d = scraper.imdbID(i)
    if(d!=-1):
        movie_data = movie_data.append(d, ignore_index=True)
    else:
        print(d)
    count+=1
    

movie_data.to_csv("movies_data.csv", sep='\t', index = None, header=True)


