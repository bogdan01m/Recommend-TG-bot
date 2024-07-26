import pandas as pd
import numpy as np
import re
def get_data():
    data = pd.read_csv('rec_data.csv')
    X = data[['vote_average', 'directors_x1', 'directors_x2', 'directors_cluster', 'genre_x1', 'genre_x2', 'genre_x3', 'genre_cluster', 'cast_x1', 'cast_x2', 'cast_cluster', 'keywords_x1', 'keywords_x2', 'keywords_cluster']]
    data['Название'] = data['заголовок'].apply(lambda x: re.sub(r' \(\d{4}\)', '', x).strip())
    indices = pd.Series(data.index, index=data['Название']).drop_duplicates()
    return X, indices, data
X, indices,data = get_data()