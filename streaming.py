
from collections import Counter


class Movie:

    def __init__(self, name, genre, views, rating):
        self.name = name
        self.genre = genre
        self.views = views
        self.rating = rating

    def __repr__(self):
        return f"{self.name} ({self.genre}) - Views: {self.views}, Rating: {self.rating}"


class StreamingPlatform:

    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_most_viewed_movie(self):
        if not self.movies:
            return None
        return max(self.movies, key=lambda m: m.views)

    def get_highly_rated_movies(self, threshold=4.5):
        return [m for m in self.movies if m.rating > threshold]

    def get_total_views(self):
        return sum(m.views for m in self.movies)

    def count_movies_by_genre(self):
        genres = [m.genre for m in self.movies]
        return dict(Counter(genres))

    def sort_movies_by_rating(self, reverse=True):
        return sorted(self.movies, key=lambda m: m.rating, reverse=reverse)



if __name__ == "__main__":
    platform = StreamingPlatform()


    platform.add_movie(Movie("Inception", "Sci-Fi", 1500000, 4.8))
    platform.add_movie(Movie("The Dark Knight", "Action", 2000000, 4.9))
    platform.add_movie(Movie("Superbad", "Comedy", 800000, 4.3))
    platform.add_movie(Movie("Interstellar", "Sci-Fi", 1200000, 4.6))
    platform.add_movie(Movie("Parasite", "Thriller", 950000, 4.6))
    platform.add_movie(Movie("Toy Story", "Animation", 700000, 4.4))


    most_viewed = platform.get_most_viewed_movie()
    print(f"Most Viewed Movie: {most_viewed.name} ({most_viewed.views} views)")
    print("-" * 40)


    print("Movies with rating > 4.5:")
    high_rated = platform.get_highly_rated_movies(4.5)
    for movie in high_rated:
        print(f" - {movie.name}: {movie.rating}")
    print("-" * 40)

    total_views = platform.get_total_views()
    print(f"Total Views Across All Movies: {total_views:,}")
    print("-" * 40)

  
    print("Movie Count by Genre:")
    genre_counts = platform.count_movies_by_genre()
    for genre, count in genre_counts.items():
        print(f" - {genre}: {count}")
    print("-" * 40)

    print("Movies Sorted by Rating:")
    sorted_movies = platform.sort_movies_by_rating()
    for movie in sorted_movies:
        print(f" - {movie.rating}: {movie.name}")

