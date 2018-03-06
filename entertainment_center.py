# This script displays information about movies in and IMDB style way. Using
# the class Movie to store information for a film, it creates a webpage with
# however many Movies we instaciate. Movie information is gathered through The
# Movie DB API.

# "This product uses the TMDb API but is not endorsed or certified by TMDb."

import media
import fresh_tomatoes
import json
import http.client

# Place you API key below. See README for further insctuction.
API_KEY = ""

# Prefix for loading poster from API
poster_string_prefix = "https://image.tmdb.org/t/p/w600_and_h900_bestv2/"

# Prefix for loading trailer from API
trailer_string_prefix = "https://www.youtube.com/watch?v="

# List of movies to pass to fresh_tomatoes.open_movies_page()
movies_to_add = []

# Connect to the API
conn = http.client.HTTPSConnection("api.themoviedb.org")

# See README for information on how to locate movie IDs.
movie_id_list = ["862-toy-story", "19995-avatar", "27205-inception",
                 "2062-ratatouille", "1584-school-of-rock",
                 "70160-the-hunger-games"]

# We grab the movie ID from the list to make the API call, create an instance
# of Media and append it to the movies_to_add list.
for movie_id in movie_id_list:
    payload = "{}"
    conn.request("GET", "/3/movie/"+movie_id+"?language=en-US&api_key=" +
                 API_KEY + "&append_to_response=videos", payload)
    res = conn.getresponse()

    # Convert response to json so I can access the information I need through
    # keys.
    data = json.loads(res.read())
    new_movie = media.Movie(data["original_title"], data["tagline"],
                            poster_string_prefix+data["poster_path"],
                            trailer_string_prefix+data["videos"]
                            ["results"][0]["key"])
    movies_to_add.append(new_movie)

# Finally pass list to function to load the web page.
fresh_tomatoes.open_movies_page(movies_to_add)
