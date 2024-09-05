import streamlit as st
import pickle
import pandas as pd
import requests

similarity =  pickle.load(open('similarity.pkl','rb'))
movies_df = pickle.load(open('movies.pkl','rb'))
movies = movies_df['title'].values



def recommend(movie):
    movie_index = movies_df[movies_df['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]   
    recommended_movies = [] 
    for i in movie_list:
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies

# // fucntion to fetch the poster of the correspond movies 
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data =  response.json
    return "https://image.tmdb.org/t/p/w500" + data['poster']





# def recommend(movie):
#     movie_index = movies_df[movies_df['title']==movie].index[0]
#     distances = similarity[movie_index]
#     movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]   

#     recommended_movies = []
#     recommended_movies_poster = [] 
#     for i in movie_list:
#         recommended_movies.append(movies_df.iloc[i[0]].title)

#         movie_id = movies_df.iloc[i[0]].movie_id
#         recommended_movies_poster.append(fetch_poster(movie_id))
    
#     return recommended_movies, recommended_movies_poster



st.title("🎬 Movie Recommender System")
st.markdown("Enter a movie name and get recommendations for similar movies!")

selected_option= st.selectbox( 'Type or select a movie from the dropdown', movies)

if st.button('Recommned'):
    recommendations = recommend(selected_option)
    st.write('### Here are 5 movies similar to **{}**:'.format(selected_option))
    for i in recommendations:
        st.write(i)


# if st.button('Recommned'):
#     name, poster= recommend(selected_option)

#     col1,col2, col3, col4, col5 = st.beta_columns(5)
#     with col1:
#         st.text(name[0])
#         st.image(poster[0])
#     with col2:
#         st.text(name[1])
#         st.image(poster[1])
#     with col3:
#         st.text(name[2])
#         st.image(poster[2])
#     with col4:
#         st.text(name[3])
#         st.image(poster[3])
#     with col5:
#         st.text(name[4])
#         st.image(poster[4])
    
    





