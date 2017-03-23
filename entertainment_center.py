import media
import fresh_tomatoes

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',  # noqa
                        'https://www.youtube.com/watch?v=vwyZH85NQC4',
                        'John Lasseter',
                        'G')

avatar = media.Movie('Avatar',
                    'A marine on an alien planet',
                    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg',  # noqa
                    'http://www.youtube.com/watch?v=-9ceBgWV8io',
                    'James Cameron',
                    'PG-13')

from_paris = media.Movie('From Paris with Love',
                        'In Paris, a young employee in the office of the US Ambassador hooks up with an American spy looking to stop a terrorist attack in the city.',  # noqa
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BNDUyMzExOTAyM15BMl5BanBnXkFtZTcwMTU0NjAyMw@@._V1_.jpg',  # noqa
                        'https://www.youtube.com/watch?v=zWPcLynIZvc',
                        'Pierre Morel',
                        'R')

son_in_law = media.Movie('Son-in-Law',
                        'Having gotten a taste of college life, a drastically changed farm girl returns home for Thanksgiving break with her best friend, a flamboyant party animal who is clearly a fish out of water in a small farm town.',  # noqa
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNDkyODMwN15BMl5BanBnXkFtZTYwODA3NjU5._V1_.jpg',  # noqa
                        'https://www.youtube.com/watch?v=K0ImPG1KzSI',
                        'Steve Rash',
                        'PG-13')

catch_me_if_you_can = media.Movie('Catch Me If You Can',
                                'The true story of Frank Abagnale Jr. who, before his 19th birthday, successfully conned millions of dollars worth of checks as a Pan Am pilot, doctor, and legal prosecutor.',  # noqa
                                'https://images-na.ssl-images-amazon.com/images/M/MV5BMTY5MzYzNjc5NV5BMl5BanBnXkFtZTYwNTUyNTc2._V1_.jpg',  # noqa
                                'https://www.youtube.com/watch?v=71rDQ7z4eFg',
                                'Steven Spielberg',
                                'PG-13')

star_wars = media.Movie('Star Wars: Episode IV A New Hope',
                        'Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a wookiee and two droids to save the galaxy from the Empires world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader.',  # noqa
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BYzQ2OTk4N2QtOGQwNy00MmI3LWEwNmEtOTk0OTY3NDk2MGJkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,664,1000_AL_.jpg',  # noqa
                        'https://www.youtube.com/watch?v=9gvqpFbRKtQ',
                        'George Lucas',
                        'PG')

movies = [toy_story, avatar, from_paris, son_in_law, catch_me_if_you_can, star_wars]  # noqa

#This open_movies_page method will create the file fresh_tomatoes.html, or
#overwrite an exisiting file if necessary.
#This file will display all movie data as formatted in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
