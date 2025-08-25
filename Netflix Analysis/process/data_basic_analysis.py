import pandas as pd
from data_preprocessing import df_processed

df = df_processed

def analyze_basic():
    # How many movies and TV series are there in the dataset
    df_count_type = df.groupby('type')['show_id'].count()
    df_count_type = df_count_type.reset_index()
    df_count_type.columns = ['Category', 'Count']

    # The year in which the most films were released
    df_most_released_year = df.groupby('release_year')['show_id'].count()
    max_year = df_most_released_year.idxmax()

    # The year in which the most content was added to the platform
    df_most_content_year = df.groupby('year_added')['show_id'].count()
    max_content_year = df_most_content_year.idxmax()

    # Top 10 countries in terms of the amount of content
    df_top_countries = df.groupby('country')['show_id'].count()
    df_top_countries = df_top_countries.sort_values(ascending=False).head(10)
    df_top_countries = df_top_countries.reset_index()
    df_top_countries.columns = ['Country', 'Count']

    # Distribution by rating
    df_new = df.copy(deep=True)
    valid_ratings = ['TV-MA', 'TV-14', 'TV-PG', 'R', 'PG-13', 'TV-Y7', 'TV-Y', 'PG', 'TV-G', 'NR', 'G', 'TV-Y7-FV',
                     'Unknown', 'NC-17', 'UR']
    df_new = df[df['rating'].isin(valid_ratings)]
    df_rating_count = df_new['rating'].value_counts()
    df_rating_count = df_rating_count.reset_index()
    df_rating_count.columns = ['Rating', 'Count']


    return (df_count_type,
            max_year, df_most_released_year[max_year],
            max_content_year, df_most_content_year[max_content_year],
            df_top_countries,
            df_rating_count
            )

