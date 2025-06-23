from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class AnimeRecommender:
    def __init__(self, anime_df):
        self.anime = anime_df
        self.vectorizer = CountVectorizer(tokenizer=lambda x: x.split(','))
        self.genre_matrix = self.vectorizer.fit_transform(self.anime['genre'])
        self.similarity_matrix = cosine_similarity(self.genre_matrix)
        self.anime_indices = pd.Series(self.anime.index, index=self.anime['name'])

    def recommend(self, anime_name, n=5):
        try:
            idx = self.anime_indices[anime_name]
        except KeyError:
            return f"Anime '{anime_name}' not found in database"
        sim_scores = list(enumerate(self.similarity_matrix[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
        recs = self.anime.iloc[[i[0] for i in sim_scores]][['name','genre','rating']]
        return recs.reset_index(drop=True)
