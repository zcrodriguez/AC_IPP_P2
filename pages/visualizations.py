import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.graph_objects as go
import plotly.express as px
import json
import pickle
import pandas as pd
from dash.exceptions import PreventUpdate

templates = ["sketchy"]
load_figure_template(templates)

# Registrar la página
dash.register_page(__name__)

# Estilo del icono de las tarjetas
card_icon = {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto",
}

# ======================================================================================================================
#                                                      CARGA DE DATOS     
# ======================================================================================================================

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('Caro\'s_files/data_viz.csv', dtype={'Course': 'category'})  # Asegúrate de que la ruta sea correcta

# Valores para tarjetas
# TODO ajustar código para calcularlos a partir de base en RDS en AWS
df_graph_a = len(df)
df_graph_b = f"{round(len(df[df['Target'] == 'Graduate']) / df_graph_a * 100, 2)}%"
df_graph_c = round(len(df[df['Target'] == 'Dropout']) / df_graph_a * 100, 2)
delta_graph_c = f"{round(df_graph_c - 8.1, 2)}%"
df_graph_c = f"{df_graph_c}%"

# Lista de datos para las tarjetas
cards_data = [
    {
        "icon_class": "fa fa-users",
        "bg_color": "bg-info",
        "value": df_graph_a,
        "footer_text": "Students in dataset"
    },
    {
        "icon_class": "fa fa-user-graduate",
        "bg_color": "bg-success",
        "value": df_graph_b,
        "footer_text": "Success rate"
    },
    {
        "icon_class": "fa fa-user-minus",
        "bg_color": "bg-secondary",
        "value": df_graph_c,
        "footer_text": "Dropout rate | "
    },
]

# Bucle para generar las tarjetas de la primera fila
cards = []
for card_data in cards_data:
    card = dbc.Col(dbc.CardGroup([
        dbc.Card(html.Div(className=card_data["icon_class"], style=card_icon), className=card_data["bg_color"], style={"maxWidth": 75}),
        dbc.Card([
            dbc.CardBody([
                html.H3(card_data["value"], className="card-text",),
            ]),
            dbc.CardFooter([
                html.H6(card_data["footer_text"], style={"display": "inline"}),
                html.I(className="fa fa-caret-up text-secondary") if card_data["footer_text"].startswith("Dropout rate") else '',
                html.Span(delta_graph_c if card_data["footer_text"].startswith("Dropout rate") else "", className="text-secondary"),
                html.Span(" vs Portugal" if card_data["footer_text"].startswith("Dropout rate") else "", className="text-secondary"),
            ]),
        ]),
    ], className="mt-4 shadow"))
    cards.append(card)

# ======================================================================================================================
#                                                      GRÁFICOS
# ======================================================================================================================

# Calcula el porcentaje de graduate, enrolled y dropout por carrera
total_counts = df.groupby('Course')['Target'].count()
graduate_percentage = df[df['Target'] == 'Graduate'].groupby('Course')['Target'].count() / total_counts * 100
enrolled_percentage = df[df['Target'] == 'Enrolled'].groupby('Course')['Target'].count() / total_counts * 100
dropout_percentage = df[df['Target'] == 'Dropout'].groupby('Course')['Target'].count() / total_counts * 100

# Crea un nuevo DataFrame con los porcentajes
percentage_df = pd.DataFrame({'Course': total_counts.index,
                              'Graduate': graduate_percentage,
                              'Enrolled': enrolled_percentage,
                              'Dropout': dropout_percentage})

# Ordena el DataFrame por el porcentaje de dropout de mayor a menor
percentage_df = percentage_df.sort_values(by='Dropout', ascending=True)

# Seleccionar solo top 5
percentage_df = percentage_df.tail(5)

# Crea un gráfico de barras apiladas
fig = px.bar(percentage_df, x=['Dropout', 'Enrolled', 'Graduate'], y='Course',
             labels={'variable': 'Categoría', 'value': 'Porcentaje'},
             color_discrete_map={'Graduate': 'green', 'Enrolled': 'blue', 'Dropout': 'red'},
             barmode="relative")

# Restablece el índice para que las carreras se muestren en el orden correcto
fig.update_xaxes(categoryorder='total ascending')

# Agregar porcentajes en el hover
fig.update_traces(texttemplate='%{value:.2f}%', textposition='inside')

# Personaliza el diseño y estilo
fig.update_layout(xaxis_title='Carrera', yaxis_title='Porcentaje (%)')



# ======================================================================================================================
#                                               CONTENIDO DE LA PÁGINA
# ======================================================================================================================

layout = html.Div([

    # Título
    dbc.Row([
        html.H3('🚧 Visualizaciones (En construcción)'),
    ], style={'padding-left': '20px', 'padding-right': '20px', 'padding-top': '10px'}),
    
    # Primera fila con tarjetas generadas por el bucle
    dbc.Row(cards, style={'padding-left': '20px', 'padding-right': '20px'}),

    # Segunda fila vacía
    dbc.Row([

        # Gráfico D: 
        dbc.Col([
            dbc.Card([
                html.H4('En proceso', style={'padding-left': '20px', 'padding-right': '20px', 'padding-top': '20px'}),

                # Insertar esta imagen https://cdn.sisense.com/wp-content/uploads/meme5-370x236.jpg centrada, con el siguiente código:
                html.Img(src="https://cdn.sisense.com/wp-content/uploads/meme5-370x236.jpg", style={'display': 'block', 'margin-left': 'auto', 'margin-right': 'auto', 'width': '80%'}),

            ], className="mt-4 shadow"),
        ], width=6),


        # Gráfico E: Stacked Bar Chart by Course
        dbc.Col([
            dbc.Card([
                    html.H4('Stacked Bar Chart by Course', style={'padding-left': '20px', 'padding-right': '20px', 'padding-top': '20px'}),
                    dcc.Graph(figure=fig)
                ], className="mt-4 shadow"),
            ], width=6),
        ], style={'padding-left': '20px', 'padding-right': '20px', 'padding-bottom': '20px'}),

])

