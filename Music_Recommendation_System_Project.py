#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Sample dataset (replace with your actual dataset)
df=pd.read_csv("SPOTIFY_DATASET_FOR_RECOMMENDATION.csv")

# Preprocessing: Encode categorical features for mood and language
df['mood_encoded'] = df['mood'].astype('category').cat.codes
df['language_encoded'] = df['language'].astype('category').cat.codes

# Calculate song similarity using collaborative filtering
def calculate_similarity_matrix():
    feature_columns = ['energy', 'tempo', 'mood_encoded', 'language_encoded']
    similarity_matrix = cosine_similarity(df[feature_columns])
    return pd.DataFrame(similarity_matrix, index=df['track_name'], columns=df['track_name'])

similarity_matrix = calculate_similarity_matrix()

# Recommendation function
def recommend_songs(mood, language, reference_song=None, top_n=5):
    # Encode mood and language
    mood_map = {m: i for i, m in enumerate(df['mood'].astype('category').cat.categories)}
    lang_map = {l: i for i, l in enumerate(df['language'].astype('category').cat.categories)}

    mood_encoded = mood_map.get(mood.lower(), -1)
    language_encoded = lang_map.get(language.capitalize(), -1)

    if mood_encoded == -1 or language_encoded == -1:
        return "Invalid mood or language. Please try again."

    # Step 1: Filter songs by mood and language
    filtered_songs = df[
        (df['mood_encoded'] == mood_encoded) & (df['language_encoded'] == language_encoded)
    ]['track_name'].tolist()

    # Step 2: Collaborative filtering
    collaborative_recommendations = []
    if reference_song and reference_song in similarity_matrix.columns:
        similar_songs = similarity_matrix[reference_song].sort_values(ascending=False).index[1:top_n + 1]
        collaborative_recommendations = list(similar_songs)

    # Combine both approaches
    final_recommendations = set(filtered_songs + collaborative_recommendations)

    if not final_recommendations:
        return "No songs found for the selected mood, language, or reference song."

    return list(final_recommendations)

# Streamlit app for user interaction
st.title("Music Recommendation System")

# Get user input for mood and language
mood = st.selectbox(
    "What's your mood right now?",
    options=["Happy", "Sad", "Calm", "Energetic", "Neutral"]
)

language = st.selectbox(
    "Preferred language for songs:",
    options=["Hindi", "English"]
)

# Optional: Ask the user for a reference song
reference_song = st.text_input(
    "Enter a reference song (optional):",
    placeholder="Enter a song name from your playlist..."
)

# Get recommendations on button click
if st.button("Get Recommendations"):
    recommendations = recommend_songs(mood, language, reference_song)
    if isinstance(recommendations, str):  # If it's an error message
        st.error(recommendations)
    else:
        st.success("Here are your song recommendations:")
        for song in recommendations:
            st.write(f"- {song}")


# In[ ]:




