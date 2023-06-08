
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# from .visualisasi import available_provinces
from .analisis import unique_products
from .analisis import data_pnbp
from .analisis import unique_jenis_bb
from .analisis import unique_jenis_olahan
from .visualisasi import fig_peta
from .visualisasi import fig_3d
from .visualisasi import fig_ked_pnbp
from .visualisasi import boxplot_layout_pnbp

card_style = {'width': '25rem', 'margin': '1rem'}

layout_graph = html.Div([
    dbc.Container([
        
        html.Div(className="mt-4"),
        dbc.Row([
            dbc.Col(html.H1('PNBP Fraud Detection Dashboard', className='text-center mb-4'), width=12)
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H1('KED - Total PNBP per Tahun dan Provinsi')),
                    dbc.CardBody([
                        dcc.Graph(id='graph-ked', figure=fig_ked_pnbp)
                        
                    ])
                ], className="mx-auto", style={'width': '75%'})
            ], width=12),
        ], className='mb-4'),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H2('Grafik Peta')),
                    dbc.CardBody([
                        dcc.Graph(figure=fig_peta)
                    ])
                ], className="mx-auto", style={'width': '75%'})
            ], width=12),
        ], className='mb-4'),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H2('Grafik 3D')),
                    dbc.CardBody([
                        dcc.Graph(figure=fig_3d)
                    ])
                ], className="mx-auto", style={'width': '75%'})
            ], width=12),
        ], className='mb-4'),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H2('Grafik 3D')),
                    dbc.CardBody([
                        dcc.Graph(figure=boxplot_layout_pnbp)
                    ])
                ], className="mx-auto", style={'width': '75%'})
            ], width=12),
        ], className='mb-4'),
    ])
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
        dbc.Col("Data Produk Yang Di Ekspor", width=12)
    ]),
    dbc.Row([
        dbc.Col(table_produk_ekspor, width=12)
    ])
])



table_pemenuhan_bb = dbc.Table(
    [
        # Header tabel
        html.Thead(
            html.Tr([html.Th("No."), html.Th("Jenis")])
        ),
        # Body tabel
        html.Tbody(
            [
                # Baris untuk setiap jenis unik
                html.Tr([html.Td(i+1), html.Td(jenis)]) for i, jenis in enumerate(unique_jenis_bb)
            ]
        )
    ],
    striped=True,
    bordered=True,
    hover=True,
    responsive=True,
    className="mt-1"
)

table_pemenuhan_bb_layout = dbc.Container([
    html.Div(className="mt-4"),
    dbc.Row([
        dbc.Col(("Data Pemenuhan Bahan Baku"), width=12)
    ]),
    dbc.Row([
        dbc.Col(table_pemenuhan_bb, width=12)
    ])
])


table_produksi_olahan = dbc.Table(
    [
        # Header tabel
        html.Thead(
            html.Tr([html.Th("No."), html.Th("Jenis")])
        ),
        # Body tabel
        html.Tbody(
            [
                # Baris untuk setiap jenis unik
                html.Tr([html.Td(i+1), html.Td(jenis)]) for i, jenis in enumerate(unique_jenis_olahan)
            ]
        )
    ],
    striped=True,
    bordered=True,
    hover=True,
    responsive=True,
    className="mt-1"
)

table_produksi_olahan_layout = dbc.Container([
    html.Div(className="mt-4"),
    dbc.Row([
        dbc.Col(("Data Produksi Olahan"), width=12)
    ]),
    dbc.Row([
        dbc.Col(table_produksi_olahan, width=12)
    ])
])

table_pnbp_layout = html.Div([
    dcc.Dropdown(
        id='dropdown-tahun',
        options=[{'label': str(tahun), 'value': tahun} for tahun in data_pnbp['tahun'].unique()],
        value=data_pnbp['tahun'].unique()[0]
    ),
    html.Div(id='table-container')
])

