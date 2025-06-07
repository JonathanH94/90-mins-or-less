import sqlite3
import random
import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("api_key")


def find_imdb() -> str:

    with sqlite3.connect('movie_database.db') as conn:
        cur = conn.cursor()
        rand_int = random.randint(1, 260295)
        cur.execute("SELECT * FROM Movies WHERE id = :id ", {"id": rand_int})
        id, imdb_id, title, runtime, genre = cur.fetchone()
        return imdb_id
        

def call_api(imdb_id: str)->tuple:
    url = f"http://www.omdbapi.com/?i={imdb_id}&plot=full&apikey={api_key}"
    response = requests.get(url)
    data: dict = response.json()
    ##NEED TO CHANGE THIS TO A DICT TO RETURN
    #print(data)
    movie_title = data.get('Title')
    year = data.get('Year')
    plot = data.get('Plot')
    poster = data.get('Poster')
    runtime = data.get('Runtime')
    imdb_rating = data.get('imdbRating')
    if not data['Ratings'] == []: 
        if len(data['Ratings']) > 1 and data['Ratings'][1]:
            rt_rating = data['Ratings'][1]['Value']
        else:
            rt_rating = 'N/A'    
    else:
        rt_rating = "N/A"
    return movie_title, year, plot, poster, runtime, imdb_rating, rt_rating ##NEEDS TO BE A DICT




if __name__=="__main__":

    call_api("tt9603208")