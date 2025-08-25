import pandas as pd
from data_preprocessing import df_processed

df = df_processed


def analyze_advanced():
    # Director with the most movies/TV series
    df_director = df.groupby('director')['show_id'].count()
    df_director = df_director.sort_values(ascending=False).head(1)

    # TOP 10 Directors with the most films/TV series
    df_director1 = df.groupby('director')['show_id'].count()
    df_director1 = df_director1.sort_values(ascending=False).head(10)
    df_director1 = df_director1.reset_index()
    df_director1.columns = ['Director', 'Count']

    # The actor who is most often found in the cast
    df_actor = df.copy(deep=True)
    df_actor['cast_list'] = df_actor['cast'].str.split(', ') # Breaking up the actors through ', '
    df_actor = df_actor.explode('cast_list')
    df_actor = df_actor['cast_list'].value_counts().head(1)

    # TOP 10 popular actors
    df_actor1 = df.copy(deep=True)
    df_actor1['cast_list'] = df_actor1['cast'].str.split(', ')  # Breaking up the actors through ', '
    df_actor1 = df_actor1.explode('cast_list')
    df_actor1 = df_actor1['cast_list'].value_counts().head(10)
    df_actor1 = df_actor1.reset_index()
    df_actor1.columns = ['Actor', 'Count']

    # Top 5 most popular genres
    top5_genres = df.copy(deep=True)
    top5_genres['genres'] = top5_genres['listed_in'].str.split(', ')
    top5_genres = top5_genres.explode('genres')
    top5_genres = top5_genres['genres'].value_counts().head(5)
    top5_genres = top5_genres.reset_index()
    top5_genres.columns = ['Genre', 'Count']

    # Average duration of movies
    mean_time_movie_mask = df[df['type'] == 'Movie']
    mean_time_movie = mean_time_movie_mask['duration_value'].mean().round(2)

    # Average number of seasons for TV series
    mean_seasons_show_mask = df[df['type'] == 'TV Show']
    mean_seasons_show = mean_seasons_show_mask['duration_value'].mean().round(2)

    return (df_director,
            df_actor,
            top5_genres,
            mean_time_movie,
            mean_seasons_show,
            mean_time_movie_mask, # for visualization
            df_actor1,
            df_director1
            )


