#!/usr/bin/env python
"""Data Access layer Tests for the Movies JSON Database in Test Driven Development (TDD)."""

import unittest
from data.movie_data import MovieData


class MoviesJsonDataTests(unittest.TestCase):
    def test_create_movie_dictionary_method_is_not_empty(self):
        # GIVEN
        expected = 1
        movies = MovieData.create_movie_dictionary()

        # WHEN
        result = len(movies)

        # THEN
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
