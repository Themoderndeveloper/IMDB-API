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


movie_cache = MovieData.create_movie_dictionary()