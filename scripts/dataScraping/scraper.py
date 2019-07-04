#Sample ID : tt9916720

# Required packages
import requests
import lxml.html as lh
import ast

# Base URL of the source
baseURL = "https://www.imdb.com/title/"

# Source scraper and data extractor function
def imdbID(imdbId):
    # URL to be scrape
    global baseURL
    url = baseURL + imdbId
    
    # sending get request to the URL 
    feed = requests.get(url)

    # Check for the response validity
    if('200' in str(feed)):
        try: 
            # extract source code from the response
            doc = lh.fromstring(feed.text)

            # extract title of the page
            mtitle = doc.xpath('//title')[0].text

            # extract relevent info from the script tag
            script = doc.xpath('//script')[11].text

            # Converting string into dictonary
            data = ast.literal_eval(script) 
            
            # Removing " - IMDB" from the title
            mtitle = mtitle[:len(mtitle)-7]

            # Initialize resultant dictonary contating data
            res = {'imdbid':imdbId,'title': mtitle}

            # Storing relevant data into dictonary 
            if("aggregateRating" in data.keys()):
                res["rating"] = data["aggregateRating"]["ratingValue"]
            else:
                res["rating"] = 'NA'
            if("director" in data.keys()):
                res["director"] = data["director"]["name"]
            else:
                res["director"] = 'NA'
            if("actor" in data.keys()):
                actors = []
                for i in data["actor"]:
                    actors.append(i["name"])
                res["cast"] = ",".join(actors)
            else:
                res["cast"] = 'NA'
            if("description" in data.keys()):
                res["description"] = data["description"]
            else:
                res["description"] = 'NA'
            if("duration" in data.keys()):
                res["duration"] = data["duration"][2:]
            else:
                res["duration"] = 'NA'
            return res
        except:
            return -1

    # for response apart from 200
    else:
        return -1
    


    
