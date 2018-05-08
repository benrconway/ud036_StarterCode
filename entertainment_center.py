# Import the necessary files, media.py and fresh_tomatoes.py
import media
import fresh_tomatoes

# Use the Movie class inside media.py to instantiate some movie objects
# All instances need a title, url for poster art and a url for a youtube trailer
predator = media.Movie("Predator",
                        "https://cdn.shopify.com/s/files/1/1416/8662/product"
                        "s/predator_1987_turkey_original_film_art_800x.jpg?v=1522356369",
                        "https://www.youtube.com/watch?v=K9AT3tQGbIk")

street_fighter = media.Movie("Street Fighter 2: The Animated Movie",
                            "https://vignette.wikia.nocookie.net/"
                            "streetfighter/images/7/7a/SFII_Animated_Movie_"
                            "poster.jpg/revision/latest?cb=20081125205612",
                            "https://www.youtube.com/watch?v=_xlb65hp4lo")

shawshank = media.Movie("The Shawshank Redemption",
                        "https://uk.movieposter.com/posters/archive/main/42/MPW-21321",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

thor_ragnarok = media.Movie("Thor Ragnarok",
                            "http://www.impawards.com/2017/posters/thor_ragnarok.jpg",
                            "https://www.youtube.com/watch?v=ue80QwXMRHg")

mononoke = media.Movie("Princess Mononoke",
                        "https://i.pinimg.com/originals/a4/7f/e8/a47fe8c7"
                        "0b2e5885463f07e1cd7a7104.jpg",
                        "https://www.youtube.com/watch?v=4OiMOHRDs14")

ponyo = media.Movie("Ponyo on the Cliff by the Sea",
                    "http://thecia.com.au/reviews/p/images/ponyo-poster-0.jpg",
                    "https://www.youtube.com/watch?v=CsR3KVgBzSM")



# Assemble those instances in an array for the open_movies_page method
movie_list = [predator, street_fighter, shawshank, ponyo, thor_ragnarok, mononoke]

# Call the method to display them in the web browser
fresh_tomatoes.open_movies_page(movie_list)
