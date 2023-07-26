
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
# from .visualisasi import available_provinces
from .analisis import unique_products
from .analisis import data_pnbp
from .analisis import unique_jenis_bb
from .analisis import unique_jenis_olahan
from .analisis import pnbp_kawasan_produksi
from .visualisasi import fig_peta
from .visualisasi import available_provinces_produksi
from .visualisasi import fig_3d
from .visualisasi import fig_treemap





card_style = {'width': '25rem', 'margin': '1rem'}
# List kolom yang dapat dipilih
available_columns = ['volume', 'pnbp_total', 'pnbp_DR', 'pnbp_PSDH', 'volume_bulat', 'volume_olahan']
# Daftar opsi px
available_plots = ['scatter', 'bar', 'box', 'line', 'area',  'density_contour']
provinsi = pnbp_kawasan_produksi['provinsi'].nunique()
volume = pnbp_kawasan_produksi['volume'].sum()
pnbp_total = pnbp_kawasan_produksi['pnbp_total'].sum()
volume_formatted = "{:,.0f} m²".format(volume)
pnbp_total_formatted = "${:,.0f} Bilion".format(pnbp_total / 1000000000)

layout_graph = html.Div([
    dbc.Container([
        html.Div(className="mt-4"),
                dbc.Row([
                    dbc.Col(html.H1('PNBP Fraud Detection Dashboard', className='text-center mb-4'), width=12),
                    html.Div(className="mt-4"),
                    html.Div(
            [
                html.Div(
                    [
                        html.Div([
                            html.P("Jumlah Provinsi:"),
                            html.H2("{}".format(provinsi), style={'font-family': 'Palatino Linotype, Book Antiqua, Palatino, serif', 'font-size': '24px', 'font-weight': 'bold', 'font-style': 'italic'}),
                        ], className="mt-4")
                    ],
                    className="col-3 bg-primary text-white text-center py-2",
                    style={'margin-right': '10px'}
                ),
                html.Div(
                    [
                        html.Div([
                            html.P("Volume Total Produksi:"),
                            html.H2("{}".format(volume_formatted), style={'font-family': 'Palatino Linotype, Book Antiqua, Palatino, serif', 'font-size': '24px', 'font-weight': 'bold', 'font-style': 'italic'}),                        ], className="mt-4")
                    ],
                    className="col-3 bg-secondary text-white text-center py-2",
                    style={'margin-right': '10px'}
                ),
                html.Div(
                    [
                        html.Div([
                            html.P("PNBP Total :"),
                            html.H2("{}".format(pnbp_total_formatted), style={'font-family': 'Palatino Linotype, Book Antiqua, Palatino, serif', 'font-size': '24px', 'font-weight': 'bold', 'font-style': 'italic'}),
                        ], className="mt-4")
                    ],
                    className="col-3 bg-info text-white text-center py-2"
                ),
            ],
            className="row mt-4 justify-content-center"
        )




        ]),

        html.Div(className="mt-4"),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H1('Total Produksi per Tahun dan Provinsi')),
                    dbc.CardBody([
                        dcc.Dropdown(
                            id='dropdown-provinsi',
                            options=[{'label': plot.capitalize(), 'value': plot} for plot in available_provinces_produksi],
                            value='Bali'
                        ),
                        dcc.Graph(id='grafik-produksi')
                        
                    ])
                ], className="mx-auto", style={'width': '100%'})
            ], width=12),
        ], className='mb-4'),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H1('Boxplot Produksi dan PNBP per Tahun dan Provinsi')),
                    dbc.CardBody([
                        dcc.Dropdown(
                            id='dropdown-provinsi-box',
                            options=[{'label': plot.capitalize(), 'value': plot} for plot in available_provinces_produksi],
                            value='Papua'
                        ),
                        dbc.Row(
                        [
                        dbc.Col(
                            dcc.Graph(
                                id='box-produksi',  
                            ),
                            width=6
                        ),
                        dbc.Col(
                            dcc.Graph(
                                id='box-pnbp',
                            ),
                            width=6
                        ),
                        ]),
                    ])
                ], className="mx-auto", style={'width': '100%'})
            ], width=12),
        ], className='mb-4'),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H1('Total PNBP per Provinsi')),
                    dbc.CardBody([
                        dcc.Dropdown(
                            id='plot-dropdown-pnbp',
                            options=[{'label': plot.capitalize(), 'value': plot} for plot in available_plots],
                            value='bar'
                        ),
                        dcc.Graph(id='plot-graph-pnbp')
                    ])
                ], className="mx-auto", style={'width': '100%'})
            ], width=12),
        ], className='mb-4'),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H2('Grafik Boxplot PNBP')),
                    dbc.CardBody([
                        dcc.Dropdown(
                            id='column-dropdown',
                            options=[{'label': col, 'value': col} for col in available_columns],
                            value=available_columns[0]
                        ),
                        dcc.Graph(id='pnbp-box-plot')
                    ])
                ], className="mx-auto", style={'width': '100%'})
            ], width=12),
        ], className='mb-4'),
        
        # dbc.Row([
        #     dbc.Col([
        #         dbc.Card([
        #             dbc.CardHeader(html.H2('Grafik 3D')),
        #             dbc.CardBody([
        #                 dcc.Graph(figure=fig_3d)
        #             ])
        #         ], className="mx-auto", style={'width': '100%'})
        #     ], width=12),
        # ], className='mb-4'),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H2('Grafik Treemap Wilayah Kawasan Hutan')),
                    dbc.CardBody([
                        dcc.Graph(figure=fig_treemap)
                    ])
                ], className="mx-auto", style={'width': '100%'})
            ], width=12),
        ], className='mb-4'),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H2('Daerah Yang Dicurigai')),
                    dbc.CardBody([
                        dcc.Graph(figure=fig_peta)
                    ])
                ], className="mx-auto", style={'width': '100%'})
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

