# This is my Movie class, it takes in a title, and urls for both
# poster art and youtube trailer. 
class Movie():
    def __init__(self, title, poster_url, trailer_url):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
