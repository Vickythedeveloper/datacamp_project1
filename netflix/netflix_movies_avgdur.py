# import pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
# read the csv file to a DataFrame
netflix_df = pd.read_csv('netflix/netflix_data.csv')
# print the first 5 rows to and columns' info to understand the dataframe
print(netflix_df[0:5])
print(netflix_df.info())
# filter the dataframe for movies
netflix_df_moviesonly = netflix_df[netflix_df['type'] == 'Movie']
# select columns of interest
netflix_movies_col_subset = netflix_df_moviesonly.iloc[:, [1, 2, 5, 10, 7, 8]]
# for the plot, save x and y axes columns
years = netflix_movies_col_subset['release_year']
durations = netflix_movies_col_subset['duration']
# plot the chart
plt.scatter(years, durations)
# label the axes
plt.xlabel('Release Year', fontsize=14)
plt.ylabel('Duration (min)', fontsize=14)
# title the plot
plt.title('Movie Duration by Year of Release', fontsize=20)
plt.savefig('movie_average.png')
# filter movie genres of less than 60 min play
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration'] < 60]
# print frist few rows of short_movies
print(f"\n{short_movies.head(30)}")
# initialize an empty list of colors
colors = []
# iterate through the dateset
for lab, row in netflix_movies_col_subset.iterrows():
    if row['genre'] == 'Children':
        colors.append('red')
    elif row['genre'] == 'Documentaries':
        colors.append('blue')
    elif row['genre'] == 'Stand-Up':
        colors.append('green')
    else:
        colors.append('black')
# plor the chart again
plt.scatter(years, durations, c=colors)
# label the axes
plt.xlabel('Release year', fontsize=14)
plt.ylabel('Duration (min)', fontsize=14)
plt.title('Movie duration by year of release')
plt.savefig('movie_average(1).png')
# Is it certain that movies are getting shorter?
are_movies_getting_shorter = 'maybe'
