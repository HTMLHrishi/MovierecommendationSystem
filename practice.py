import numpy as np
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
import difflib
from sklearn.metrics.pairwise import  cosine_similarity
import joblib


df = pd.read_csv('movies.csv')
print(df.head())

print(df.groupby('genres').describe()[:10])
print(df.info())

dx = df[['genres','keywords','overview','tagline','cast','director']]

print(dx.info())

print(dx.isnull().sum())

for i in dx:
    dx[i] = dx[i].fillna('')

print(dx.isnull().sum())




combined_features = dx['genres']   + dx['keywords'] + dx['overview'] + dx['tagline'] + dx['cast'] + dx['director']

print(combined_features.head())
print(type(combined_features))


#tfidf

tf = TfidfVectorizer()

tf_sparse = tf.fit_transform(combined_features)

print(tf_sparse[:10])


#cosine

cs = cosine_similarity(tf_sparse)
print(cs[:10])


print(df.iloc[0]['title']) #dx doesnt contain title so used df
print(df.iloc[100]['title'])
print('Similarity score: ',end = ' ')
print(cs[0][100])




#user input 

movie_name = input("Enter Movie name: ")

#difflib

find_close_match = difflib.get_close_matches(movie_name,df['title'],n = 1)

print(find_close_match)




#similarity with every movie  and sorting

movie_index = df[df['title'] == find_close_match[0]]['index'].iloc[0]

print(movie_index)


similar_movies = list(enumerate(cs[movie_index]))

print(similar_movies[:10])


sorted_similar_movies = sorted(similar_movies, key =  lambda x: x[1], reverse= True)
print(sorted_similar_movies[:10])



#Movie Recommendation Final Step 
print("Top 20 movie suggested for User")



"""index = sorted_similar_movies[0][0] as its a tuple """ 

i = 1 

for movies in sorted_similar_movies:
    index = movies[0]
    movie_title_from_index = df[df['index'] == index]['title'].iloc[0]

    if i < 21:
        print(i,". ",movie_title_from_index)
        i += 1
    

joblib.dump(cs,'similarity.pkl')
joblib.dump(df,'movieiinput.pkl')
