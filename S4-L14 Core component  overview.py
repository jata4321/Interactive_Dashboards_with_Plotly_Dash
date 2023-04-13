from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

line_fig = px.line(happiness[happiness['country'] == 'United States'],
                   x='year', y='happiness_score', title='Happiness score')

app = Dash()

app.layout = html.Div(children=[
    html.H1(children=['World happiness dashboard']),
    html.P(children=['This dashboard shows happiness score',
                     html.Br(),
                     html.A(children=['World happiness score data source'],
                            href='https://worldhappiness.report',
                            target='_blank')]),
    dcc.RadioItems(options=happiness['region'].unique(), value='North America'),
    dcc.Checklist(options=happiness['region'].unique(), value=['North America']),
    dcc.Dropdown(options=happiness['country'].unique(), value='United States'),
    dcc.Graph(figure=line_fig)
])

if __name__ == '__main__':
    app.run(debug=True)
