from dash import Dash, Input, Output, html, dcc

app = Dash()

my_input = dcc.Input(value='', type='text', placeholder="type here")
page_output = html.Div()

app.layout = html.Div([my_input, page_output])


@app.callback(
    Output(component_id=page_output, component_property='children'),
    Input(component_id=my_input, component_property='value')
)
def update_output_paragraph(input_text):
    return f'Text input: {input_text}'


if __name__ == '__main__':
    app.run(debug=True)
