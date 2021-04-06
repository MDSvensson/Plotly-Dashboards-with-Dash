#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np


# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/mpg.csv')

# Add columns to the DataFrame to convert model year to a string and
# then combine it with name so that hover text shows both:
df['text1']=pd.Series(df['model_year'],dtype=str)
df['text2']="'"+df['text1']+" "+df['name']
df['horsepower'] = df['horsepower'].apply(lambda x: 0 if x == '?' else x)
df['horsepower'] = pd.to_numeric(df['horsepower'])

# create data by choosing fields for x, y and marker size attributes
data = [go.Scatter(
            x=df['acceleration'],
            y=df['mpg'],
            text=df['text2'],  # use the new column for the hover text
            mode='markers',
            marker=dict(size=0.1*df['horsepower'],
                        color=df['weight'])
    )]

# create a layout with a title and axis labels
layout = go.Layout(
    title=dict(text='Vehicle mpg vs. acceleration',x=0.5),
    xaxis={'title':'Acceleration'},
    yaxis=dict(title='mpg'),
    hovermode='closest'
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble_exercise.html')
