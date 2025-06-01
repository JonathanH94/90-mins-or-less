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
    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    ##NEED TO CHANGE THIS TO A DICT TO RETURN
    movie_title = data.get('Title')
    year = data.get('Year')
    plot = data.get('Plot')
    poster = data.get('Poster')
    runtime = data.get('Runtime')
    return movie_title, year, plot, poster, runtime ##NEEDS TO BE A DICT




if __name__=="__main__":

    call_api("tt9603208")