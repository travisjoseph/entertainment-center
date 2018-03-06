import webbrowser


class Movie():
    """Stores information about a film.
    Attributes:
        title (str): Title of movie
        storyline (str): Tag-line for movie
        poster_image_url (str): URL to movie poster
        trailer_youtube_url (str): URL to movie trailer
    """

    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        