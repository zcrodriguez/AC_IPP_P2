import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY], use_pages=True)
server = app.server

app.layout = html.Div([

    # Barra de navegación
    dbc.Navbar(
        dbc.Container([
            html.A(
                dbc.Row([
                    dbc.Col(html.Img(src="./assets/logo-deca.png", height="40px"), width="auto"),
                    dbc.Col(dbc.NavbarBrand("IPP - Ferramenta de predição de sucesso académico")),
                ], align="center"),
            ),
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("🏠 Home", href="/")),
                    dbc.NavItem(dbc.NavLink("🚧 Page 1", href="/visualizations")),
                ],
                className="ml-auto",
            ),
        ]),
        color="dark", dark=True,
    ),

    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)