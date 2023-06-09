import plotly.graph_objects as go
import pandas as pd
import dash_core_components as dcc
import numpy as np
import plotly.express as px
import plotly.io as pio
from .analisis import kawasan_pnbp 
from .analisis import produksi 
from .analisis import kawasan 
from .analisis import pnbp_kawasan_produksi 
from .analisis import data_clusters 
from .analisis import pnbp_tahunan 
import plotly.graph_objects as go
from plotly.subplots import make_subplots



available_provinces = kawasan_pnbp['provinsi'].unique().tolist()
available_provinces_produksi = produksi['provinsi'].unique().tolist()
def generate_figure_pnbp(provinsi):
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

def generate_figure_produksi(provinsi):
    fig_kawasan_produksi = go.Figure()
    for i in range(2018, 2023):
        tes = produksi.loc[(produksi['provinsi'] == provinsi) & (produksi['tahun'] == i)]
        if not tes.empty:
            fig_kawasan_produksi.add_trace(go.Bar(x=tes['bulan'], y=tes['volume'], name=f'Produksi Tahun {i}'))
    fig_kawasan_produksi.update_layout(
        title=f"Grafik Produksi - Provinsi {provinsi}",
        xaxis_title="Bulan",
        yaxis_title="Produksi"
    )
    return fig_kawasan_produksi

def generate_boxplot_produksi(provinsi):
    filtered_data = produksi[produksi['provinsi'] == provinsi]
    fig_box_produksi = go.Figure()
    fig_box_produksi.add_trace(go.Box(
        x=filtered_data['tahun'],
        y=filtered_data['volume'],
        name='Produksi',
        boxpoints='all',
        marker=dict(color='blue'),
        jitter=0.3,
        pointpos=-1.8
    ))
    fig_box_produksi.update_layout(
        title=f'Boxplot Produksi - Provinsi {provinsi}',
        xaxis_title='Tahun',
        yaxis_title='Volume Produksi'
    )
    return fig_box_produksi


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
    showscale=False  # Menghilangkan bar warna di sebelah kanan
))


fig_peta.update_layout(
    title_text='Jumlah dalam setiap provinsi di Indonesia',
    geo=dict(
        showframe=False,  # Menyembunyikan bingkai peta
        showcoastlines=False,  # Menyembunyikan garis pantai
        projection_type='natural earth',  # Tipe proyeksi peta 
        scope='asia'  
    ),
    width=800,  # Lebar peta dalam piksel
    height=600,  # Tinggi peta dalam piksel
    margin=dict(l=0, r=0, t=0, b=0)  # Mengatur margin ke nol untuk mengisi seluruh area yang tersedia
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


# # Ambil contoh data volume PNBP area
# volume_pnbp_area = np.random.randn(100)
# cluster_labels = np.random.randint(0, 4, size=100)


# # Definisikan warna untuk setiap cluster
# colors = ['red', 'green', 'blue', 'yellow']

# # Buat 3D scatter plot
# fig_3d = go.Figure()

# # Tambahkan data scatter plot untuk setiap cluster
# for cluster, data in enumerate(pnbp_kawasan_produksi):
#     fig_3d.add_trace(go.Scatter3d(
#         x=data['volume'],
#         y=data['pnbp'],
#         z=data['area'],

#         mode='markers',
#         marker=dict(
#             size=8,
#             color=colors[cluster],
#             opacity=0.8
#         ),
#         name='Cluster {}'.format(cluster)
#     ))

# # Set layout
# fig_3d.update_layout(
#     scene=dict(
#         xaxis=dict(title='Volume'),
#         yaxis=dict(title='PNBP'),
#         zaxis=dict(title='Area'),
#     ),
#     title='3D Scatter Plot'
# )

# Group data by tahun, provinsi, and calculate total pnbp
kde_data_pnbp = pnbp_tahunan.groupby(['tahun', 'provinsi'], sort=False)['pnbp'].sum().reset_index()

# Create kde figure using scatter plot
fig_kde_pnbp = px.density_contour(kde_data_pnbp, x='tahun', y='pnbp', color='provinsi', title='Total PNBP per Tahun dan Provinsi')

# Update figure layout
fig_kde_pnbp.update_layout(xaxis_title='Tahun', yaxis_title='Total PNBP')

# Filter kolom yang ingin ditampilkan
filtered_columns = ['volume', 'pnbp_total', 'pnbp_DR', 'pnbp_PSDH', 'volume_bulat', 'volume_olahan']

# Membuat list objek Box untuk setiap kolom yang difilter
box_plots = []
for column in filtered_columns:
    box_plot = go.Box(
        x=pnbp_kawasan_produksi['provinsi'],
        y=pnbp_kawasan_produksi[column],
        name=column
    )
    box_plots.append(box_plot)

# Membuat layout dan menampilkan box plot
fig_pnbp_box = go.Layout(
    height=600,
    width=800,
    title="Visualisasi PNBP terhadap Produksi"
)

# Membuat treemap menggunakan Plotly
fig_treemap = px.treemap(kawasan, path=['provinsi'], values='area')

# Update layout
fig_treemap.update_layout(
    title='Treemap - Kawasan',
    height=600,
    width=800
)

data_terpilih = pnbp_kawasan_produksi[pnbp_kawasan_produksi['tahun'] == 2023]

fig_box_area = px.box(data_terpilih, x="cluster", y="area", color="cluster",
             title=f"Boxplot Area")

fig_box_area.update_layout(height=600, width=800)


