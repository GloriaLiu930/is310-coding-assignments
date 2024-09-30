favorite_movies = [
    ("Flipped", 2010),
    ("Spirited Away", 2001),
    ("Howl's Moving Castle", 2004),
    ("Gone with the Wind", 1939),
    ("The Truman Show", 1998),
    ("Roman Holiday", 1953),
    ("Coco", 2017),
    ("Batman: The Dark Knight", 2008)
]

def check_movie_year(movie):
    name, year = movie
    if year < 2000:
        print(f"{name} was released before 2000.")
    else:
        print(f"{name} was released after 2000.")
        return name

recent_movies = []

for movie in favorite_movies:
    result = check_movie_year(movie)
    if result is not None:
        recent_movies.append(result)

print("Movies released after 2000:", recent_movies)

