from dash import Dash, html, dcc, Input, Output, State
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

app = Dash()
score_type_dict = dict(happiness_rank='Happiness Rank', happiness_score='Happiness Score')
app.layout = html.Div(children=[
    html.H1(children=['World happiness dashboard']),
    html.P(children=['This dashboard shows happiness score',
                     html.Br(),
                     html.A(children=['World happiness score data source'],
                            href='https://worldhappiness.report',
                            target='_blank')]),
    dcc.RadioItems(id='region-select', options=happiness['region'].unique(), value='Central and Eastern Europe'),
    dcc.Dropdown(id='country-select', options=happiness['country'].unique(), value='Poland'),
    dcc.RadioItems(id='score-type-select', options=score_type_dict, value='happiness_score'),
    html.P(),
    html.Button(id='submit-button', n_clicks=0, children='Update data'),
    dcc.Graph(id='happiness-plot'),
    html.Div(id='text-area', children=[]),
    dcc.Graph(id='average-happiness-plot')
])


@app.callback(
    Output('country-select', 'options'),
    Output('country-select', 'value'),
    Input('region-select', 'value')
)
def change_dropdown(region):
    countries_df = happiness[happiness['region'] == region]
    countries_df = countries_df['country'].unique()
    return countries_df, countries_df[0]


@app.callback(
    Output('happiness-plot', 'figure'),
    Output('average-happiness-plot', 'figure'),
    Output('text-area', 'children'),
    Input('submit-button','n_clicks'),
    State(component_id='country-select', component_property='value'),
    State(component_id='region-select', component_property='value'),
    State(component_id='score-type-select', component_property='value')
)
def update_graph(button_click, country, region, score_type):
    filtered_line_df = happiness[(happiness['country'] == country) & (happiness['region'] == region)]
    variable_display = score_type_dict[score_type]
    line_fig_select = px.line(filtered_line_df, x='year', y=score_type, title=f'{variable_display} for {country}.')

    average_value = filtered_line_df[score_type].mean().round(4)

    filtered_bar_df = happiness[happiness['region'] == region]
    filtered_bar_df = pd.pivot_table(filtered_bar_df, index='country', values=score_type)
    bar_fig_select = px.bar(filtered_bar_df, y=score_type, title=f'Average {variable_display} for {region}.')

    return line_fig_select, bar_fig_select, f'Average of {variable_display} for {country} is {average_value}'


if __name__ == '__main__':
    app.run(debug=True)
