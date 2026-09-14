import streamlit as st
import joblib
import difflib

df = joblib.load('movieiinput.pkl')
cs = joblib.load('similarity.pkl')
st.title('Movie Recommendation Sytstem')


movie_name = st.text_input("Enter Movie Name: ") 

if st.button("Recommend Movies:"):
    close_match = difflib.get_close_matches(
        movie_name,
        df['title'],n = 1 
    )


    if close_match:
        movie_index = df[df['title'] == close_match[0]]['index'].iloc[0]
        similar_movies = list(enumerate(cs[movie_index]))
        sorted_similar_movies = sorted(similar_movies, key =  lambda x: x[1], reverse= True)

        st.subheader("Recommended Movies: ")

        i = 1 
        
        for movies in sorted_similar_movies:
            index = movies[0]
            movie_title_from_index = df[df['index'] == index]['title'].iloc[0]

            if i < 21:
                st.write(i,". ",movie_title_from_index)
            i += 1


    else:
        st.error("Movie not found.")        