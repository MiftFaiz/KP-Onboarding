
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# from .visualisasi import available_provinces
from .analisis import unique_products
from .analisis import data_pnbp
from .analisis import unique_jenis_bb
from .analisis import unique_jenis_olahan
from .visualisasi import fig_peta
from .visualisasi import available_provinces
from .visualisasi import available_provinces_produksi
from .visualisasi import fig_3d
from .visualisasi import fig_treemap



card_style = {'width': '25rem', 'margin': '1rem'}
# List kolom yang dapat dipilih
available_columns = ['volume', 'pnbp_total', 'pnbp_DR', 'pnbp_PSDH', 'volume_bulat', 'volume_olahan']
# Daftar opsi px
available_plots = ['scatter', 'bar', 'box', 'line', 'area',  'density_contour']


layout_graph = html.Div([
    dbc.Container([
        html.Div(className="mt-4"),
        
        dbc.Row([
            dbc.Col(html.H1('PNBP Fraud Detection Dashboard', className='text-center mb-4'), width=12),
        ]),
        
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H1('Total Produksi per Tahun dan Provinsi')),
                    dbc.CardBody([
                        dcc.Dropdown(
                            id='dropdown-provinsi',
                            options=[{'label': plot.capitalize(), 'value': plot} for plot in available_provinces_produksi],
                        ),
                        dcc.Graph(id='grafik-produksi')
                    ])
                ], className="mx-auto", style={'width': '75%'})
            ], width=12),
        ], className='mb-4'),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H1('Boxplot Produksi per Tahun dan Provinsi')),
                    dbc.CardBody([
                        dcc.Dropdown(
                            id='dropdown-provinsi',
                            options=[{'label': plot.capitalize(), 'value': plot} for plot in available_provinces_produksi],
                        ),
                        dcc.Graph(id='box-produksi')
                    ])
                ], className="mx-auto", style={'width': '75%'})
            ], width=12),
        ], className='mb-4'),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H1('Total PNBP per Tahun dan Provinsi')),
                    dbc.CardBody([
                        dcc.Dropdown(
                            id='plot-dropdown-pnbp',
                            options=[{'label': plot.capitalize(), 'value': plot} for plot in available_plots],
                            value='bar'
                        ),
                        dcc.Graph(id='plot-graph-pnbp')
                    ])
                ], className="mx-auto", style={'width': '75%'})
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
                    dbc.CardHeader(html.H2('Grafik Treemap Wilayah Kawasan Hutan')),
                    dbc.CardBody([
                        dcc.Graph(figure=fig_treemap)
                    ])
                ], className="mx-auto", style={'width': '75%'})
            ], width=12),
        ], className='mb-4'),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H2('Daerah Yang Dicurigai')),
                    dbc.CardBody([
                        dcc.Graph(figure=fig_peta)
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

