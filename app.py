import streamlit as st
from data_loader import load_and_clean_data
from anime_recommender import AnimeRecommender
from posters import fetch_anime_poster

#load data and build recommender
anime_df = load_and_clean_data("anime.csv")
recommender = AnimeRecommender(anime_df)

#app title
st.title("Anime Recommender")
st.markdown("Get anime recommendations based on your favourite show")

#dropdown menu
anime_list = anime_df['name'].sort_values().tolist()
selected_anime = st.selectbox("Select an anime you like", anime_list)

#recommend button
if st.button("Recommend"):
    recs = recommender.recommend(selected_anime)

    if isinstance(recs, str):
        st.warning(recs)
    else:
        st.subheader(f"Recommendations for **{selected_anime}**")
        for i, row in recs.iterrows():
            poster_url = fetch_anime_poster(row['name'])
            cols = st.columns([1,4])
            with cols[0]:
                if poster_url:
                    st.image(poster_url, width=100)
                else:
                    st.text("No Image")
            with cols[1]:
                st.markdown(f"**{row['name']}** \n⭐ {row['rating']} \n*{row['genre']}*")
                st.markdown("---")
