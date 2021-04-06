#######
# Objective: Create a stacked bar chart from
# the file ../data/mocksurvey.csv. Note that questions appear in
# the index (and should be used for the x-axis), while responses
# appear as column labels.  Extra Credit: make a horizontal bar chart!
######

# Perform imports here:
from pandas.core.indexes.base import Index
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd


# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/mocksurvey.csv',
                index_col=0)

# create traces using a list comprehension:
traces = [go.Bar(
    x=df.index,
    y=df[name],
    name=name) for name in df.columns] # set the marker color to bronze

# create a layout, remember to set the barmode here
layout = go.Layout(title={'text':'Mock Survey Results', 'y':0.9, 'x':0.5,},
                            barmode='stack')

# create a fig from data & layout, and plot the fig.
fig = go.Figure(data=traces,layout=layout)
pyo.plot(fig, filename='barchart_exercise.html')