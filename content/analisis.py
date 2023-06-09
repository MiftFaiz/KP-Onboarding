import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler



# Load Data
data_pnbp = pd.read_csv('Dataset/pnbp.csv')
data_kawasan = pd.read_csv('Dataset/kawasan_hutan.csv')
data_ekspor = pd.read_csv('Dataset/ekspor.csv')
data_produksi_bulat = pd.read_csv('Dataset/produksi_kayu_bulat.csv')
data_produksi_olahan = pd.read_csv('Dataset/produksi_kayu_olahan.csv')
data_pemenuhan_bb = pd.read_csv('Dataset/pemenuhan_bahan_baku.csv')

# Ubah format nama Provinsi menyesuaikan data pnbp
data_produksi_olahan["provinsi"] = data_produksi_olahan["provinsi"].replace(["Daerah Istimewa Yogyakarta"], "D.I. Yogyakarta")
data_produksi_olahan["provinsi"] = data_produksi_olahan["provinsi"].replace(["Aceh"], "Nangroe Aceh Darussalam")

# Menghilangkan jenis dan sum volumenya lalu grupkan berdasarkan tahun bulan dan provinsi
sum_olahan = data_produksi_olahan.groupby(['tahun', 'bulan', 'provinsi'], sort=False)["volume"].sum().reset_index()
sum_bulat = data_produksi_bulat.drop("kelompok", axis=1).groupby(["tahun", "bulan", "provinsi"], sort=False)["volume"].sum().reset_index()

# Membenarkan nama provinsi
sum_olahan['provinsi'] = sum_olahan['provinsi'].replace(["Nangroe Aceh\xa0Darussalam"], 'Nangroe Aceh Darussalam')

# Menyatukan Data Produksi dengan Outer Join
produksi = pd.merge(sum_olahan, sum_bulat, how='outer', on=['provinsi', 'bulan', 'tahun'])
produksi = produksi.rename(columns={'volume_x':'volume_olahan','volume_y':'volume_bulat'})
produksi = produksi.fillna(0)
produksi['volume'] = produksi['volume_olahan'] + produksi['volume_bulat']
# print(produksi)

pnbp = data_pnbp.copy()
pnbp["provinsi"] = pnbp["provinsi"].replace(["Kalimantan Timur"], "Kalimantan Timur dan Utara")
pnbp["provinsi"] = pnbp["provinsi"].replace(["Kalimantan Utara"], "Kalimantan Timur dan Utara")
# pnbp = pnbp.drop("jenis", axis=1)
new_pnbp = pnbp.groupby(["tahun", "bulan", "provinsi"], sort=False)["pnbp"].sum().reset_index()

# Buat PNBP yang jenisnya berkaitan dengan produksi
# pnbp_produksi = pnbp.loc[(pnbp['jenis'] == 'IURAN') | (pnbp['jenis'] == 'DR')]
pnbp_produksi = pnbp.copy()
pnbp_produksi['jenis'].unique()

data_kawasan['provinsi'] = data_kawasan['provinsi'].replace(['Aceh'], 'Nangroe Aceh Darussalam')
data_kawasan['provinsi'] = data_kawasan['provinsi'].replace(['Kepulauan Bangka Belitung'], 'Bangka Belitung')
kawasan = data_kawasan.copy()

provinsi_pnbp = pnbp['provinsi'].unique()
provinsi_kawasan = data_kawasan['provinsi'].unique()

[x for x in provinsi_kawasan if x not in provinsi_pnbp]

kawasan = kawasan.groupby(['provinsi'], sort=False)['area'].sum().reset_index()

kawasan_pnbp = pd.merge(new_pnbp, kawasan, how='left', on=['provinsi'])
kawasan_pnbp.fillna(0, inplace=True)

print(produksi.columns)

unique_products = data_ekspor['produk'].unique()

unique_jenis_bb = data_pemenuhan_bb['jenis'].unique()

unique_jenis_olahan = data_produksi_olahan['jenis'].unique()

available_provinces = kawasan_pnbp['provinsi'].unique().tolist()



data_pnbp["provinsi"] = data_pnbp["provinsi"].replace(["Kalimantan Timur"], "Kalimantan Timur dan Utara")
data_pnbp["provinsi"] = data_pnbp["provinsi"].replace(["Kalimantan Utara"], "Kalimantan Timur dan Utara")
new_pnbp = data_pnbp.groupby(["tahun", "bulan", "provinsi", "jenis"], sort=False)["pnbp"].sum().reset_index()
new_pnbp = new_pnbp.drop(new_pnbp[(new_pnbp['tahun'] == 2023) & (new_pnbp['bulan'].isin(['Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']))].index)
pnbp_tahunan = new_pnbp.groupby(['tahun', 'provinsi'], sort=False)['pnbp'].sum().reset_index()

# One Hot Encoding Data PNBP buat produksi
enc_pnbp_p = OneHotEncoder(sparse_output=False).fit(pnbp_produksi.drop(columns=['tahun','bulan', 'provinsi','pnbp']))
encoded_pnbp_p = enc_pnbp_p.transform(pnbp_produksi.drop(columns=['tahun','pnbp','bulan', 'provinsi']))

encoded_df = pd.DataFrame(
    encoded_pnbp_p,
    columns=enc_pnbp_p.get_feature_names_out()
    )
pnbp_produksi = pd.concat([pnbp_produksi.drop(columns=['jenis']), encoded_df], axis=1)


pnbp_produksi['pnbp_IURAN'] = pnbp_produksi['pnbp'].loc[pnbp_produksi['jenis_IURAN'] == 1.0]
pnbp_produksi['pnbp_DR'] = pnbp_produksi['pnbp'].loc[pnbp_produksi['jenis_DR'] == 1.0]
pnbp_produksi['pnbp_PSDH'] = pnbp_produksi['pnbp'].loc[pnbp_produksi['jenis_PSDH'] == 1.0]
pnbp_produksi['pnbp_DPEH'] = pnbp_produksi['pnbp'].loc[pnbp_produksi['jenis_DPEH'] == 1.0]
pnbp_produksi.fillna(0,inplace=True)
pnbp_produksi.drop(columns=['pnbp'], inplace=True)
pnbp_produksi = pnbp_produksi.groupby(['provinsi', 'tahun', 'bulan'], sort=False).sum().reset_index()


pnbp_produksi['pnbp_total'] = pnbp_produksi['pnbp_IURAN'] + pnbp_produksi['pnbp_DR'] + pnbp_produksi['pnbp_PSDH'] +pnbp_produksi['pnbp_DPEH']
pnbp_produksi.loc[
    (pnbp_produksi['jenis_DPEH'] > 1 )|
    (pnbp_produksi['jenis_DR'] > 1 )|
    (pnbp_produksi['jenis_IURAN'] > 1 )|
    (pnbp_produksi['jenis_DPEH'] > 1 )|
    (pnbp_produksi['jenis_PSDH'] > 1 ),["jenis_DR", "jenis_IURAN","jenis_DPEH","jenis_PSDH"]] = 1.0

pnbp_p = pd.merge(pnbp_produksi, produksi, how='left',on=['tahun', 'bulan', 'provinsi'])
pnbp_p.fillna(0, inplace=True)
# selisih = pnbp_p['pnbp_total'] - pnbp_p['volume_total']


pnbp_kawasan_produksi = pd.merge(pnbp_p, kawasan, how='left', on=['provinsi']).fillna(0)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(pnbp_kawasan_produksi.drop(columns=['provinsi','bulan', 'tahun', 'jenis_DPEH', 'jenis_IURAN', 'jenis_PSDH', 'jenis_DR']))

scaled_data = pd.DataFrame(
    scaled_data,
    columns=scaler.get_feature_names_out()
    )

scaled_pnbp_KP = pd.concat([pnbp_kawasan_produksi.drop(columns=scaled_data.columns), scaled_data],axis=1)


