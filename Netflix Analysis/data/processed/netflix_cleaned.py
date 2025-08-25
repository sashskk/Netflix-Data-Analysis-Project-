import pandas as pd
from process.data_preprocessing import df_processed
# Processed data file

df_processed.to_csv('cleaned_netflix_titles.csv')