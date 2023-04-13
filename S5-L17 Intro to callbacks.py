from dash import Dash, Input, Output, html, dcc

app = Dash()

app.layout = html.Div(children=[
    dcc.Input(id='input_text', value='Some text', type='text'),
    html.P(children=[], id='output_text')
])


@app.callback(
    Output(component_id='output_text', component_property='children'),
    [Input(component_id='input_text', component_property='value')]
)
def update_output_p(input_text):
    return f'Text input: {input_text}'


if __name__ == '__main__':
    app.run(debug=True)
