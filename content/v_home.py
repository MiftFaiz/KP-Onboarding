
import dash_bootstrap_components as dbc
from dash import html

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
    ]
)