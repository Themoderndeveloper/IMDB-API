#!/usr/bin/env python
""" API calls to JSON Movie Database """
import json
from time import perf_counter

from data.movie_data import MovieData


class MovieApi:
    @staticmethod
    def remove_empty_keys(movie):
        for key in list(movie.keys()):
            if movie[key] == '\\N':
                del movie[key]
        return movie

    @staticmethod
    def calculate_performance(start_time, end_time, movie):
        time_diff = end_time - start_time
        perf_time_mill = time_diff / 1000
        perf_nano = {'performanceInNanoseconds': format(time_diff, 'G')}
        movie.update(perf_nano)
        return movie

    @staticmethod
    def get_movie_by_id(tconst):
        start_time = perf_counter()

        movie = MovieData.get_movie_by_tconst_id(tconst)
        movie_result = MovieApi.remove_empty_keys(movie)
        end_time = perf_counter()

        movieDict = MovieApi.calculate_performance(start_time, end_time, movie_result)

        movie = {'count': '1'}
        results = {'results': movieDict}
        movie.update(results)

        return movie

    @staticmethod
    def get_movies_by_start_year(year):
        movie = MovieData.get_movies_by_start_year(year)
        result = MovieApi.remove_empty_keys(movie)
        return result

    @staticmethod
    def get_movies_by_genre(genre):
        movie = MovieData.get_movies_by_genre(genre)
        result = MovieApi.remove_empty_keys(movie)
        return result
