# Entertainment Center

This script displays information about movies in an IMDB style.</br> 
Using the class Movie from `media.py` to store information about a film - title, tag-line, trailer etc., it creates a web page with however many Movies we instaciate. 

`fresh_tomatoes.py` was provided by Udacity for the first Front End Web Dev. project.

Information on the movies is gathered through the TMDb API</br>
**This project uses the TMDb API but is not endorsed or certified by TMDb.**


# USAGE

Clone the repo on your local machine.</br>
`python3 entertainment_center.py` in your console will run the program.


## API Key
Visit <https://developers.themoviedb.org/3/getting-started/introduction> and follow the instuctions to get your API key. Once you have your API key, place it here:

```
# Place you API key below. See README for further insctuction.
API_KEY = ""
```
in `entertainment_center.py`.

*Note: When applying for a key you can type N/A in the application URL field*

## Movies
While I have preloaded six movies in the file, you can add more thanks to the TMDb API. The API uses a movie ID to make the call. To find a movie id visit <https://www.themoviedb.org/>, search for a film.

Once at the film's page, the URL should look like this:</br>
<https://www.themoviedb.org/movie/>**someDigits-name-of-movie**

**For example**:</br> 
<https://www.themoviedb.org/movie/399055-the-shape-of-water>

The last part of the URL is the movie ID. Copy the movie ID and add it to the `moive_ID_list` in `entertainment_center.py`.

```
# See README for information on how to locate movie IDs.
movie_id_list = ["862-toy-story", "19995-avatar", "27205-inception",
                 "2062-ratatouille", "1584-school-of-rock",
                 "70160-the-hunger-games"]
```
