#importing dependancies 

import pandas as pd
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer
import difflib
from sklearn.metrics.pairwise import cosine_similarity
import joblib 

df = pd.read_csv('movies.csv')

print(df.head())

print(df.groupby('original_language').describe()[:10])

print(df.shape)

print(df.info())

#counting th number of english movies
print(len(df[df['original_language'] == 'en']))



#selecting relevant features

X = df[['genres','keywords','overview','tagline','cast','director']]


#replacing string null values with "";

for i in X:
    X[i] = X[i].fillna('')

print(X.info())



#combining all the features

combined_features = X['genres'] + X['keywords'] + X['overview'] + X['tagline'] + X['cast'] + X['director']

print(combined_features.head())

df['combined_features'] = combined_features


#convert this textual data to numerical values

tf = TfidfVectorizer()

tf_sparse = tf.fit_transform(df['combined_features'])

print(tf_sparse)

#the values like 0.05 mean very little importance the word has to this current movie title


#Cosine Similarity

similarity = cosine_similarity(tf_sparse)

print(similarity)

print(similarity[:5])

#check similarity between 1 and 10 

print(df.iloc[0]['title'])
print(df.iloc[10]['title'])
print("similarity = ",similarity[0][10])
print(similarity[813])


#Enter Movie name 

movie_name = input("Enter your movie name:")
movie_list2 = df['title']
movie_list = df['title'].tolist()
print(movie_list[:50])


#doing difflib to find the closest match to the  user's input as user might have made a mistake

find_close_match = difflib.get_close_matches(movie_name,movie_list2,n=1)

print(find_close_match)


index_movie = df[df['title'] == find_close_match[0]].index[0]
print(index_movie)



#getting a list of similar movies

similarity_score = list(enumerate(similarity[index_movie]))
print(similarity_score[770:780])

print(len(similarity_score))



#sorting the similar movies based on similarity 

sorted_similar_movies = sorted(similarity_score,key = lambda x: x[1], reverse= True)
print(sorted_similar_movies[:10])




#top 20 movies based on similarity and printing the title

print('Movies suggested for User: \n') 


i = 1

for movies in sorted_similar_movies:
    index = movies[0]
    movie_title_from_index = df[df['index'] == index]['title'].iloc[0]
    print(i, ' ', movie_title_from_index)

    if i <20:
        i += 1
    else:
        break

#movie derecommendation system 
"""print('Movie Derecommendation System')
i =1 

for movies in sorted_similar_movies[-20:][::-1]:
    index = movies[0]
    movie_title_from_index = df[df['index'] == index]['title'].iloc[0]
    print(i, ' ', movie_title_from_index)

    if i < 20:
        i += 1
    else:
        break """





