import dash
import dash_core_components as dcc
import dash_html_components as html
from sqlalchemy import *


engine = create_engine('sqlite:///blsdata.db')
conn = engine.connect()
gdp_percap = conn.execute("SELECT * FROM gdp_percap;").fetchall()
exp_by_edu = conn.execute("SELECT * FROM by_edu WHERE edu_level = 03;").fetchall()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Auggie is Bossy'),

    html.Div(children='''
        My question is: How does GDP per capita relate to high school income?
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                # {'x': [item[1] for item in gdp_percap], 'y': [item[2] for item in gdp_percap], 'type': 'bar', 'name': 'GDP'},
                # {'x': [item[1] for item in exp_by_edu], 'y': [item[3] for item in exp_by_edu], 'type': 'bar', 'name': '< HS Income'},
                {'x': [item[1] for item in exp_by_edu], 'y': [item[4] for item in exp_by_edu], 'type': 'bar', 'name': '< HS Housing'},
                {'x': [item[1] for item in exp_by_edu], 'y': [item[5] for item in exp_by_edu], 'type': 'bar', 'name': '< HS FoodHome'},
                {'x': [item[1] for item in exp_by_edu], 'y': [item[6] for item in exp_by_edu], 'type': 'bar', 'name': '< HS FoodAway'},
                {'x': [item[1] for item in exp_by_edu], 'y': [item[7] for item in exp_by_edu], 'type': 'bar', 'name': '< HS AlcBvg'},
            ],
            'layout': {
                'title': 'GDP Per Capita'
                # yaxis = dict(
                #     range=[20000, 50000]
                #     )
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
