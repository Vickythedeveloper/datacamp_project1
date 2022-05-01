# import matplotlib and pandas
import matplotlib.pyplot as plt
import pandas as pd
# create a list of movie release years
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
         2019, 2020]
# create a list of corresponding movie duration yearly
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]
# create a dictionary
movie_dict = {'years': years, 'duration': durations}
print(movie_dict)
# create a new dataframe based on movie_dict
duration_df = pd.DataFrame(movie_dict)
print(duration_df)
# set the style
plt.style.use('Solarize_Light2')
# plot a line chart of durations against year
plt.plot(years, durations, linewidth=3)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Duration (min)', fontsize=14)
plt.title('Netflix Average Movie Duration 2011-2020')
plt.xticks([2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
plt.show()