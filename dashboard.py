import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from template.navbar import navbar
from template.footer import footer
from content.v_data import content as data
from content.v_data import table_produk_ekspor_layout as table_ekspor
from content.v_home import layout as home
from content.visualisasi import generate_figure
import dash


# Buat layout dashboard dengan Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

table_layout = dbc.Container(
    [
        navbar,
        dbc.Row(
            [
                dbc.Col(table_ekspor, width=6),
                #dbc.Col(table_produksi, width=6)
            ],
            className="mt-4"
        ),
        footer,
    ],
    fluid=True
)

data_layout = html.Div(
    style={
        "background-image": 'url("")',
        "background-size": "cover",
        "background-position": "center",
        "height": "calc(100vh - 100px)",
        "width": "100%",
    },
    children=[
        navbar,
        data,
        footer,
    ]
)
home_layout = html.Div(
    style={
        "background-image": 'url("")',
        "background-size": "cover",
        "background-position": "center",
        "height": "calc(100vh - 100px)",
        "width": "100%",
    },
    children=[
        navbar,
        home,
        footer,
    ]
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    dash.dependencies.Output('page-content', 'children'),
    [dash.dependencies.Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/':
        return home_layout
    if pathname == '/data':
        return data_layout
    if pathname == '/home':
        return home_layout
    if pathname == '/table':
        return table_layout
    else:
        return '404 - Halaman tidak ditemukan'

@app.callback(
    dash.dependencies.Output('grafik-pnbp', 'figure'),
    [dash.dependencies.Input('dropdown-provinsi', 'value')]
)

def update_figure(provinsi):
    fig = generate_figure(provinsi)
    return fig




if __name__ == "__main__":
    try:
        app.run_server(debug=True)
    except Exception as e:
        print(f"Error: {e}")
