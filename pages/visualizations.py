import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

templates = ["minty"]
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

# ======================================================================================================================
#                                               DICCIONARIOS AUXILIARES
# ======================================================================================================================
course_name = {
    "33": "Biofuel Production Technologies",
    "171": "Animation and Multimedia Design",
    "8014": "Social Service (evening attendance)",
    "9003": "Agronomy",
    "9070": "Communication Design",
    "9085": "Veterinary Nursing",
    "9119": "Informatics Engineering",
    "9130": "Equinculture",
    "9147": "Management",
    "9238": "Social Service",
    "9254": "Tourism",
    "9500": "Nursing",
    "9556": "Oral Hygiene",
    "9670": "Advertising and Marketing Management",
    "9773": "Journalism and Communication",
    "9853": "Basic Education",
    "9991": "Management (evening attendance)",
}

# ======================================================================================================================
#                                                     TARJETAS
# ======================================================================================================================

# Valores para tarjetas
# TODO ajustar código para calcularlos a partir de base en RDS en AWS
df_graph_a = len(df)
df_graph_b = f"{round(len(df[df['Target'] == 'Graduate']) / df_graph_a * 100, 2)}%"
df_graph_c = round(len(df[df['Target'] == 'Dropout']) / df_graph_a * 100, 2)
delta_graph_c = f"{round(df_graph_c - 29.0, 2)}%"
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
                html.H4(card_data["value"], className="card-text",),
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
#                                       GRÁFICO PARA TAB 1: DROPOUT RATE BY COURSE
# ======================================================================================================================

# Calcula el porcentaje de graduate, enrolled y dropout por carrera
total_counts = df.groupby('Course')['Target'].count()
graduate_percentage = df[df['Target'] == 'Graduate'].groupby('Course')['Target'].count() / total_counts * 100
enrolled_percentage = df[df['Target'] == 'Enrolled'].groupby('Course')['Target'].count() / total_counts * 100
dropout_percentage = df[df['Target'] == 'Dropout'].groupby('Course')['Target'].count() / total_counts * 100
# Estudiantes totales por carrera


# Crea un nuevo DataFrame con los porcentajes
percentage_df = pd.DataFrame({'Course': total_counts.index,
                              'Students': total_counts.values,
                              'Graduate': graduate_percentage,
                              'Enrolled': enrolled_percentage,
                              'Dropout': dropout_percentage})

# Reemplaza los códigos de las carreras con sus nombres
percentage_df['Course'] = percentage_df['Course'].map(course_name)

# Ordena el DataFrame por el porcentaje de dropout de mayor a menor
percentage_df = percentage_df.sort_values(by='Dropout', ascending=False)

# Crea un gráfico de barras apiladas con las 10 carreras con mayor porcentaje de dropout
n_registros = 10
fig = px.bar(percentage_df.head(n_registros), x='Dropout', y='Course',
             labels={'variable': 'Course', 'value': 'Dropout rate'},
             barmode="relative",
             hover_data={'Course': False, 
                         'Dropout': False,
                         'Dropout rate': [str(round(percentage, 1))+'%' for percentage in percentage_df['Dropout'].head(n_registros).values],
                         'Students': True,},
             )

# Cursos que se pintarán de rojo oscuro
red_courses = ['Biofuel Production Technologies', 'Informatics Engineering', 'Management (evening attendance)']

# Personaliza los colores de las barras
colors = ['#E87479' if course in red_courses 
          else '#F7BBBD' if course in percentage_df['Course'].head(5).values 
          else 'lightgrey' for course in percentage_df['Course']]

fig.update_traces(marker=dict(color=colors)),

# Agregar porcentajes en el hover
fig.update_traces(texttemplate='%{value:.1f}%', textposition='inside')

# Personaliza el diseño y estilo
fig.update_xaxes(showticklabels=False)
fig.update_yaxes(categoryorder='total ascending')

# Añadir línea vertical en el 29% con opacidad al 70% (Requiere modificar margin a t=50)
# fig.add_vline(x=29, line_width=2, line_dash="dash", line_color="#549f93", opacity=0.7, annotation_text="Portugal (29%)", annotation_position="top")

fig.update_layout(xaxis_title='', yaxis_title='Courses', margin=dict(t=10,b=5), height=350)


# ======================================================================================================================
#                                                       TABS
# ======================================================================================================================

# TAB 1: DROPOUT RATE BY COURSE
tab1_content = dbc.Card(

    dbc.CardBody([
        dbc.Row([
            
            # Gráfico E: Dropout rate by Course
            dbc.Col([
                dbc.Card([

                    # Título del gráfico
                    dbc.CardHeader([
                        html.H4([html.I(className="fa fa-user-minus"), '\tTop 10 Courses with Highest Dropout Rate']),
                    ]),
                    
                    dcc.Graph(figure=fig),

                ], className="mt-4 shadow"),
            ], width=8),

            # Comentarios a la derecha
            dbc.Col([
                html.Br(),
                html.H2('🚧 Insights'),

                # Viñetas (html.Li) dentro de una lista (html.Ul)
                html.Ul([
                    html.Li('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
                    html.Li('Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'),
                    html.Li('Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'),
                    html.Li('Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
                ]),
                
            ], width=4),
            
        ], style={'padding-left': '20px', 'padding-right': '20px', 'padding-bottom': '20px'}),
    ])
)


tab2_content = dbc.Card(

    dbc.CardBody([
        html.P("This is tab 2!"),
    ])
)

# Crea el objeto layout
tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Dropout rate by Course"),
        dbc.Tab(tab2_content, label="Tab 2"),
        dbc.Tab(
            "This tab's content is never seen", label="Tab 3", disabled=True
        ),
    ], style={'padding-left': '20px', 'padding-right': '20px', 'padding-bottom': '0px', 'padding-top': '30px'}
)


# ======================================================================================================================
#                                               CONTENIDO DE LA PÁGINA
# ======================================================================================================================

layout = html.Div([

    # Título
    dbc.Row([
        html.H3('🚧 Visualizaciones (En construcción)'),
    ], style={'padding-left': '20px', 'padding-right': '20px', 'padding-top': '10px'}),
    
    # Primera fila: Tarjetas generadas por el bucle
    dbc.Row(cards, style={'padding-left': '20px', 'padding-right': '20px'}),

    # Segunda fila: Gráficos
    tabs,

])
