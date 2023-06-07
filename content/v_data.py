
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from .visualisasi import available_provinces
from .analisis import unique_products


content = dbc.Container([
    html.Div(className="mt-4"),
    dbc.Row([
        dbc.Col(html.H1('PNBP Fraud Detection Dashboard', className='text-center mb-4'), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H2('Grafik PNBP')),
                dbc.CardBody([
                    dcc.Dropdown(
                        id='dropdown-provinsi',
                        options=[{'label': provinsi, 'value': provinsi} for provinsi in available_provinces],
                        value=available_provinces[0]
                    ),
                    dcc.Graph(id='grafik-pnbp')
                ])
            ], className="mx-auto", style={'width': '75%'})
        ], width=12),
    ], className='mb-4'),
])

card_style = {'width': '25rem', 'margin': '1rem'}
content = dbc.Container([
    html.Div(className="mt-4"),
    dbc.Row([
        dbc.Col(html.H1('PNBP Fraud Detection Dashboard', className='text-center mb-4'), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H2('Grafik PNBP')),
                dbc.CardBody([
                    dcc.Dropdown(
                        id='dropdown-provinsi',
                        options=[{'label': provinsi, 'value': provinsi} for provinsi in available_provinces],
                        value=available_provinces[0]
                    ),
                    dcc.Graph(id='grafik-pnbp')
                ])
            ], className="mx-auto", style={'width': '75%'})
        ], width=12),
    ], className='mb-4'),
])

table_produk_ekspor = dbc.Table(
    [
        # Header tabel
        html.Thead(
            html.Tr([html.Th("No."), html.Th("Produk")])
        ),
        # Body tabel
        html.Tbody(
            [
                # Baris untuk setiap produk unik
                html.Tr([html.Td(i+1), html.Td(product)]) for i, product in enumerate(unique_products)
            ]
        )
    ],
    striped=True,
    bordered=True,
    hover=True,
    responsive=True,
    className="mt-1"
)

table_produk_ekspor_layout = dbc.Container([
    html.Div(className="mt-4"),
    dbc.Row([
        dbc.Col("Produk Yang Di Ekspor", width=12)
    ]),
    dbc.Row([
        dbc.Col(table_produk_ekspor, width=12)
    ])
])


