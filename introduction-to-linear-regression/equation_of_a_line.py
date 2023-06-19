# Load libraries
# import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the data
students = pd.read_csv('data/test_data.csv')

# Write equation for a line

## Original line: too steep
# predicted_score = 25 * students.hours_studied + 20

## New line: adjusted slope
# predicted_score = 10 * students.hours_studied + 20

## Final line: adjusted slope and constant (y-intercept)
predicted_score = 10 * students.hours_studied + 45

# Create the plot
plt.scatter(students.hours_studied, students.score)
plt.plot(students.hours_studied, predicted_score)
plt.show()