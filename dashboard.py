import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
from template.navbar import navbar
from template.footer import footer
from content.v_data import layout_graph as data
from content.v_data import table_produk_ekspor_layout as table_ekspor
from content.v_data import table_pemenuhan_bb_layout as table_bb
from content.v_data import table_produksi_olahan_layout as table_olahan
from content.v_data import table_pnbp_layout
from content.v_home import layout as home
from content.analisis import pnbp_tahunan
from content.visualisasi import generate_figure
import dash
import dash_table


# Buat layout dashboard dengan Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])




table_layout = dbc.Container(
    [
        navbar,
        
       dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4("Table PNBP", className="card-title"),
                            table_pnbp_layout
                        ]
                    ),
                    className="p-4 text-center"
                ),
                width={"size": 6, "offset": 3}
            ),
        ],
        className="mt-4"
    ),

    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4("Table Ekspor", className="card-title"),
                            table_ekspor
                        ]
                    )
                ),
                width=6
            ),
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4("Table BB", className="card-title"),
                            table_bb
                        ]
                    )
                ),
                width=6
            )
        ],
        className="mt-4"
    ),
    dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4("Table Olahan", className="card-title"),
                            table_olahan
                        ]
                    )
                ),
                width=6
            ),
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4("Table Ekspor", className="card-title"),
                            table_ekspor
                        ]
                    )
                ),
                width=6
            )
        ],
        className="mt-4 mb-4"
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
    fig_kawasan_pnbp = generate_figure(provinsi)
    return fig_kawasan_pnbp

@app.callback(
    dash.dependencies.Output('table-container', 'children'),
    [dash.dependencies.Input('dropdown-tahun', 'value')]
)
def update_table(tahun):
    filtered_data = pnbp_tahunan[pnbp_tahunan['tahun'] == tahun]
    table = dash_table.DataTable(
        data=filtered_data.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in filtered_data.columns],
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left'},
        editable=True
    )
    return [table]





if __name__ == "__main__":
    try:
        app.run_server(debug=True)
    except Exception as e:
        print(f"Error: {e}")
