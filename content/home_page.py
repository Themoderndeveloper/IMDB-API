#!/usr/bin/env python
"""API Home Page Link Code"""


class HomePage:
    @staticmethod
    def home_page_content():
        html0 = "<h2>IMDB Movie API Home Page</h2>"
        html1 = "<p><i>This Website is a simple REST API with two HTTP GET API Endpoints</i></p>"
        html2 = "<p><b>These are the APIs at 127.0.0.1:5000:</b></p>"
        html3 = "<ul><li><a href='/health'>/health</a></li>"
        html4 = "<li><a href='/movies/tconst/tt0000492''>/movies/tconst/tt0000492</a></li>"
        result = html0 + html1 + html2 + html3 + html4
        return result
