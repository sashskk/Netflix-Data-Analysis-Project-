import pandas as pd


df = pd.read_csv('../data/raw/netflix_titles.csv')
# pd.set_option('display.max_rows', None)

def data_overview():
    # Converting date_Added to date-time
    df['date_added'] = df['date_added'].str.strip() # Removing unnecessary spaces
    df['date_added'] = pd.to_datetime(df['date_added'], infer_datetime_format=True)
    # Replacing passes in rating with 'Unknown'
    df['rating'] = df['rating'].fillna('Unknown')
    # Replacing omissions in release_year with 'Unknown'
    df['release_year'] = df['release_year'].fillna('Unknown')
    # Adding a Release Decade (release_decade)
    df['release_decade'] = df['release_year'].round(-1)
    # Adding a month_added category
    df['month_added'] = df['date_added'].dt.month
    # Adding a year_added category
    df['year_added'] = df['date_added'].dt.year
    # Splitting duration into 'duration_value' - number of minutes or seasons, 'duration_type' - type, season, or minutes
    df[['duration_value', 'duration_type']] = df['duration'].str.split(' ', expand=True)
    df['duration_value'] = df['duration_value'].fillna(0)# Replacing NaN with '0'
    df['duration_value'] = df['duration_value'].astype(int)

    return df

df_processed = data_overview()
df_processed.to_csv('cleaned_netflix_titles.csv')




