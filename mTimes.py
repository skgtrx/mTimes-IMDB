# Import logging for disabling the logs on the terminal
import logging
logging.getLogger("kivy").disabled = True

# Import kivy for gui
import kivy
kivy.require('1.10.0')

# Import Text input element from kivy
from kivy.uix.textinput import TextInput

# Import Text Label element from kivy
from kivy.uix.label import Label

# Import Image element from kivy
from kivy.uix.image import Image

# Image Scroller label from kivy
from kivy.uix.scrollview import ScrollView

# Import kivy App and Builder from kivy
from kivy.app import App
from kivy.lang import Builder

# Import Screen and Screen manager for multiscreen
from kivy.uix.screenmanager import ScreenManager, Screen

# Import WindowBase and Window for the window size
from kivy.core.window import WindowBase
from kivy.core.window import Window

### Import modules Code ###
''' 
    Not able to import created module due to error in pandas csv import.
    Instead of importing nodule writing code for that module here only.
'''
# required packages
import pandas as pd
import re

# read movies data
movies = pd.read_csv("movies_data.csv")

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
    return movies[movies["imdbid"].apply(lambda x: True if x.lower()==imdbId.lower() else False)].to_dict('record')

### Import modules Code ###

# Set window Size
Window.size = (400, 600)

# Start Screen class
class StartScreen(Screen):
    pass

# Menu Screen class
class SelectScreen(Screen):
    pass

# Movie Search By name class
class SearchByNameScreen(Screen):
    # Movie details extractor
    def get_movie_details(self):
        self.ids.abs_title.text = "[b][i][size=30] SEARCH [/size][/i][/b]"
        self.ids.rel_title.text = "[b][i][size=30] Related Searchs [/size][/i][/b]"
        
        # Extracting entered movie name from text field
        name = self.ids.movname.text
        # Passing the name for extraction
        res = query_name(name)

        # Exact Match Block
        absolute = res[0]
        if(len(absolute)!=0):
            absolute = absolute[0]
            abs_details = "[b]Title:[/b] {}\n[b]Ratings:[/b] {}\n[b]Duration:[/b] {}\n[b]Director:[/b] {}\n[b]Cast:[/b] {}\n[b]Description:[/b] {}".format(absolute["title"],absolute["rating"],absolute["duration"],absolute["director"],absolute["cast"],absolute["description"])
            self.ids.movname_detail_absolute.text = abs_details
        else:
            abs_details = "[b][color=#00FF00]\n\n                           Exact Match not found!\n                                Please Enter the\n                                   Valid Name.[/color][/b]"
            self.ids.movname_detail_absolute.text = abs_details
        
        # Relative match block
        relative = res[1]
        if(len(relative)!=0):
            rel_details = ''
            for i in relative:
                rel_details = rel_details +"*"*54+"\n[b]Title:[/b] {}\n[b]Ratings:[/b] {}\n[b]Duration:[/b] {}\n[b]Director:[/b] {}\n[b]Cast:[/b] {}\n[b]Description:[/b] {}\n".format(i["title"],i["rating"],i["duration"],i["director"],i["cast"],i["description"])+"*"*54+"\n\n"
            self.ids.movname_detail_relative.text = rel_details
        else:
            rel_details = "[b][size=25][color=#00FF00]\n\n         No Related Search found![/color][/size][/b]"
            self.ids.movname_detail_relative.text = rel_details

# Movie Search By IMDB Id class
class SearchByIdScreen(Screen):
    # Movie details extractor
    def get_movie_by_id(self):
        # Extracting entered movie id from text field
        imdb = self.ids.movid.text
        # Passing the id for extraction
        res = query_id(imdb)

        # Output on screen result block
        if(len(res)==0):
            self.ids.movid_detail.text = "[b][size=40][color=#00FF00]\n\n\n     Invalid IMDB Id!\n    Please Enter the\n           Valid ID.[/color][/size][/b]"
        else:
            res = res[0]
            details = "[b]Title:[/b] {}\n[b]Ratings:[/b] {}\n[b]Duration:[/b] {}\n[b]Director:[/b] {}\n[b]Cast:[/b] {}\n[b]Description:[/b] {}".format(res["title"],res["rating"],res["duration"],res["director"],res["cast"],res["description"])
            self.ids.movid_detail.text = details
        
# Application builder class
class mTimesApp(App):
    def build(self):
        self.icon = 'icons/logo.png'
        return Builder.load_file('gui/mTimes.kv')

if __name__ == '__main__':
    mTimesApp().run()
