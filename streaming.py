movies = [
    {"name": "Inception", "genre": "Sci-Fi", "views": 1500000, "rating": 4.8},
    {"name": "The Dark Knight", "genre": "Action", "views": 2000000, "rating": 4.9},
    {"name": "Superbad", "genre": "Comedy", "views": 800000, "rating": 4.3},
    {"name": "Interstellar", "genre": "Sci-Fi", "views": 1200000, "rating": 4.6},
    {"name": "Parasite", "genre": "Thriller", "views": 950000, "rating": 4.6},
    {"name": "Toy Story", "genre": "Animation", "views": 700000, "rating": 4.4}
]


most_viewed = max(movies, key=lambda x: x["views"])
print(f"Most Viewed Movie: {most_viewed['name']} ({most_viewed['views']} views)")
print("-" * 40)


print("Movies with rating > 4.5:")
for movie in movies:
    if movie["rating"] > 4.5:
        print(f" - {movie['name']}: {movie['rating']}")
print("-" * 40)


total_views = sum(movie["views"] for movie in movies)
print(f"Total Views: {total_views}")
print("-" * 40)


genre_counts = {}
for movie in movies:
    genre = movie["genre"]
    if genre in genre_counts:
        genre_counts[genre] += 1
    else:
        genre_counts[genre] = 1

print("Movie Count by Genre:")
for genre, count in genre_counts.items():
    print(f" - {genre}: {count}")
print("-" * 40)

# 5. Sort movies by rating (Highest to Lowest)
sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
print("Movies Sorted by Rating:")
for movie in sorted_movies:
    print(f" - {movie['rating']}: {movie['name']}")

