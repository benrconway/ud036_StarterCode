# This is my Movie class, it takes in a title, and urls for both
# poster art and youtube trailer.


class Movie():
    """This class answers the need of a website displaying movies.

    The following attributes are required by the constructor to provide a
    complete instance of this class.
    
    Attributes:
        title (str): The title of the movie.
        poster_image_url (str): A URL of poster art for this movie.
        trailer_youtube_url (str): A URL of the trailer on youtube.

    """
    def __init__(self, title, poster_url, trailer_url):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
