from dash import Dash, html, dcc

# This command launches a dash (similar to Flask)
app = Dash()

# This is section that designs web pages
app.layout = html.Div(children=[
    'This is simple layout 2'
])

# This line runs the server
if __name__ == '__main__':
    app.run_server(debug=True)
