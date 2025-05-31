from flask import Flask, render_template
import main


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/find-film", methods=["POST"])
def find_film():
    imdb_id = main.find_imdb()
    movie_title, year, plot, poster = main.call_api(imdb_id)
    return f"TITLE:{movie_title} \n YEAR: {year} \n PLOT: {plot} \n POSTER: {poster} "


if __name__ =="__main__":
    app.run(debug=True)