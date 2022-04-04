import pandas as pd
import streamlit as st
import pickle
import  requests
# import os
# ON_HEROKU = os.environ.get('ON_HEROKU')

# if ON_HEROKU:
#     # get the heroku port
#     port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
# else:
#     port = 3000
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
simliarity=pickle.load(open('Simliarity.pkl','rb'))
############################################################################################################################################
def fetch_posters(movie_id):
      response=requests.get('https://api.themoviedb.org/3/movie/{}%7D?api_key=640dcb945f38d83e87018332ce98e0ec&language=en-US'.format(movie_id))
      data=response.json()
      return "https://image.tmdb.org/t/p/w500"+data['poster_path']
################################################################################################################################################
def recommend(movie):
    d1=movies[movies['title']==movie].index[0]
    distances=simliarity[d1]
    movies_list=sorted(enumerate(distances),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
########################################################################################################
    for i in movies_list:
        movieid=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_posters(movieid))
    return recommended_movies,recommended_movies_posters
st.title('Movie Reccomendation')
option = st.selectbox(
'Select a movie that you liked!!',
movies['title'].values)

if st.button('Recommend'):
     name,posters=recommend(option)
     col1,col2,col3,col4,col5=st.columns(5)
     with col1:
         st.text(name[0])
         st.image(posters[0])
     with col2:
         st.text(name[1])
         st.image(posters[1])
     with col3:
         st.text(name[2])
         st.image(posters[2])
     with col4:
         st.text(name[3])
         st.image(posters[3])
     with col5:
         st.text(name[4])
         st.image(posters[4])
