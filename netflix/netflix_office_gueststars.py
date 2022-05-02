# import matplotlib.pyplot and pandas
import matplotlib.pyplot as plt
import pandas as pd
# read the csv file to a DataFrame
office_epi = pd.read_csv('datacamp_project1/netflix/office_episodes.csv')
# print info about the dataset
print(f"{office_epi.head(7)}\n{office_epi.info()}")
# create a new dataftame with interested columns only
office_epi_subset = office_epi.iloc[:, [0, 6, 9, 12, 13]]
# initialize empty lists of colors and sizes
sizes = []
colors = []
# interate over every row data
for lab, row in office_epi_subset.iterrows():
    if row['scaled_ratings'] < 0.25:
        colors.append('red')
    elif (row['scaled_ratings'] >= 0.25) and (row['scaled_ratings'] < 0.5):
        colors.append('gray')
    elif (row['scaled_ratings'] >= 0.5) and (row['scaled_ratings'] < 0.75):
        colors.append('blueviolet')
    else:
        colors.append('darkgreen')
# iterate again to get the sizing system
for lab, row in office_epi_subset.iterrows():
    if row['has_guests'] == True:
        sizes.append(250)
    else:
        sizes.append(25)
# set a style
plt.style.use('dark_background')
# save x and y axes
epi_no = office_epi['episode_number']
viewership = office_epi['viewership_mil']
# plot the scatterplot chart
plt.scatter(epi_no, viewership, c=colors, s=sizes)
# label axes
plt.xlabel('Episode Number', fontsize=14)
plt.ylabel('Viewership (Millions)', fontsize=14)
plt.title('Popularity, Quality, and Guest Appearances on the Office', fontsize=20)
plt.savefig('datacamp_project1/netflix/office_episodes.png')
# save the most viewed episode
most_viewed = office_epi[office_epi['viewership_mil'] > 20]
# save the guest stars on the most viewed episode
gueststars_most_viewed = most_viewed['guest_stars']
