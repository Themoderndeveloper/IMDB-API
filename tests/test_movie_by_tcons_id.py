#!/usr/bin/env python
"""Data Access layer Tests for the Movies JSON Database in Test Driven Development (TDD)."""

import unittest
from data.movie_data import MovieData


class MovieByTconstIdTests(unittest.TestCase):
    def test_create_movie_dictionary_method_is_not_empty(self):
        # GIVEN
        tconst = 'tt0000001'
        expected = 'Carmencita'
        movie = MovieData.get_movie_by_tconst_id(tconst)

        # WHEN
        result = movie['primaryTitle']

        # THEN
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()