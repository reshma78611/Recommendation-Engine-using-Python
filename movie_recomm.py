# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:22:48 2020

@author: HP
"""
import numpy as np
import pandas as pd

movie_rating_data=pd.read_csv('C:/Users/HP/Desktop/datasets/Movie.csv')
movie_rating_data.head(5)
sorted_data=np.sort(movie_rating_data.userId)

#no of unique users in dataset
len(movie_rating_data.userId.unique())

#no of unique movies in dataset
len(movie_rating_data.movie.unique())

#build a matrix
movie_rating_data_matrix=movie_rating_data.pivot_table(index='userId',columns='movie',values='rating').reset_index(drop=True)
movie_rating_data_matrix

#replacing index values with userid
movie_rating_data_matrix.index=movie_rating_data.userId.unique()

#impute NAN values with 0
movie_rating_data_matrix.fillna(0,inplace=True)

#to find similarity between users using cosine similarity measure
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine,correlation
user_similarity=1-pairwise_distances(movie_rating_data_matrix.values,metric='cosine')
user_similarity

#store results in dataframe
user_similarity_df=pd.DataFrame(user_similarity)

#set index and column names to userid's
user_similarity_df.index=movie_rating_data.userId.unique()
user_similarity_df.columns=movie_rating_data.userId.unique()
user_similarity_df.iloc[0:5,0:5]
np.fill_diagonal(user_similarity,0)
user_similarity_df.iloc[0:5,0:5]

#most similar user
user_similarity_df.idxmax(axis=1)[0:5]

movie_rating_data[(movie_rating_data['userId']==6)| (movie_rating_data['userId']==168) ]

#recommended movies for userid=6
user1=movie_rating_data[movie_rating_data['userId']==6]
user1.movie

#recommended movies for userid==11
user2=movie_rating_data[movie_rating_data['userId']==11]
user2.movie

pd.merge(user1,user2,on='movie',how='outer')



