import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import random
st.title("My Anime Recommender")

cv = CountVectorizer(max_features = 1000, stop_words='english')
@st.cache
def data_load():
    animedict=pickle.load(open('animedict.pkl' , 'rb'))
    animes = pd.DataFrame(animedict)
    new_df = pickle.load(open('newdf.pkl' , 'rb'))
    vectors = cv.fit_transform(new_df['Tags']).toarray()
    similarity = cosine_similarity(vectors)

    return animes,similarity

animes , similarity = data_load()

data_load()

sel_anime = st.selectbox(
    'Which anime do you like ??' ,
    animes['title'].values
)


def recommend(anime ):
    anime_index = animes[animes['title']==anime].index[0]
    distances = similarity[anime_index]
    anime_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:51]
    recc_anime=[]
    recc_anime_id=[]
    for i in anime_list:
        recc_anime.append(animes['title'][i[0]])
        recc_anime_id.append(i[0])


    return recc_anime_id , recc_anime


if st.button("Recommend bruh!!"):
    id , names = recommend(sel_anime  )

    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        x=random.randint(0,50)
        st.write(names[x])
        st.image(animes['img_url'][id[x]])
        st.write("Score :" , animes['score'][id[x]])


    with col2:
        y = random.randint(0, 50)
        st.write(names[y])
        st.image(animes['img_url'][id[y]])
        st.write("Score :", animes['score'][id[y]])

    with col3:
        z = random.randint(0, 50)
        st.write(names[z])
        st.image(animes['img_url'][id[z]])
        st.write("Score :", animes['score'][id[z]])

    with col4:
        u = random.randint(0, 50)
        st.write(names[u])
        st.image(animes['img_url'][id[u]])
        st.write("Score :", animes['score'][id[u]])

    with col5:
        v = random.randint(0, 50)
        st.write(names[v])
        st.image(animes['img_url'][id[v]])
        st.write("Score :", animes['score'][id[v]])




