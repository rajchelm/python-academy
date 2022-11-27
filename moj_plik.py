movie = {
    "title": "Titanic",
    "year": 2000,
    "budget": 221645.69,
    "cinema_premiere": True,
    "avability": ["cinema", "vod", "dvd"],
    "actors": ("leonardo", "abc", "many_others")
}
print(movie)
print(f"{movie['title']} is a movie available from {movie['year']}")