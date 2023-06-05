import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# Load Data
data_pnbp = pd.read_csv('Data/pnbp.csv')
data_hutan = pd.read_csv('Data/kawasan_hutan.csv')
data_ekspor = pd.read_csv('Data/ekspor.csv')
data_produksi_bulat = pd.read_csv('Data/produksi_kayu_bulat.csv')
data_produksi_olahan = pd.read_csv('Data/produksi_kayu_olahan.csv')

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

app.layout = dbc.Container([
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
            ], style=card_style)
        ], width=6),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H2('Analisis 2: Pengusaha dengan PNBP Lebih Rendah')),
                dbc.CardBody([
                    html.P(f"Pengusaha dengan PNBP Lebih Rendah: {', '.join(pengusaha_pnbp_rendah)}")
                ])
            ], style=card_style)
        ], width=6)
    ], className='mb-4'),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H2('Analisis 3: Daerah dengan Produksi Besar namun PNBP Kecil')),
                dbc.CardBody([
                    html.P(f"Daerah dengan Produksi Besar dan PNBP Kecil: {', '.join(daerah_anomali_produksi_pnbp)}"),
                    dcc.Graph(figure=fig_produksi_pnbp)
                ])
            ], style=card_style)
        ], width=6),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H2('Analisis 4: Daerah dengan Volume dan Value Ekspor Besar namun PNBP Kecil')),
                dbc.CardBody([
                    html.P(f"Daerah dengan Volume dan Value Ekspor Besar dan PNBP Kecil: {', '.join(daerah_anomali_ekspor_pnbp)}"),
                    dcc.Graph(figure=fig_ekspor_pnbp)
                ])
            ], style=card_style)
        ], width=6)
    ])
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
