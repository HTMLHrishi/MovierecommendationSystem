# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python and Machine Learning. The system recommends movies based on the similarity of their genres, keywords, overview, tagline, cast, and director.

## 🚀 Project Overview

This project uses **TF-IDF Vectorization** and **Cosine Similarity** to find movies that are most similar to a movie selected by the user.

The application is deployed as an interactive **Streamlit web application**, allowing users to enter a movie name and receive a list of recommended movies.

## 🧠 How It Works

The recommendation process follows these steps:

1. Load the movie dataset using Pandas.
2. Select relevant movie features:
   - Genres
   - Keywords
   - Overview
   - Tagline
   - Cast
   - Director
3. Combine these features into a single text representation for each movie.
4. Convert the combined text into numerical vectors using **TF-IDF**.
5. Calculate similarity between movies using **Cosine Similarity**.
6. Use `difflib` to find the closest matching movie title when the user enters a movie name.
7. Retrieve the movies with the highest similarity scores.
8. Display the top 20 recommendations through Streamlit.

## 🛠️ Technologies Used

- **Python**
- **Pandas** – Data manipulation and preprocessing
- **NumPy** – Numerical operations
- **Scikit-learn** – TF-IDF Vectorization and Cosine Similarity
- **Joblib** – Saving and loading processed data and similarity matrix
- **Difflib** – Fuzzy movie-title matching
- **Streamlit** – Interactive web application

## 📂 Project Structure

```text
MovieRecommendationSystem/
│
├── app.py
├── movierecommendationsystemproject.py
├── practice.py
├── movies.csv
├── movieiinput.pkl
├── similarity.pkl
└── README.md

```

<img width="1911" height="908" alt="image" src="https://github.com/user-attachments/assets/82e72669-08fd-441c-9513-585b825a19da" />

<img width="1918" height="933" alt="image" src="https://github.com/user-attachments/assets/c2e060e6-3d2f-4adc-9d0c-32e2c048ba2c" />


