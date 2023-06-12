import dash_bootstrap_components as dbc
from dash import html

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
        dbc.NavItem(dbc.NavLink("Home", href="home")),
        dbc.NavItem(dbc.NavLink("Data", href="data")),
        dbc.NavItem(dbc.NavLink("Table", href="table")),
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