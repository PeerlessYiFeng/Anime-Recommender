from data_loader import load_and_clean_data
from anime_recommender import AnimeRecommender
from posters import fetch_anime_poster

# Load dataset
anime = load_and_clean_data('anime.csv')

# Just to preview the cleaned data
print(anime[['name','genre','rating']].head())

# Make recommendations
recommender = AnimeRecommender(anime)
print("\nRecommendations for One Piece:\n")
recs = recommender.recommend("One Piece")

if isinstance(recs, str):
    print(recs)
else:
    for i, row in recs.iterrows():
        print(f"{row['name']} ({row['rating']})")
        poster = fetch_anime_poster(row['name'])
        print(f"Poster: {poster if poster else 'Not found'}")
        print("---")
