#!/usr/bin/env python
"""Movie API Access layer Tests using Data Access layer in Test Driven Development (TDD)."""

import unittest

from services.movie_api import MovieApi


class MovieApiTests(unittest.TestCase):
    def test_get_movie_by_tconst_id_returns_id_tt0000492(self):
        # GIVEN
        tconst = "tt0000492"
        expected = 'Personal'
        movie = MovieApi.get_movie_by_id(tconst)

        # WHEN
        result = movie['primaryTitle']

        # THEN
        self.assertEqual(expected, result)

    def test_movie_removes_multiply_nulls_using_id_tt0000581(self):
        # GIVEN
        # tt0000581 record returns 9 keys but 2 are "\\N" Values
        # test that the [remove_empty_keys()] method length is 7 keys

        tconst = "tt0000581"
        expected = 2
        movie = MovieApi.get_movie_by_id(tconst)

        # WHEN
        result = len(movie)

        # THEN
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

