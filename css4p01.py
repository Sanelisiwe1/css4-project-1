#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:17:25 2024

@author: sanelisiwe
"""


import pandas as pd

df = pd.read_csv("/Users/sanelisiwe/CSS Project IMDB Data/movie_dataset.csv")

print (df)
###Cleaning the data
df.columns = df.columns.str.replace(' ', '_')

df.columns = df.columns.str.replace(' ', '_')


x1 = df["Revenue_(Millions)"].mean()

df["Revenue_(Millions)"].fillna(x1, inplace = True)

x2 = df["Metascore"].mean()

df["Metascore"].fillna(x2, inplace = True)

df = df.sort_values (by=['Rating'], ascending=False)

print(df.describe())

print(df)
##Sorted the ranks from higherst to lowest. According to the ranks The Dark Knight is at the top
print(df.info())

###Question 2 & 3

start_Year = 2015

end_Year = 2015

filtered_df = df[(df['Year'] >= start_Year) & (df['Year'] <= end_Year)]
average_value = filtered_df['Revenue_(Millions)'].mean()

print(average_value)

###Question 4

Year_2016 = df[df['Year'] > 2015]


print(df.info())
print(df.describe())

###Question 5
Chris_Nolan = df[df['Director'] == 'Christopher Nolan']

print(Chris_Nolan)

###Question 6

ratings = df[df['Rating'] >= 8]

print(ratings)

###Question 7
print(Chris_Nolan['Rating'].median())

###Question 8
df.groupby("Year").agg({"Rating":"mean"})

###Question 9

movies_2006 = df[df['Year'] == 2006].shape[0]

movies_2016 = df[df['Year'] == 2016].shape[0]

percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100

print(percentage_increase)

###Question 10

# target_name = 'Bradley Cooper'
# name_frequency = df['Actors'].str.count(target_name).sum()
# print(name_frequency)
###Did this for all the actors names from the question
target_name = 'Mark Wahlberg'
name_frequency = df['Actors'].str.count(target_name).sum()
print(name_frequency)

###Question 11

genres_df = df['Genre'].str.split(',').explode().str.strip()
unique_genres_count = genres_df.nunique()
print(unique_genres_count)


###Question 12

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

correlation = df['Runtime_(Minutes)'].corr(df['Rating'])

# Plot a scatter plot for visualization

sns.lineplot(x='Runtime_(Minutes)', y='Rating', data=df)

plt.title(f'Correlation between Runtime and Rating: {correlation:.2f}')
# plt.show()

correlation = df['Runtime_(Minutes)'].corr(df['Revenue_(Million)'])

