import pandas as pd
import sqlite3


#READ DATASET
dataset = pd.read_csv('title.basics.tsv', sep='\t')

#FILTER FOR MOVIES#
type_df = dataset.loc[dataset['titleType'] =='movie' ]

#TRANSFORM RUNTIME COLUMN
pattern = r'^\d+$'
type_df = type_df[type_df['runtimeMinutes'].str.match(pattern)]
type_df['runtimeMinutes'] = type_df['runtimeMinutes'].astype(int)

#FILTER FOR FILMS LESS THAN OR EQUAL TO 90 MINS
runtime_df = type_df[type_df['runtimeMinutes'] <= 90] 

#SPILT GENRE OUT
runtime_df['genre'] = runtime_df['genres'].str.split(',').str[0]

columns_to_drop = ['titleType', 'originalTitle', 'isAdult', 'startYear', 'endYear', 'genres']

final_df = runtime_df.drop(columns_to_drop, axis=1)



#conn = sqlite3.connect('movie_database.db')



# try:
#     final_df.to_sql('Movie_staging', conn, if_exists='replace', index=False)
# except Exception as e:
#     print(f"Failed to process: {e}")


#cur.execute("CREATE TABLE Movies (ID INTEGER PRIMARY KEY AUTOINCREMENT, IMDB_NO CHAR(12) NULL, Title varchar(500) NULL, Runtime_mins INT NULL, Genre Char(50) NULL)")
#cur.execute("insert into movies (IMDB_NO , Title , Runtime_mins , Genre ) select tconst, primaryTitle, runtimeMinutes, genre from Movie_staging")
#conn.commit()













