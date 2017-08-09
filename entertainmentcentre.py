import fresh_tomatoes
import media

ToyStory = media.Movie("Toy Story",
                       "A story of a boy and his toys that come to life",
                       "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print ToyStory.storyline

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print avatar.storyline
#avatar.showTrailer()

SingingInTheRain = media.Movie("Singing in the Rain",
                               "Transition from silent to talking movies",
                               "https://upload.wikimedia.org/wikipedia/en/f/f9/Singing_in_the_rain_poster.jpg",
                               "https://www.youtube.com/watch?v=jEKQwy13j_8")
                              
#print SingingInTheRain.storyline
#SingingInTheRain.showTrailer()

SomeLikeItHot = media.Movie ("Some Like it Hot",
                             "Two cross-dressing mucisians on the run from gangsters",
                             "https://upload.wikimedia.org/wikipedia/en/b/b4/Some_Like_It_Hot_poster.jpg",
                             "https://www.youtube.com/watch?v=rI_lUHOCcbc")

Pyscho = media.Movie("Pyscho",
                     "Thief gets more than she'd bargained for in a creepy motel",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/Psycho_%281960%29.jpg/220px-Psycho_%281960%29.jpg",
                     "https://www.youtube.com/watch?v=Ps8H3rg5GfM")

NightAtTheOpera = media.Movie("Night at the Opera",
                              "Marx Brothers at the Opera",
                              "https://upload.wikimedia.org/wikipedia/en/4/45/A_Night_at_the_Opera_Poster.gif",
                              "https://www.youtube.com/watch?v=tu6COUl3fx8")

TheBirds = media.Movie("The Birds",
                       "Terrifying birds attack town",
                       "https://upload.wikimedia.org/wikipedia/commons/c/c0/The_Birds_original_poster.jpg",
                       "https://www.youtube.com/watch?v=0fJh2gIBOto")

movies = [ToyStory, avatar, SingingInTheRain, SomeLikeItHot, NightAtTheOpera, TheBirds]
#fresh_tomatoes.open_movies_page(movies)
