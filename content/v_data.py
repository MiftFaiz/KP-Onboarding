
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from .visualisasi import available_provinces


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


