from dash import Dash, dcc, html, Input, Output, State
import pandas as pd
import plotly.express as px

avocado = pd.read_csv('avocado.csv')

app = Dash()

app.layout = html.Div([
    html.H1('Avocado prices Dashboard'),
    dcc.Dropdown(id='venue-select', options=avocado['geography'].unique(), value='Albany'),
    dcc.Graph(id='avocado-graph')
])


@app.callback(
    Output('avocado-graph', 'figure'),
    Input('venue-select', 'value')
)
def update_avocado_graph(venue):
    df_filter = avocado['geography'] == venue
    line_fig = px.line(avocado[df_filter], x='date', y='average_price',
                       color='type',
                       title=f'Avocado Prices in {venue}')
    return line_fig


if __name__ == '__main__':
    app.run(debug=True)
