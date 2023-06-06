import pandas as pd

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
sum_olahan = data_produksi_olahan.groupby(['tahun', 'bulan', 'provinsi'], sort=False).sum().reset_index()
sum_bulat = data_produksi_bulat.drop("kelompok", axis=1).groupby(["tahun", "bulan", "provinsi"], sort=False)["volume"].sum().reset_index()

# Membenarkan nama provinsi
sum_olahan['provinsi'] = sum_olahan['provinsi'].replace(["Nangroe Aceh\xa0Darussalam"], 'Nangroe Aceh Darussalam')

# Menyatukan Data Produksi dengan Outer Join
produksi = pd.merge(sum_olahan, sum_bulat, how='outer', on=['provinsi', 'bulan', 'tahun'])
produksi = produksi.rename(columns={'volume_x':'volume_olahan','volume_y':'volume_bulat'})
produksi = produksi.fillna(0)
produksi['volume'] = produksi['volume_olahan'] + produksi['volume_bulat']

pnbp = data_pnbp.copy()
pnbp["provinsi"] = pnbp["provinsi"].replace(["Kalimantan Timur"], "Kalimantan Timur dan Utara")
pnbp["provinsi"] = pnbp["provinsi"].replace(["Kalimantan Utara"], "Kalimantan Timur dan Utara")
# pnbp = pnbp.drop("jenis", axis=1)
new_pnbp = pnbp.groupby(["tahun", "bulan", "provinsi"], sort=False)["pnbp"].sum().reset_index()

# Buat PNBP yang jenisnya berkaitan dengan produksi
pnbp_produksi = pnbp.loc[(pnbp['jenis'] == 'IURAN') | (pnbp['jenis'] == 'DR')]
pnbp_produksi['jenis'].unique()

data_kawasan['provinsi'] = data_kawasan['provinsi'].replace(['Aceh'], 'Nangroe Aceh Darussalam')
data_kawasan['provinsi'] = data_kawasan['provinsi'].replace(['Kepulauan Bangka Belitung'], 'Bangka Belitung')
kawasan = data_kawasan.copy()

provinsi_pnbp = pnbp['provinsi'].unique()
provinsi_kawasan = data_kawasan['provinsi'].unique()

[x for x in provinsi_kawasan if x not in provinsi_pnbp]

kawasan = kawasan.groupby(['provinsi'], sort=False).sum().reset_index()

kawasan_pnbp = pd.merge(new_pnbp, kawasan, how='left', on=['provinsi'])
kawasan_pnbp.fillna(0, inplace=True)

