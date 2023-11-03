import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
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

school_name = {
    "33": "ESTG",
    "171": "ESTG",
    "8014": "ESECS",
    "9003": "ESAE",
    "9070": "ESTG",
    "9085": "ESAE",
    "9119": "ESTG",
    "9130": "ESAE",
    "9147": "ESTG",
    "9238": "ESECS",
    "9254": "ESECS",
    "9500": "ESS",
    "9556": "ESS",
    "9670": "ESECS",
    "9773": "ESECS",
    "9853": "ESECS",
    "9991": "ESTG",
}


# ======================================================================================================================
#                                                     TARJETAS
# ======================================================================================================================

# Valores para tarjetas
# TODO ajustar código para calcularlos a partir de base en RDS en AWS
card_val_a = len(df)
card_val_b = f"{round(len(df[df['Target'] == 'Graduate']) / card_val_a * 100, 2)}%"
card_val_c = round(len(df[df['Target'] == 'Dropout']) / card_val_a * 100, 2)
delta_card_c = f"{round(card_val_c - 29.0, 2)}%"
card_val_c = f"{card_val_c}%"

# Lista de datos para las tarjetas
cards_data = [
    {
        "icon_class": "fa fa-users",
        "bg_color": "bg-info",
        "value": card_val_a,
        "footer_text": "Students in dataset"
    },
    {
        "icon_class": "fa fa-user-graduate",
        "bg_color": "bg-success",
        "value": card_val_b,
        "footer_text": "Success rate"
    },
    {
        "icon_class": "fa fa-user-minus",
        "bg_color": "bg-secondary",
        "value": card_val_c,
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
                html.Span(delta_card_c if card_data["footer_text"].startswith("Dropout rate") else "", className="text-secondary"),
                html.Span(" vs Portugal" if card_data["footer_text"].startswith("Dropout rate") else "", className="text-secondary"),
            ]),
        ]),
    ], className="mt-4 shadow"))
    cards.append(card)

# ======================================================================================================================
#                                       GRÁFICOS PARA TAB 1: DROPOUT RATE BY COURSE
# ======================================================================================================================

# Calcula el porcentaje de graduate, enrolled y dropout por carrera
total_counts = df.groupby('Course')['Target'].count()
graduate_percentage = df[df['Target'] == 'Graduate'].groupby('Course')['Target'].count() / total_counts * 100
enrolled_percentage = df[df['Target'] == 'Enrolled'].groupby('Course')['Target'].count() / total_counts * 100
dropout_percentage = df[df['Target'] == 'Dropout'].groupby('Course')['Target'].count() / total_counts * 100

# Crea un nuevo DataFrame con los porcentajes
percentage_df = pd.DataFrame({'Course': total_counts.index,
                              'Students': total_counts.values,
                              'Graduate': graduate_percentage,
                              'Enrolled': enrolled_percentage,
                              'Dropout': dropout_percentage})

# Reemplaza los códigos de las carreras con sus nombres
percentage_df['Course'] = percentage_df['Course'].map(course_name)

# Añade una columna con el nombre de la escuela a partir del indice de la carrera
percentage_df['School'] = percentage_df.index.map(school_name)


# Ordena el DataFrame por el porcentaje de dropout de mayor a menor
percentage_df = percentage_df.sort_values(by='Dropout', ascending=False)

def create_figure(percentage_df, n_registros, highlighted_courses, top=True):

    topmargin = 15
    altura = 350
    
    # Si no hay carreras destacadas, se muestran todas
    if len(highlighted_courses) == 0:
        topmargin = 30
        altura = 650
        colors = ['#78C2AD' if course in percentage_df['Course'].tail(4).values
                  else 'lightgrey' for course in percentage_df['Course'].head(n_registros).values]
    
    elif top:
        percentage_df = percentage_df.head(n_registros)
        colors = ['#E87479' if course in highlighted_courses
                  else '#F7BBBD' if course in percentage_df['Course'].head(5).values
                  else 'lightgrey' for course in percentage_df['Course'].head(n_registros).values]
    else:
        percentage_df = percentage_df.tail(n_registros)
        colors = ['#78C2AD' if course in highlighted_courses
                  else 'lightgrey' for course in percentage_df['Course'].tail(n_registros).values]
        topmargin = 35

    fig = px.bar(percentage_df, x='Dropout', y='Course',
                 labels={'variable': 'Course', 'value': 'Dropout rate'},
                 barmode="relative",
                 hover_data={'Course': False, 'Dropout': False,
                             'School': True,
                             'Dropout rate': [f'{percentage:.1f}%' for percentage in percentage_df['Dropout'].values],
                             'Students': True})
    
    fig.update_traces(marker=dict(color=colors))
    fig.update_traces(texttemplate='%{value:.1f}%', textposition='inside')
    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(categoryorder='total ascending')
    fig.update_layout(xaxis_title='', yaxis_title='Courses', margin=dict(t=topmargin, b=5), height=altura)

    if not top or len(highlighted_courses) == 0:
        fig.add_vline(x=29, line_width=2, line_dash="dash", line_color="#549f93", opacity=0.7, annotation_text="Portugal (29%)", annotation_position="top")

    return fig

fig0 = create_figure(percentage_df, 17, highlighted_courses=[])

n_registros = 10

highlighted_courses = ['Biofuel Production Technologies', 'Informatics Engineering', 'Management (evening attendance)']
fig1 = create_figure(percentage_df, n_registros, highlighted_courses)

highlighted_courses = ['Biofuel Production Technologies']
fig2 = create_figure(percentage_df, n_registros, highlighted_courses)

# ======================================================================================================================
#                                           TAB 1: DROPOUT RATE BY COURSE
# ======================================================================================================================
tab1_content = dbc.Card(

    dbc.CardBody([
        dbc.Row([
            
            # Gráfico a la izquierda
            dbc.Col([
                dbc.Card([

                    # Título del gráfico
                    dbc.CardHeader([
                        html.Div(id='title_cardhead_1', className='card-title'),
                    ]),
                    
                    # Gráfico
                    dcc.Graph(id='graph1', style={"maxHeight": "370px", "overflow-y": "scroll"}, config={'displayModeBar': False}),

                ], className="mt-4 shadow"),
            ], width=8),

            # Comentarios a la derecha
            dbc.Col([
                html.Br(),
                
                # Grupo de 3 botones a partir de los cuales se mostrará un output
                html.Div(
                    [
                        dbc.RadioItems(
                            id="radios",
                            className="btn-group",
                            inputClassName="btn-check",
                            labelClassName="btn btn-outline-primary",
                            labelCheckedClassName="active",
                            options=[
                                {"label": "Overview", "value": 0},
                                {"label": "Insight 1", "value": 1},
                                {"label": "Insight 2", "value": 2}
                            ],
                            value=0,
                        ),
                    ],
                    className="radio-group",
                ),
                
                html.Hr(),
               
                # Output que depende de los botones
                html.Div(id="output-radio-group"),

            ], width=4),
            
        ], style={'padding-left': '20px', 'padding-right': '20px', 'padding-bottom': '20px'}),
    ])
)

# ======================================================================================================================
#                                           TAB 2: DROPOUT RATE BY COURSE
# ======================================================================================================================
tab2_content = dbc.Card(

    dbc.CardBody([
        dcc.Input(id='input-element', type='text', placeholder='Ingrese texto aquí'),
        html.Div(id='output-element')  # Aquí mostraremos la salida del callback
    ])
)



# ======================================================================================================================
#                                                    TABS' LAYOUT
# ======================================================================================================================
tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Dropout rate by Course"),
        dbc.Tab(tab2_content, label="Tab 2"),
        dbc.Tab(
            "This tab's content is never seen", label="Tab 3", disabled=True
        ),
    ], style={'padding-left': '20px', 'padding-right': '20px', 'padding-bottom': '10px', 'padding-top': '30px'}
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


# ======================================================================================================================
#                                               CALLBACKS
# ======================================================================================================================

# Callback Tab 1: DROPOUT RATE BY COURSE
@dash.callback([Output("output-radio-group", "children"),
                Output('graph1', 'figure'),
                Output('title_cardhead_1', 'children')],
               [Input("radios", "value")])
def display_value(value):

    op0 = html.H4([html.I(className="fa fa-users"), '\t Courses by Dropout Rate']),
    op1 = html.H4([html.I(className="fa fa-user-minus"), '\t Top 10 Courses by Dropout Rate']),

    if value == 0:
        
        comentarios = dcc.Markdown('''
        ##### Overview
        - **<span style='color:#78C2AD' children=\"4 of 17 programs\" />** have maintained **dropout rates below the national average**.
        ''', dangerously_allow_html=True)
        return comentarios, fig0, op0
    
    elif value == 1:
        comentarios = html.Div([
            dcc.Markdown('''
            ##### Pay special attention to the ESTG
            - **<span style='color:#E87479' children=\"3 of the top 5 programs\" />** with the **highest dropout rates** are from the **Escola Superior de Tecnologia e Gestão (ESTG)**. 
            - This suggests that there may be specific challenges within ESTG contributing to higher dropout rates.
            ''', dangerously_allow_html=True),
        ])
        return comentarios, fig1, op1
    
    elif value == 2:
        comentarios = dcc.Markdown('''
        ##### Biofuel Production Technologies: An Alarmingly High Dropout Rate
        - **<span style='color:#E87479' children=\"Biofuel Production Technologies\" />** stands out with the **highest dropout rate at 67.7%**, surpassing the national average by a significant 38.7%.                         
        - The program's small enrollment of **only 12 students could impact its reliability** given the high dropout rate.
        ''', dangerously_allow_html=True)
        return comentarios, fig2, op1
    else:
        return 'Tiririri', fig0, op0
