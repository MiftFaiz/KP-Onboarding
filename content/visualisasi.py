import plotly.graph_objects as go
from .analisis import kawasan_pnbp 

available_provinces = kawasan_pnbp['provinsi'].unique().tolist()
def generate_figure(provinsi):
    fig = go.Figure()
    for i in range(2018, 2023):
        tes = kawasan_pnbp.loc[(kawasan_pnbp['provinsi'] == provinsi) & (kawasan_pnbp['tahun'] == i)]
        area = tes.iloc[0]['area']
        fig.add_trace(go.Bar(x=tes['bulan'], y=tes['pnbp'], name=f'PNBP Tahun {i} Area: {area}'))
    fig.update_layout(
        title=f"Grafik PNBP - Provinsi {provinsi}",
        xaxis_title="Bulan",
        yaxis_title="PNBP"
    )
    return fig

