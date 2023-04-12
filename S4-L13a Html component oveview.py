from dash import Dash, html

app = Dash()

app.layout = html.Div(children=[
    html.H1(children=['World happiness dashboard']),
    html.P(children=['This dashboard shows happiness score',
                     html.Br(),
                     html.A(children=['World happiness score data source'],
                            href='https://worldhappiness.report',
                            target='_blank')])
])

if __name__ == '__main__':
    app.run(debug=True)