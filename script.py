# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1

# Create a histogram of coach_price
sns.histplot(flight.coach_price)

# Show plot
plt.show()

# Calculate the mean of coach_price
print('Mean of coach_price = {}'.format(np.mean(flight.coach_price)))

# Calculate the median of coach_price
print('Median of coach_price = {}'.format(np.median(flight.coach_price)))

# Clear current plot
plt.clf()

## Task 2

# Create a histogram of coach ticket prices for flights that are 8 hours long
sns.histplot(flight.coach_price[flight.hours == 8])

# Show plot
plt.show()

# Calculate the mean of coach_price that are 8 hours long
print('Mean of coach_price that are 8 hours long = {}'.format(np.mean(flight.coach_price[flight.hours == 8])))

# # Calculate the median of coach_price that are 8 hours long
print('Median of coach_price that are 8 hours long = {}'.format(np.median(flight.coach_price[flight.hours == 8])))

# Clear curren plot
plt.clf()

## Task 3

# Plot a histogram of flight delay times
sns.histplot(flight.delay[flight.delay<=500])

# Show plot
plt.show()

## Task 4

# Clear current plot
plt.clf()

# initialize perc to 0.05
perc = 0.1

# Take random subset of flight dataframe
flight_sub = flight.sample(n = int(flight.shape[0]*perc))

# Plot a Locally Weighted Scatter Smoothing
sns.lmplot(x='coach_price', y='firstclass_price', data=flight_sub, line_kws={'color': 'black'}, lowess=True)

# Show plot
plt.show()

# Clear current plot
plt.clf()

## Task 5

# Create a histogram for inflight_meal flight feature
sns.histplot(data=flight, x='coach_price', hue=flight.inflight_meal)

# Show plot
plt.show()

# Clear current plot
plt.clf()

# Create a histogram for inflight_entertainment flight feature
sns.histplot(data=flight, x='coach_price', hue=flight.inflight_entertainment)

# Show plot
plt.show()

# Clear current plot
plt.clf()

# Create a histogram for inflight_wifi flight feature
sns.histplot(data=flight, x='coach_price', hue=flight.inflight_wifi)

# Show plot
plt.show()

# Clear current plot
plt.clf()

## Task 6

# Create scatter plot by adding jitters
sns.lmplot(x='hours', y='passengers', data=flight_sub, x_jitter=0.25, scatter_kws={'s': 5, 'alpha':0.2}, fit_reg=False)

# Show plot
plt.show()

# Clear current figure
plt.clf()

## Task 7

# Create scatter plot of coach_price and firstclass_price on weekend bases
sns.lmplot(x='coach_price', y='firstclass_price', hue='weekend', data=flight_sub, fit_reg=False)

# Show plot
plt.show()

# Clear current plot
plt.clf()

## Task 8

# Create boxplots
sns.boxplot(x='day_of_week', y='coach_price', hue='redeye', data=flight)

# Show plot
plt.show()