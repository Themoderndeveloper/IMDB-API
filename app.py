from flask import jsonify
from flask_api import FlaskAPI, status, exceptions

from bin.movie_api import MovieApi
from content.home_page import HomePage
from time import perf_counter

app = FlaskAPI(__name__)


@app.route('/', methods=['GET'])
def home():
    return HomePage.home_page_content()


@app.route("/health", methods=['GET'])
def health_check():
    """
    Health Check: OK
    """
    health_status = '"Body: "OK"'
    return jsonify({'body': 'OK'})


@app.route("/movies/tconst/<tconst>", methods=['GET'])
def get_movie_by_tconst(tconst):
    """
    Get a single movie by tconst ID
    """
    start_time = perf_counter()
    movie = MovieApi.get_movie_by_id(tconst)
    end_time = perf_counter()
    result = MovieApi.calculate_performance(start_time, end_time, movie)
    return result


@app.route("/movies/startYear/<int:start_year>", methods=['GET'])
def get_movie_by_start_year(start_year):
    """
    Get movies by a start year
    """

    return jsonify({'movie start year': start_year})


@app.route("/movies/genre/<genre>", methods=['GET'])
def get_movie_by_genre(genre):
    """
    Get movies by a genre
    """

    return jsonify({'movie genre': genre})


if __name__ == "__main__":
    app.run(debug=True)

