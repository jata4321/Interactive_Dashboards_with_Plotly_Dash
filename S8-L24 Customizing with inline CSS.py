from dash import Dash, dcc, html
import pandas as pd

soccer = pd.read_csv('fifa_soccer_players.csv')

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
    html.H1('Soccer Players Dashboard',
            style={'textAlign': 'Center',
                   'fontFamily': 'SF Mono',
                   'fontSize': '50px'}),
    html.P(['Source: ', html.A('Sofifa', href='https://sofifa.com', target='_blank')],
           ),
    html.Label('Player name:'),
    dcc.Dropdown(options=soccer['long_name'].unique(),
                 value=soccer['long_name'].unique()[0])
], style={'padding': 190})

if __name__ == '__main__':
    app.run(debug=True)
