# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:06:02 2020

@author: HP
"""
import numpy as np
import pandas as pd

book_rating_data=pd.read_csv('C:/Users/HP/Desktop/assignments submission/recommendations/book.csv',encoding='ISO-8859-1')
book_rating_data.columns
book_rating_data.columns=['sr_no','user_id','book_title','book_rating']
book_rating_data.head()
len(book_rating_data.user_id.unique())
len(book_rating_data.book_title.unique())

book_rating_data_matrix=book_rating_data.pivot_table(index='user_id',columns='book_title',values='book_rating').reset_index(drop=True)
book_rating_data_matrix

book_rating_data_matrix.index=book_rating_data.user_id.unique()
book_rating_data_matrix.fillna(0,inplace=True)

from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine,correlation
user_similarity=1-pairwise_distances(book_rating_data_matrix.values,metric='cosine')
user_similarity

#store results in dataframe
user_similarity_df=pd.DataFrame(user_similarity)

#set index and column names to userid's
user_similarity_df.index=book_rating_data.user_id.unique()
user_similarity_df.columns=book_rating_data.user_id.unique()
user_similarity_df.iloc[0:5,0:5]
np.fill_diagonal(user_similarity,0)
user_similarity_df.iloc[0:5,0:5]

#most similar user
user_similarity_df.idxmax(axis=1)[0:5]


#recommended books for userid==276726
user1=book_rating_data[book_rating_data['user_id']==276726]
user1.book_title





