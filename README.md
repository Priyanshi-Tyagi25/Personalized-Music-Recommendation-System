# Music-Recommendation-System
A Music Recommendation System based on the user's mood, preferred language and collaborative filtering

## Overview
This project is a **Music Recommendation System** that provides personalized song suggestions based on a user's mood, preferred language, and optionally, a reference song. The application uses **collaborative filtering** and **content-based filtering** techniques to recommend songs and is built using **Python** and **Streamlit** for user interaction.

## Features
1. **Mood-based Recommendations**: Suggests songs based on the user's selected mood (e.g., Happy, Sad).
2. **Language-based Filtering**: Filters songs based on the user's preferred language (e.g., English, Hindi).
3. **Collaborative Filtering**: Provides recommendations similar to a reference song selected by the user.
4. **Interactive User Interface**: Built with Streamlit to enable easy user interaction.

## Dataset
The system uses a dataset named `SPOTIFY_DATASET_FOR_RECOMMENDATION.csv`, which contains the following columns:
- `track_name`: The name of the song.
- 'artist_name': The name of the artist.
- 'year': The year the song was released.
- 'popularity': Represents the popularity of the song.
- 'acousticness', 'danceability', 'instrumentalness', 'key': Numeric features representing song characteristics.
- 'liveness', 'loudness', 'speechiness', 'valence': Numeric features representing song characteristics.
- `spotify_link`: Link to the song on Spotify.
- `mood`: The mood associated with the song (e.g., Happy, Sad, Neutral, Energetic, Calm).
- `language`: The language of the song (e.g., English, Hindi).
- `energy` and `tempo`: Numeric features representing song characteristics.

## Installation and Setup
1. Clone this repository to your local machine.
2. Install the required Python libraries:
   ```bash
   pip install pandas numpy scikit-learn streamlit
   ```
3. Place your dataset (`SPOTIFY_DATASET_FOR_RECOMMENDATION.csv`) in the same directory as the project file.
4. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## How It Works
### 1. Preprocessing
- **Encoding Categorical Features**: The `mood` and `language` columns are encoded into numeric values using `astype('category').cat.codes`.
- These encoded features are used for similarity calculations.

### 2. Similarity Matrix
- **Collaborative Filtering**: A similarity matrix is calculated using the `cosine_similarity` function from the **scikit-learn** library. The similarity is based on features such as `energy`, `tempo`, `mood_encoded`, and `language_encoded`.

### 3. Recommendation Function
- **Input Validation**: Ensures the provided mood and language are valid. If a reference song is provided, it verifies its existence in the dataset.
- **Filtering**: Filters songs based on the user's mood and language.
- **Combining Approaches**: Combines mood/language filtering and collaborative filtering results to generate recommendations.

### 4. Streamlit User Interface
- **User Input**: Users can select their mood and language preferences using dropdowns. Optionally, they can also input a reference song.
- **Output**: Displays the recommended songs, each with its name and Spotify link.

## Usage
1. Open the application in your web browser (Streamlit will generate a local link).
2. Select your mood and preferred language from the dropdown menus.
3. Optionally, input a reference song to get collaborative filtering recommendations.
4. Click the **Get Recommendations** button to view the recommended songs.

## Example
### Input:
- Mood: Happy
- Language: English
- Reference Song: "Shape of You"

### Output:
A list of up to 5 recommended songs, such as:
- "Song Name 1" - [Spotify Link](https://spotify.com)
- "Song Name 2" - [Spotify Link](https://spotify.com)

## Tools Dependencies
- Python 3.7+
- pandas
- numpy
- scikit-learn
- streamlit

## Future Improvements
1. Support for more moods and languages.
2. Integration with Spotify's API for dynamic dataset updates.
3. Enhanced recommendation algorithms using deep learning models.
4. Improved UI for better user experience.
5. Providing more data to cover more songs.

## Acknowledgments
- **Streamlit** for providing an easy-to-use framework for building web apps.
- **scikit-learn** for machine learning algorithms and utilities.
- Inspiration from Spotify's music recommendation algorithms.

---
Enjoy discovering new music with the **Music Recommendation System**!

