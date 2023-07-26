
import dash_bootstrap_components as dbc
from dash import html
from .analisis import pnbp_kawasan_produksi 


layout = html.Div(
    [
        dbc.Container(
            [
                html.H1("PNBP FRAUD DETECTION", className="text-center mt-5 mb-4"),
                html.H3("DATA YANG DIGUNAKAN:", className="mb-3"),
                html.P("1. Data PNBP"),
                html.P("2. Data kawasan hutan"),
                html.P("3. Data ekspor"),
                html.P("4. Data produksi"),
                
                html.H3("Alasan Mengambil Kasus PNBP Fraud Detection:", className="mt-5 mb-3"),
                html.P(
                    "Kami memilih untuk mengambil kasus PNBP Fraud Detection dengan data PNBP, data kawasan hutan, "
                    "data ekspor, dan data produksi karena mengidentifikasi potensi kejanggalan atau penyalahgunaan "
                    "dalam pengumpulan PNBP cukup menarik dan juga objektif case yang lebih jelas."
                ),
                
              
            ],
            className="mt-4",
        ),

        dbc.Card(
            dbc.Container(
                [
                    html.H3("Apa Itu PNBP?", className="mb-3"),
                    html.P(
                        "PNBP (Penerimaan Negara Bukan Pajak) merupakan sumber pendapatan negara yang berasal dari berbagai "
                        "penerimaan selain pajak. Penerimaan ini diperoleh dari kegiatan atau layanan yang dilakukan oleh "
                        "instansi pemerintah atau lembaga negara kepada masyarakat atau pihak ketiga, yang dikenakan "
                        "biaya atau pungutan tertentu."
                    ),
                    html.H3("Penerimaan PNBP yang Diambil untuk Analisis:", className="mt-5 mb-3"),
                    html.P("1. PSDH (Penerimaan Sumber Daya Hutan)"),
                    html.P("2. Dana Reboisasi"),
                    html.P("3. Dana Iuran"),
                    html.P("4. DPEH (Dana Pengelolaan Ekosistem Hutan)"),
                ],
                className="mt-4",
            ),
        ),

        dbc.Card(
            dbc.Container(
                [
                    html.H3("Jenis-jenis Area:", className="mb-3"),
                    html.P("1. Hutan Produksi"),
                    html.P("2. UPHHK HTR (Usaha Pemanfaatan Hutan Tanaman Rakyat)"),
                    html.P("3. HKM HD Kemitraan (Hutan Kemasyarakatan Hutan Desa Kemitraan)"),
                    html.P("4. IUPHHK RE (Izin Usaha Pemanfaatan Hasil Hutan Kayu Reboisasi Ekonomi)"),
                    html.P("5. IUPHHK HTI (Izin Usaha Pemanfaatan Hasil Hutan Kayu Hutan Tanaman Industri)"),
                    html.P("6. IUPHHK HA (Izin Usaha Pemanfaatan Hasil Hutan Kayu Hutan Alam)"),
                    html.P("7. Hutan Lindung"),
                    html.P("8. HKM HD HTR (Hutan Kemasyarakatan Hutan Desa Hutan Tanaman Rakyat)"),
                ],
                className="mt-4",
            ),
        ),

        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.Container(
                            [
                                html.H3("Cluster 0:", className="mb-3"),
                                html.P("Jumlah PNBP Tinggi"),
                                html.P("Jumlah Produksi Normal"),
                                html.P("Luas area Sedang"),
                            ],
                            className="mt-4",
                        ),
                    ),
                    width=6,
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.Container(
                            [
                                html.H3("Cluster 1:", className="mb-3"),
                                html.P("Jumlah PNBP relatif Normal"),
                                html.P("Jumlah Produksi Normal"),
                                html.P("Luas area kecil"),
                            ],
                            className="mt-4",
                        ),
                    ),
                    width=6,
                ),
            ],
            className="mb-4",
        ),

        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.Container(
                            [
                                html.H3("Cluster 2:", className="mb-3"),
                                html.P("Jumlah PNBP relatif sedikit"),
                                html.P("Jumlah Produksi Sedikit"),
                                html.P("Luas area cukup besar"),
                            ],
                            className="mt-4",
                        ),
                    ),
                    width=6,
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.Container(
                            [
                                html.H3("Cluster 3:", className="mb-3"),
                                html.P("Jumlah PNBP relatif Tinggi"),
                                html.P("Jumlah Produksi Sangat Tinggi"),
                                html.P("Luas area sangat kecil"),
                            ],
                            className="mt-4",
                        ),
                    ),
                    width=6,
                ),
            ],
            className="mb-4",
        ),

        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.Container(
                            [
                                html.H3("Cluster 4:", className="mb-3"),
                                html.P("Jumlah PNBP relatif Tinggi"),
                                html.P("Jumlah Produksi relatif Normal"),
                                html.P("Luas area sangat besar"),
                            ],
                            className="mt-4",
                        ),
                    ),
                    width=6,
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.Container(
                            [
                                html.H3("Cluster 5:", className="mb-3"),
                                html.P("Jumlah PNBP sedikit"),
                                html.P("Jumlah Produksi Sedikit"),
                                html.P("Luas area kecil"),
                            ],
                            className="mt-4",
                        ),
                    ),
                    width=6,
                ),
            ],
            className="mb-4",
        )


        
        




    ]
)