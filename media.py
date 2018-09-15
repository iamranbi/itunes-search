#Ran Bi

import requests
import json
import webbrowser


## Create a base class (“Media”) and two subclasses (“Song” and “Movie”) that represent items in the iTunes store
class Media:
    def __init__(self, title="No Title", author="No Author", releaseyear="No Year",url="No url",json_dict=None):
        if json_dict is None:
            self.title = title
            self.author = author
            self.releaseyear = releaseyear
            self.url = url
        else:
            self.title = json_dict["collectionName"]
            self.author = json_dict["artistName"]
            self.releaseyear = json_dict["releaseDate"].split('-')[0]
            self.url = json_dict["collectionViewUrl"]
    def __str__(self):
        return "{} by {} ({})".format(self.title,self.author,self.releaseyear)
    def __len__(self):
        return 0
    def launch_browser(self):
        webbrowser.open(self.url)

class Song(Media):
    def __init__(self, title="No Title", author="No Author", releaseyear="No Year", album="No Album", genre="No Genre", tracklength=0,url="No url",json_dict=None):
        super().__init__(title, author, releaseyear,url)
        if json_dict is None:
            self.album = album
            self.genre = genre
            self.tracklength = tracklength
        else:
            self.title = json_dict["trackName"]
            self.author = json_dict["artistName"]
            self.releaseyear = json_dict["releaseDate"].split('-')[0]
            self.album = json_dict["collectionName"]
            self.genre = json_dict["primaryGenreName"]
            self.tracklength = json_dict["trackTimeMillis"]
            self.url = json_dict["trackViewUrl"]
    def __str__(self):
        return super().__str__() + " [" + self.genre + "]"
    #track length in nearest seconds
    def __len__(self):
        return round(0.001*self.tracklength)
    def launch_browser(self):
        webbrowser.open(self.url)

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", releaseyear="No Year", rating="No Rating", movielength=0,url="No url",json_dict=None):
        super().__init__(title, author, releaseyear,url)
        if json_dict is None:
            self.rating = rating
            self.movielength = movielength
        else:
            self.title = json_dict["trackName"]
            self.author = json_dict["artistName"]
            self.releaseyear = json_dict["releaseDate"].split('-')[0]
            self.rating = json_dict["contentAdvisoryRating"]
            self.movielength = json_dict["trackTimeMillis"]
            self.url = json_dict["trackViewUrl"]
    def __str__(self):
        return super().__str__() + " [" + self.rating +"]"
    #movie length in nearest minutes
    def __len__(self):
        return round(1.66667e-5*self.movielength)
    def launch_browser(self):
        webbrowser.open(self.url)

## Create objects using JSON and parse each of these JSON objects into properly constructed objects of the correct type
def creat_object_from_json(js):
    with open(js) as jso:
        j = json.load(jso)
        object_from_json = []
        for x in j:
            if x["wrapperType"] == "track":
                if x["kind"] == "feature-movie":
                    m = Movie(json_dict = x)
                elif x['kind'] == "song":
                    m = Song(json_dict = x)
            else:
                m = Media(json_dict = x)
            object_from_json.append(m)
        return object_from_json

## Fetch data from the iTunes API, and create lists of objects from the data retrieved
def creat_object_from_api(base_url):
    json_string = requests.get(base_url).text
    results_list = json.loads(json_string)['results']
    object_from_api = []
    for x in results_list:
        if x["wrapperType"] == "track":
            if x["kind"] == "feature-movie":
                m = Movie(json_dict = x)
            elif x['kind'] == "song":
                m = Song(json_dict = x)
        else:
            m = Media(json_dict = x)
        object_from_api.append(m)
    return object_from_api

## Create an interactive search interface
if __name__ == "__main__":
    num_s = [str(x+1) for x in list(range(50))]
    ask_user = input("Enter a search term, or 'exit' to quit: ")
    while True:
        d1 = dict()
        d2 = dict()
        songs = []
        movies = []
        othermedia = []
        total = []
        count = 1
        if ask_user == "exit":
            print("Bye!")
            break
        elif isinstance(ask_user, str):
            base_url_user = "https://itunes.apple.com/search?term="+ask_user
            object_from_user = creat_object_from_api(base_url_user)
            for x in object_from_user:
                if isinstance(x, Song):
                    songs.append(x)
                elif isinstance(x, Movie):
                    movies.append(x)
                else:
                    othermedia.append(x)
            total=songs+movies+othermedia
            for x in range(len(total)):
                d1[str(x+1)]=total[x]
            d2["SONGS"] = songs
            d2["MOVIES"] = movies
            d2["OTHER MEDIA"] = othermedia
            if all(x==[] for x in d2.values()):
                print("No result. Please try something else")
            else:
                for x in d2:
                    print(x)
                    for y in d2[x]:
                        print(str(count) + " " + y.__str__())
                        count = count + 1
            ask_user=input("Enter a number for more info, or another search term, or exit: ")
            while ask_user in num_s:
                print("Launching in web browser")
                d1[ask_user].launch_browser()
                ask_user=input("Enter a number for more info, or another search term, or exit: ")
