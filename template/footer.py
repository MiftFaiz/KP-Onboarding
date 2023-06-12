import dash_bootstrap_components as dbc
from dash import html
import dash


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
footer = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        html.Img(src=app.get_asset_url('logo.png'), height="50px", style={'vertical-align': 'middle'}),
                        width="auto",
                    ),
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("About", href="#")),
                            ],
                            className="ml-auto",
                            navbar=True,
                        ),
                    ),
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Contact", href="#")),
                            ],
                            className="ml-auto",
                            navbar=True,
                        ),
                    ),
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Comment", href="#")),
                            ],
                            className="ml-auto",
                            navbar=True,
                        ),
                    ),
                ],
                align="center",
            ),
            dbc.Row(
                dbc.Col(
                    html.P("© 2023 Ganesha79. All rights reserved. | GG TERASANA NO 6A, Bandung, Jawa Barat", className="text-muted", style={'white-space': 'nowrap'}),
                    width="auto",
                ),
            ),
        ],
        
    ),
    color="light",
    className="fixed-bottom",
    dark=False,
)