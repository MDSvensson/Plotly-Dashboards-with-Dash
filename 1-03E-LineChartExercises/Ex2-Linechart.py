#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('../data/2010YumaAZ.csv')
df.set_index('DAY', inplace=True)

days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

# Use a for loop (or list comprehension to create traces for the data list)
data = [go.Scatter(
    x=df['LST_TIME'].loc[day],
    y=df['T_HR_AVG'].loc[day],
    mode='lines',
    name=day
)
for day in days]

layout = go.Layout(title='Temperature variation per week day')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='line_exercise.html')

# for day in days:
#     # What should go inside this Scatter call?
#     trace = go.Scatter(x=, y=, mode=, name=)
#     data.append(trace)

# Define the layout





# Create a fig from data and layout, and plot the fig
