# As per the requirements of our Project, this file will contain the class for
# our movie listing website

class Movie():
    def __init__(self, title, poster_url, trailer_url):
        self.title = title
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url
