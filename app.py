from flask import Flask, render_template
import helper as h


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")



@app.route("/find-film", methods=["POST"])
def find_film():
    imdb_id = h.find_imdb()
    movie_title, year, plot, poster, runtime = h.call_api(imdb_id) ##NEEDS TO BE A DICT INSTEAD OF TUPLE
    return render_template("view_film.html", movie_title=movie_title, poster=poster, plot=plot, year=year, runtime=runtime, imdb_id=imdb_id)


if __name__ =="__main__":
    app.run(debug=True)