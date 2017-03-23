import webbrowser

class Movie():
    '''This class provides a way to store movie related information'''

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, directed_by, movie_rating):
        '''This constructor method initializes an instance of the class Movie, taking inputs including title, storyline, a poster image, youtube trailer url, director name, and rating, and will output those values to the instance variables listed below.'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_rating = movie_rating
        self.directed_by = directed_by

    def show_trailer(self):
        '''This function will open a browswer window, and navigate to the URL specified by the instance variable trailer_youtube_url'''
        webbrowser.open(self.trailer_youtube_url)
