import streamlit as st
import pandas as pd
import neattext.functions as nfx

def extract_features(recommanded_df):
    """
    Extract features from the DataFrame and return them as lists
    """
    course_name_list = list(recommanded_df['course_title'])
    course_url_list = list(recommanded_df['url'])
    course_price_list = list(recommanded_df['price'])
    course_subs_list = list(recommanded_df['num_subscribers'])
    course_level_list = list(recommanded_df['level'])
    course_similarity_list = list(recommanded_df['Similarity_Score'])
    
    return course_name_list, course_url_list, course_price_list, course_subs_list, course_level_list, course_similarity_list

def recommand(df, course_name, cos_sim):
    """
    Input: 
        df: pandas DataFrame, 
        course_name: str,
        cos_sim: ndarray
    output:
        name, url, price, subs, level, similarity: list of str
    """
    course_index = pd.Series(df.index, index=df['Clean_Title']).drop_duplicates()
    index = course_index[course_name]
    scores = list(enumerate(cos_sim[index])) # index, cos_sim
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True) # first item is course_name itself
    recommanded_course_index = [x[0] for x in sorted_scores[1:]]
    recommanded_course_score = [x[1] for x in sorted_scores[1:]]
    recommanded_df = df.loc[recommanded_course_index]
    recommanded_df['Similarity_Score'] = recommanded_course_score
    top_recom_df = recommanded_df.sort_values('Similarity_Score', ascending=False).head(6)
    name, url, price, subs, level, similarity = extract_features(top_recom_df)
    
    return name, url, price, subs, level, similarity

def searchCourse(df, keyword):
    """
    This function search in the course with highest number of subscribers using the keyword 
    """
    try:
        result_df = df[df['course_title'].str.contains(keyword.title())]
        course_name = result_df.sort_values('num_subscribers', ascending=False).head(1).course_title.values[0]
        course_name = nfx.remove_special_characters(course_name)
    
        return course_name
    except:
        st.error(f"Seems like there's no courses relevent to '{keyword}' in the database, may be you misspelled it :man-shrugging::wink:")
        quit()