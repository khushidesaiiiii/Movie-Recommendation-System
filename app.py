import streamlit as st
import pickle
import pandas as pd
import requests

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #E6B0AA;
            color: white;
        }
        .stApp {
            background-color: #E6B0AA;
        }
        .css-1cpxqw2 {
            background-color: #E6B0AA;
        }
        .stButton>button {
            background-color: #e50914;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stSelectbox, .stText {
            font-size: 18px;
        }
        .stImage {
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(255, 255, 255, 0.2);
        }
        h1, .sttitle, .stwrite {
            color: #C0392B;
            text-align: center;
        }
        .stMarkdown {
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=59b8a058748464ae1177ba347a1cf716&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl", "rb"))



#st.write("This is a Streamlit app.")
st.title("Movie Recommendation System")
# st.write("Welcome to the Movie Recommendation System.")
# st.write("This system will recommend movies based on your favorite movies.")

option = st.selectbox(
    'Which movie do you like?',
     movies['title'].values)

if st.button("Recommend"):
    names, poster = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        # st.text(names[0])
        # st.image(poster[0])
        st.markdown(f"""
            <div style='text-align: center;'>
                <img src='{poster[0]}' style='width: 100%; border-radius: 10px; box-shadow: 0 4px 10px rgba(255,255,255,0.2);'><br>
                <p style='color:#1e1e1e; font-size: 16px; margin-top: 10px;'>{names[0]}</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        # st.text(names[1])
        # st.image(poster[1])
        st.markdown(f"""
            <div style='text-align: center;'>
                <img src='{poster[1]}' style='width: 100%; border-radius: 10px; box-shadow: 0 4px 10px rgba(255,255,255,0.2);'><br>
                <p style='color:#1e1e1e; font-size: 16px; margin-top: 10px;'>{names[1]}</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        # st.text(names[2])
        # st.image(poster[2]) 
        st.markdown(f"""
            <div style='text-align: center;'>
                <img src='{poster[3]}' style='width: 100%; border-radius: 10px; box-shadow: 0 4px 10px rgba(255,255,255,0.2);'><br>
                <p style='color:#1e1e1e; font-size: 16px; margin-top: 10px;'>{names[3]}</p>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
            <div style='text-align: center;'>
                <img src='{poster[4]}' style='width: 100%; border-radius: 10px; box-shadow: 0 4px 10px rgba(255,255,255,0.2);'><br>
                <p style='color:#1e1e1e; font-size: 16px; margin-top: 10px;'>{names[4]}</p>
            </div>
        """, unsafe_allow_html=True)
    with col5:
        # st.text(names[4])
        # st.image(poster[4])
        st.markdown(f"""
            <div style='text-align: center;'>
                <img src='{poster[4]}' style='width: 100%; border-radius: 10px; box-shadow: 0 4px 10px rgba(255,255,255,0.2);'><br>
                <p style='color:#1e1e1e; font-size: 16px; margin-top: 10px;'>{names[4]}</p>
            </div>
        """, unsafe_allow_html=True)







