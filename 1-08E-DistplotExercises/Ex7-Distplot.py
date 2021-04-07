#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd


# create a DataFrame from the .csv file:
df = pd.read_csv('../data/iris.csv')


# Define the traces
group_labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']
# HINT:
# This grabs the petal_length column for a particular flower
# df[df['class']=='Iris-some-flower-class']['petal_length']

hist_data = [ 
   df[df['class']==iris]['petal_length'] for iris in group_labels
]



# Define a data variable
# hist_data = [x1,x2,x3,x4]
# group_labels = ['Group1','Group2','Group3','Group4']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data, group_labels)
pyo.plot(fig, filename='distplot_exercise.html')