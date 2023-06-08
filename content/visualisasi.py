import plotly.graph_objects as go
import pandas as pd
import dash_core_components as dcc
import numpy as np
import plotly.express as px
import plotly.io as pio
import dash_html_components as html
from .analisis import kawasan_pnbp 
from .analisis import pnbp_tahunan 
from .analisis import scaled_pnbp_KP 


available_provinces = kawasan_pnbp['provinsi'].unique().tolist()
def generate_figure(provinsi):
    fig_kawasan_pnbp = go.Figure()
    for i in range(2018, 2023):
        tes = kawasan_pnbp.loc[(kawasan_pnbp['provinsi'] == provinsi) & (kawasan_pnbp['tahun'] == i)]
        if not tes.empty:
            area = tes.iloc[0]['area']
            fig_kawasan_pnbp.add_trace(go.Bar(x=tes['bulan'], y=tes['pnbp'], name=f'PNBP Tahun {i} Area: {area}'))
    fig_kawasan_pnbp.update_layout(
        title=f"Grafik PNBP - Provinsi {provinsi}",
        xaxis_title="Bulan",
        yaxis_title="PNBP"
    )
    return fig_kawasan_pnbp

data_peta = [
    {'provinsi_peta': 'Aceh', 'jumlah': 100},
    {'provinsi_peta': 'Sumatera Utara', 'jumlah': 200},
    {'provinsi_peta': 'Sumatera Barat', 'jumlah': 150},
    # ... tambahkan data_peta untuk wilayah lainnya ...
]

# Membuat dataframe dari list data_peta
df_peta = pd.DataFrame(data_peta)

# Membuat objek peta
fig_peta = go.Figure(data=go.Choropleth(
    locations=df_peta['provinsi_peta'],  # Nama provinsi
    z=df_peta['jumlah'],  # Jumlah pada setiap provinsi
    locationmode='country names',  # Mode lokasi dengan nama provinsi
    colorscale='Blues',  # Skala warna
    autocolorscale=False,  # Menonaktifkan otomatisasi skala warna
    marker_line_color='white',  # Warna garis batas wilayah
    colorbar_title='Jumlah',  # Judul colorbar
))

fig_peta.update_layout(
    title_text='Jumlah dalam setiap provinsi di Indonesia',
    geo=dict(
        showframe=False,  # Menyembunyikan bingkai peta
        showcoastlines=False,  # Menyembunyikan garis pantai
        projection_type='natural earth',  # Tipe proyeksi peta
        center=dict(lat=-8, lon=135),  # Koordinat pusat peta 
        scope='asia'  # Level zoom untuk tampilan Indonesia
    ),
    width=800,  # Lebar peta dalam piksel
    height=600  # Tinggi peta dalam piksel
)

# Menambahkan scattergeo trace untuk tanda lingkaran merah
fig_peta.add_trace(go.Scattergeo(
    lon=[117, 111, 103.7],  # Koordinat longitude untuk lokasi yang ingin ditandai
    lat=[2, -2, -2.7],  # Koordinat latitude untuk lokasi yang ingin ditandai
    mode='markers',
    marker=dict(
        size=15,
        color='red',
        symbol='circle'
    ),
    name='Lokasi Tertentu'
))

np.random.seed(0)
n = 100
x = np.random.randn(n)
y = np.random.randn(n)
z = np.random.randn(n)

# Create 3D scatter plot
fig_3d = go.Figure(data=go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=8,
        color=z,
        colorscale='Viridis',
        opacity=0.8
    )
))

# Set layout
fig_3d.update_layout(
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z'),
    ),
    title='3D Scatter Plot'
)

# Group data by tahun, provinsi, and calculate total pnbp
ked_data_pnbp = pnbp_tahunan.groupby(['tahun', 'provinsi'], sort=False)['pnbp'].sum().reset_index()

# Create KED figure using scatter plot
fig_ked_pnbp = px.scatter(ked_data_pnbp, x='tahun', y='pnbp', color='provinsi', title='KED - Total PNBP per Tahun dan Provinsi')

# Update figure layout
fig_ked_pnbp.update_layout(xaxis_title='Tahun', yaxis_title='Total PNBP')

pio.templates.default = "plotly_dark"

# Buat dropdown options
dropdown_options_Jenis = [
    {'label': 'Volume Total', 'value': 'volume_total'},
    {'label': 'Volume Olahan', 'value': 'volume_olahan'},
    {'label': 'Volume Bulat', 'value': 'volume_bulat'},
    {'label': 'PNBP PSDH', 'value': 'pnbp_PSDH'},
    {'label': 'PNBP DR', 'value': 'pnbp_DR'},
    {'label': 'PNBP Total', 'value': 'pnbp_total'}
]

# Fungsi untuk menggambar boxplot
def draw_boxplot(selected_x):
    fig = go.Figure()

    fig.add_trace(go.Box(
        x=scaled_pnbp_KP[selected_x],
        y=scaled_pnbp_KP['provinsi'],
        name=selected_x,
        orientation='h'
    ))

    fig.update_layout(
        title="Boxplot",
        yaxis=dict(title="Provinsi"),
        xaxis=dict(title=selected_x),
        height=600,
        margin=dict(l=20, r=20, t=40, b=20),
        template="plotly_dark"
    )

# Buat dropdown menu
dropdown = dcc.Dropdown(
    id='x-dropdown',
    options=dropdown_options_Jenis,
    value='volume_total'
)

# Buat boxplot
boxplot = dcc.Graph(
    id='boxplot'
)

boxplot_layout_pnbp = html.Div([
    html.H1("Boxplot PNBP"),
    html.Label("Pilih x:"),
    dropdown,
    boxplot
])