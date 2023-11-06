import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MINTY, '/assets/custom.css', dbc.icons.FONT_AWESOME], use_pages=True)
server = app.server

# ======================================================================================================================
#                                               LAYOUT PRINCIPAL
# ======================================================================================================================
app.layout = html.Div([

    # Barra de navegación
    dbc.Navbar(
        dbc.Container([

            # Logo y título
            html.A(
                dbc.Row([
                    dbc.Col(html.Img(src="./assets/logo-deca.png", height="40px"), width="auto"),
                    dbc.Col(dbc.NavbarBrand("IPP - Ferramenta de predição de sucesso académico")),
                ], align="center"),
            ),

            # Links de la barra de navegación
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("🏠 Home", href="/", active="exact")),
                    dbc.NavItem(dbc.NavLink("📊 Visualizations", href="/visualizations", active="exact",)),
                ],
                pills=True, 
            ),
        ]),
        color="dark", dark=True,
    ),

    # Contenido de la página
    dash.page_container
])

# ======================================================================================================================
#                                              EJECUCIÓN DE LA APLICACIÓN
# ======================================================================================================================
if __name__ == '__main__':
    app.run_server(debug=True)