#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
# Range slider is the component to use
######

# Perform imports here:
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div([
    dcc.RangeSlider(
        id='my-range-slider',
        min=-5,
        max=6,
        step=1,
        marks={i:str(i) for i in range(-5,7,1)},
        value=[-2, 6]
    ),
    html.Br(),  # add a horizontal rule
    html.H1(id='output-container-range-slider')
], style={'fontFamily':'helvetica', 'fontSize':22})

# Create a Dash callback:
@app.callback(
    Output('output-container-range-slider', 'children'),
    [Input('my-range-slider', 'value')])
def update_output(value):
    # Multiply elements one by one
    result = 1
    for x in value:
         result = result * x
    return '{}'.format(result)

# Add the server clause:
if __name__ == '__main__':
    app.run_server()
