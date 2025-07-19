import streamlit as st
import pickle

def recommend_movies(our_movie, num):
    movie_index = movies_final[movies_final['title'] == our_movie].index[0]
    similarities = cosine_similarity_between_vectors[movie_index]
    recommendations = sorted(list(enumerate(similarities)), reverse=True, key=lambda x: x[1])[1: num + 1]

    recommended_movie_names = []
    for movie in recommendations:
        recommended_movie_names.append(movies_final.iloc[movie[0]].title)
    return recommended_movie_names


st.title("Movie Recommendation System")

movies_final = pickle.load(open('movies_final.pkl', 'rb'))
movies_titles = movies_final['title'].values
cosine_similarity_between_vectors = pickle.load(open('cosine_similarity_between_vectors.pkl', 'rb'))

st.write("Enter your favourite movie and the number of recommended movies you want")
key_movie = st.selectbox('Enter the movie name',movies_titles)
no_of_recommendations = st.slider('How many movies like this do you want?',1,25)
st.divider()
if st.button("Recommend", type="primary"):
    st.write("Here are ", no_of_recommendations, " movies like ", key_movie, " that you might enjoy!")
    recommended_movies = recommend_movies(key_movie, no_of_recommendations)
    for recommendation in recommended_movies:
        container = st.container(border=True)
        container.write(recommendation)

