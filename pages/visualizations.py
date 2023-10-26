import dash
from dash import html, dcc, Input, Output, State, MATCH, ALL
from dash.exceptions import PreventUpdate

dash.register_page(__name__)

layout = html.Div([
    dcc.Store(id="session-store", data={}),
    html.H1('This is our Visualizations page'),
    html.Div([
        "Select a city: ",
        dcc.RadioItems(
            options=['New York City', 'Montreal', 'San Francisco'],
            id='visualizations-input',
            persistence=True  # Habilitar la persistencia para mantener el estado
        )
    ]),
    html.Br(),
    html.Div(id='visualizations-output'),
])


@dash.callback(
    Output('session-store', 'data'),
    Input('visualizations-input', 'value')
)
def update_session_data(selected_city):
    if selected_city is None:
        raise PreventUpdate
    return {'selected_city': selected_city}


@dash.callback(
    Output('visualizations-output', 'children'),
    Input('session-store', 'data')
)
def update_visualizations_output(data):
    selected_city = data.get('selected_city', 'Montreal')
    return f"You selected: {selected_city}"
