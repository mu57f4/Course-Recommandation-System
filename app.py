import streamlit as st
from modules import *
from card import card

import pandas as pd
import neattext.functions as nfx
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.header("Course Recommander Systerm Using Machine Learning :books: :computer:")
df = pd.read_csv('data/udemy_course_data.csv')
df['Clean_Title'] = df['course_title'].apply(nfx.remove_stopwords)
df['Clean_Title'] = df['course_title'].apply(nfx.remove_special_characters)

countVect = CountVectorizer()
cvmat = countVect.fit_transform(df['Clean_Title'])
cos_sim = cosine_similarity(cvmat)

keyword = st.text_input(
    label="Input a Keyword or course name",
    max_chars=150,
    # placeholder="Python"
)

if st.button('Show Recommandation'):
    try:
        name_list, url_list, price_list, subs_list, level_list, simil_list = recommand(df, keyword, cos_sim)
        # starts from 1 cus the item[0] is the keywork course itself
        card(name_list[1:], url_list[1:], price_list[1:], subs_list[1:], level_list[1:])
    except:
        course_name = searchCourse(df, keyword)
        name_list, url_list, price_list, subs_list, level_list, simil_list = recommand(df, course_name, cos_sim)
        card(name_list, url_list, price_list, subs_list, level_list)
