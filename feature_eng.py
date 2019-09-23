import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

#import all datasets
df_pop = pd.read_csv('data/df_pop.csv')

df_pop.drop(['Unnamed: 0','Romance',
       'Documentary', 'News', 'Sport', 'Biography', 'Drama', 'Crime',
       'Adventure', 'Fantasy', 'Comedy', 'War', 'Family', 'History', 'SciFi',
       'Western', 'Thriller', 'Mystery', 'Horror', 'Action', 'Music', 'Short',
       'Animation', 'Musical', 'FilmNoir', 'TalkShow', 'Adult', 'RealityTV',
       'GameShow'], axis=1, inplace=True)

#get top6 genres to do feature engineering
top6genres = ['romance','drama','documentary','thriller','action','comedy']
top5genres = ['romance','drama','documentary','thriller','action']

#we are flagging only the movies that contain any of the above genres.
def flagit(df):
    
    df['flag']=0
    df['new_genres']=''
    df['genres']=df['genres'].str.lower()
    
    for index,row in df.iterrows():
        flag=0
        print(index)
        movie_genre = row['genres'].split(',')
        #print(movie_genre)

        no_genre=[]
        
        for genre in movie_genre:

        	if genre in top5genres:
        		flag =1

        	else :
        		no_genre.append(genre)       	
            
        
        if flag ==1:
            combined_genre = ",".join(sorted(list(set(movie_genre) - set(no_genre))))
            #print('combined is ',combined_genre)
            df.new_genres[index]=combined_genre
        
        df.flag[index]=flag
        #print('flag is',flag)
        
        
        #print('flag is '+ str(df.flag[index]))
    return df


#test1=df_pop[2000:2100]
#test2 = flagit(test1)

#test2.to_csv(r'/Users/byungchankim/Downloads/Springboard/capstone1/data/test2.csv')

new_pop = flagit(df_pop)
new_pop.to_csv(r'/Users/byungchankim/Downloads/Springboard/capstone1/data/new_pop.csv')
