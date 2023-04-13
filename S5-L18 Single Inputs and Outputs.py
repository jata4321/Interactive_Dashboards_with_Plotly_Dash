from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

app = Dash()

app.layout = html.Div(children=[
    html.H1(children=['World happiness dashboard']),
    html.P(children=['This dashboard shows happiness score',
                     html.Br(),
                     html.A(children=['World happiness score data source'],
                            href='https://worldhappiness.report',
                            target='_blank')]),
    dcc.Dropdown(id='country-select', options=happiness['country'].unique(), value='Poland'),
    dcc.Graph(id='happiness-plot', figure={})
])


@app.callback(
    Output(component_id='happiness-plot',component_property='figure'),
    Input(component_id='country-select', component_property='value')
)
def update_graph(country):
    line_fig_select = px.line(happiness[happiness['country'] == country],
                              x='year', y='happiness_score',
                              title=f'Happiness score for {country}.')
    return line_fig_select


if __name__ == '__main__':
    app.run(debug=True)
