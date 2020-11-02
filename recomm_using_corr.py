# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:33:48 2020

@author: HP
"""
import numpy as np
import pandas as pd

movie_rated_data=pd.read_csv('C:/Users/HP/Desktop/datasets/Movie.csv')
movie_rated_data.shape
movie_rated_data.columns
movie_rated_data.groupby('movie')['userId'].mean().sort_values(ascending=False).head()

# creating dataframe with 'rating' count values 
ratings = pd.DataFrame(movie_rated_data.groupby('movie')['rating'].mean())  
  
ratings['num of ratings'] = pd.DataFrame(movie_rated_data.groupby('movie')['rating'].count()) 
  
ratings.head() 

movie_matrix=movie_rated_data.pivot_table(index='userId',columns='movie',values='rating')
movie_matrix.head()
ratings.sort_values('num of ratings',ascending=False).head(10)

# analysing correlation with similar movies 
ToyStory_user_ratings = movie_matrix['Toy Story (1995)'] 
Heat_user_ratings = movie_matrix['Heat (1995)'] 
  
ToyStory_user_ratings.head() 

# analysing correlation with similar movies 
similar_to_ToyStory = movie_matrix.corrwith(ToyStory_user_ratings) 
similar_to_Heat = movie_matrix.corrwith(Heat_user_ratings) 
  
corr_ToyStory = pd.DataFrame(similar_to_ToyStory, columns =['Correlation']) 
corr_ToyStory.dropna(inplace = True) 
  
corr_ToyStory.head() 

# Similar movies like Tot Story 
corr_ToyStory.sort_values('Correlation', ascending = False).head(10) 
corr_ToyStory= corr_ToyStory.join(ratings['num of ratings']) 
  
corr_ToyStory.head() 
  
corr_ToyStory[corr_ToyStory['num of ratings']>100].sort_values('Correlation', ascending = False).head() 
