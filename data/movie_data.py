#!/usr/bin/env python
"""IMDB Data Access Methods"""

import json


class MovieData:
    @staticmethod
    def create_movie_dictionary():
        with open('C:\\data.json') as file:
            print('Start')
            movies = json.load(file)
            result = movies
            return result

    @staticmethod
    def get_movie_by_tconst_id(tconst_id):
        result = movie_cache['movies'][tconst_id]
        return result

    @staticmethod
    def get_movies_by_start_year(year):
        new_movie_dict = {}
        for movie in list(movie_cache['movies'].values()):
            for key, value in movie.items():
                if (key == 'startYear') and (value == year):
                    new_movie_dict.update(movie)
        result = new_movie_dict
        return result

    @staticmethod
    def get_movies_by_genre(genre):
        result = movie_cache['movies'][genre]
        return result


movie_cache = MovieData.create_movie_dictionary()