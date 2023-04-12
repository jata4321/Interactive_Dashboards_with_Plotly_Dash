from dash import Dash, html, dcc

# Typical html components: H1,H2,...,p,div etc.

app = Dash()

app.layout = html.Div(children=[
    'Hi2'
])

if __name__ == '__main__':
    app.run(debug=True)
