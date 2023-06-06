import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# Load Data
data_pnbp = pd.read_csv('Dataset/pnbp.csv')
data_hutan = pd.read_csv('Dataset/kawasan_hutan.csv')
data_ekspor = pd.read_csv('Dataset/ekspor.csv')
data_produksi_bulat = pd.read_csv('Dataset/produksi_kayu_bulat.csv')
data_produksi_olahan = pd.read_csv('Dataset/produksi_kayu_olahan.csv')
data_pemenuhan_bb = pd.read_csv('Dataset/pemenuhan_bahan_baku.csv')

# Define Thresholds
threshold_hutan = 100000  # Menentukan batas kawasan hutan yang dianggap besar
threshold_pnbp = 500000  # Menentukan batas PNBP yang dianggap kecil
threshold_produksi = 10000  # Menentukan batas produksi yang dianggap besar
threshold_ekspor = 1000  # Menentukan batas volume ekspor yang dianggap besar
threshold_value_ekspor = 1000000  # Menentukan batas value ekspor yang dianggap besar

# Analisis 1: Daerah dengan Kawasan Hutan Besar, namun PNBP Kecil
daerah_kawasan_hutan_besar_pnbp_kecil = data_hutan[data_hutan['area'] > threshold_hutan]['provinsi']
daerah_pnbp_kecil = data_pnbp[data_pnbp['pnbp'] < threshold_pnbp]['provinsi']
daerah_anomali_kawasan_hutan_pnbp = daerah_kawasan_hutan_besar_pnbp_kecil[daerah_kawasan_hutan_besar_pnbp_kecil.isin(daerah_pnbp_kecil)]

# Analisis 2: Pengusaha dengan PNBP Lebih Rendah
pengusaha_pnbp_rendah = data_pnbp[data_pnbp['pnbp'] < threshold_pnbp]['jenis'].unique()

# Analisis 3: Daerah dengan Produksi Besar namun PNBP Kecil
daerah_produksi_besar_pnbp_kecil = data_produksi_bulat[data_produksi_bulat['volume'] > threshold_produksi]['provinsi']
daerah_anomali_produksi_pnbp = daerah_produksi_besar_pnbp_kecil[daerah_produksi_besar_pnbp_kecil.isin(daerah_pnbp_kecil)]

# Analisis 4: Daerah dengan Volume dan Value Ekspor Besar namun PNBP Kecil
daerah_ekspor_besar_pnbp_kecil = data_ekspor[(data_ekspor['value usd'] > threshold_value_ekspor) & (data_ekspor['provinsi'].isin(daerah_pnbp_kecil))]['provinsi']
daerah_anomali_ekspor_pnbp = daerah_ekspor_besar_pnbp_kecil[daerah_ekspor_besar_pnbp_kecil.isin(daerah_pnbp_kecil)]

# Visualisasi 1: Perbandingan Kawasan Hutan dan PNBP
fig_kawasan_hutan_pnbp = px.scatter(data_hutan, x='area', y='provinsi', color='area',
                                   labels={'area': 'Kawasan Hutan (Ha)', 'provinsi': 'Provinsi'},
                                   title='Perbandingan Kawasan Hutan dan PNBP')

# Visualisasi 2: Perbandingan Produksi dan PNBP
fig_produksi_pnbp = px.line(data_produksi_bulat, x='tahun', y='volume', color='provinsi',
                            labels={'volume': 'Volume Produksi', 'provinsi': 'Provinsi', 'tahun': 'Tahun'},
                            title='Perbandingan Produksi dan PNBP')

# Visualisasi 3: Perbandingan Volume Ekspor dan PNBP
fig_ekspor_pnbp = px.bar(data_ekspor, x='provinsi', y='value usd',
                         labels={'value usd': 'Value Ekspor (USD)', 'provinsi': 'Provinsi'},
                         title='Perbandingan Volume Ekspor dan PNBP')



# Buat layout dashboard dengan Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Styling komponen menggunakan Bootstrap
card_style = {'width': '25rem', 'margin': '1rem'}

search_form = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search"), width=8),
        dbc.Col(
            dbc.Button("Search", color="success", className="ml-2", outline=True),
            width=2,
        ),
    ],
    className="ml-auto flex-nowrap mt-3 mt-md-0 align-items-center",  # Add custom CSS classes
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#")),
        dbc.NavItem(dbc.NavLink("Link", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Action", href="#"),
                dbc.DropdownMenuItem("Another action", href="#"),
                html.Div(className="dropdown-divider"),
                dbc.DropdownMenuItem("Something else here", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="Dropdown",
        ),
        dbc.NavItem(dbc.NavLink("Disabled", disabled=True)),
        dbc.NavItem(dbc.NavLink(search_form)),
    ],
    brand="Team 2 On Boarding",
    brand_href="#",
    color="primary",
    dark=True,
)

footer = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("About", href="#")),
                            ],
                            
                            navbar=True,
                        ),
                    ),
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Terms of Service", href="#")),
                            ],
                           
                            navbar=True,
                        ),
                    ),
                    dbc.Col(
                         dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Privacy Policy", href="#")),
                            ],
                            navbar=True,
                        ),
                    ),
                ],
                align="center",
            ),
             dbc.Row(
                    dbc.Col(html.P("© 2023 Your Company. All rights reserved.", className="text-muted")),
            )
        ]
    ),
    color="light",
    className="mt-8",
    dark=False,
    sticky="bottom",
)


app.layout = dbc.Container(
     style={
        "background-image": "url('/Data/bg.jpg')",
        "background-size": "cover",
        "background-position": "center",
        "height": "100vh",
    },

    children=[
    
    navbar,
    
    html.Div(className="mt-4"),
    dbc.Row([
        dbc.Col(html.H1('PNBP Fraud Detection Dashboard', className='text-center mb-4'), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H2('Analisis 1: Daerah dengan Kawasan Hutan Besar, namun PNBP Kecil')),
                dbc.CardBody([
                    html.P(f"Daerah dengan Kawasan Hutan Besar dan PNBP Kecil: {', '.join(daerah_anomali_kawasan_hutan_pnbp)}"),
                    dcc.Graph(figure=fig_kawasan_hutan_pnbp)
                ])
            ], className="mx-auto", style={'width': '75%'})
        ], width=12),

    ], className='mb-4'),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H2('Analisis 2: Pengusaha dengan PNBP Lebih Rendah')),
                dbc.CardBody([
                    html.P(f"Pengusaha dengan PNBP Lebih Rendah: {', '.join(pengusaha_pnbp_rendah)}"),
                    dcc.Graph(figure=fig_produksi_pnbp)
                ])
            ], className="mx-auto", style={'width': '75%'})
        ], width=12)
    ], className='mb-4'),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H2('Analisis 3: Daerah dengan Produksi Besar namun PNBP Kecil')),
                dbc.CardBody([
                    html.P(f"Daerah dengan Produksi Besar dan PNBP Kecil: "),
                    dcc.Graph(figure=fig_produksi_pnbp)
                ])
            ], className="mx-auto", style={'width': '75%'})
        ], width=12),
    ], className='mb-4'),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H2('Analisis 4: Daerah dengan Volume dan Value Ekspor Besar namun PNBP Kecil')),
                dbc.CardBody([
                    html.P(f"Daerah dengan Volume dan Value Ekspor Besar dan PNBP Kecil: "),
                    dcc.Graph(figure=fig_ekspor_pnbp)
                ])
            ], className="mx-auto", style={'width': '75%'})
        ], width=12)
    ]),

    footer,

],
fluid=True)

if __name__ == "__main__":
    try:
        app.run_server(debug=True)
    except Exception as e:
        print(f"Error: {e}")
