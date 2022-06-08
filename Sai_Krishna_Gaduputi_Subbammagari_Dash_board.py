import pandas as pd
from xlsxwriter import Workbook
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
file="https://github.com/saikrishnags05/Tools-For-Data-Analysis/blob/main/Sai_krishna_Gaduputi_Subbammagari_Data_Set.xlsx"
app = Dash(__name__)
plot_1 = pd.read_excel('Sai_krishna_Gaduputi_Subbammagari_Data_Set.xlsx','Sheet1',)
plot_2 = pd.read_excel('Sai_krishna_Gaduputi_Subbammagari_Data_Set.xlsx','Sheet2',)
plot_3 = pd.read_excel('Sai_krishna_Gaduputi_Subbammagari_Data_Set.xlsx','Sheet3',)
plot_4 = pd.read_excel('Sai_krishna_Gaduputi_Subbammagari_Data_Set.xlsx','Sheet4',)
plot_5 = pd.read_excel('Sai_krishna_Gaduputi_Subbammagari_Data_Set.xlsx','Sheet5',)
plot_6 = pd.read_excel('Sai_krishna_Gaduputi_Subbammagari_Data_Set.xlsx','Sheet6',)

fig_grouped_single_5 = px.choropleth(plot_3,  # Input Pandas DataFrame
                    locations='GESTFIPS_data',  # DataFrame column with locations
                    color='population',# DataFrame column with color values,
                    color_discrete_sequence=px.colors.sequential.Blues,
                    hover_name='state',# DataFrame column hover info
                    animation_frame="Year",
                    locationmode = 'USA-states') # Set to plot as US States 
fig_grouped_single_5.update_layout(
     geo_scope='usa',  # Plot only the USA instead of globe
)
#----------------------PLOT-4--------------------------------
fig_line = px.line(plot_4, x="Year", y="population",color="GTCBSASZ_data")
fig_line .update_layout(showlegend=False)
#-----------------------------PLOT-5-----------------------
bar_state_fig_2 = px.bar(plot_5 , x="state", y="population",animation_frame="Year")

#--------------plot-6----------------------------

app.layout = html.Div([
        html.Div([
        html.Center(html.H1("Graphical Representation of United States Census Bureau Data ")),]),
    html.Div([
        html.Div([
            html.H3("Mother's Native Place"),
            dcc.Dropdown(
                plot_1["Father_nat"].unique(),
                value='United States',
                id='xaxis-column'
            ),
            
        ], style={'width': '50%', 'display': 'inline-block'}),

        html.Div([
            html.H3("Father's Native Place"),
            dcc.Dropdown(
                plot_1["Mother_nat"].unique(),
                value='United States',
                id='yaxis-column'
            ),
        ], style={'width': '50%', 'display': 'inline-block'}),
        html.Center(html.H3("Residential population based Father's and Mother's Native place")),
            dcc.Graph(id='indicator-graphic'),
    ], style={'width': '50%', 'float': 'left', 'display': 'inline-block'}),

    html.Div([
                html.Center(html.H3("Overall increment and decrement of Population with respect to years")),
                dcc.Graph(figure=fig_grouped_single_5)
        ], style={'width': '50%',  'display': 'inline-block'}),

    html.Div([
            html.H3("Type of Area"),
            dcc.Dropdown(
                plot_2["GTCBSAST_data"].unique(),
                value='Balance Metropolitan',
                id='area_column'
            ),
            html.Center(html.H3("Overall increment and decrement in Maritual Status based on Population with respect to years")),
    dcc.Graph(id='bar' ),
        ], style={'width': '50%', 'float': 'right', 'display': 'inline-block'}),
    
           # html.Div([
                
       # ], style={'width': '50%','float': 'left',  'display': 'inline-block'}),
    

    html.Div([
                html.Center(html.H3("Overall increment and decrement of Population with respect to Metropolitan Statistical Area Size and years")),
                dcc.Graph(figure=fig_line),
        ], style={'width': '50%',  'display': 'inline-block'}),
    html.Div([
                html.Center(html.H3("Overall increment and decrement of Population with respect to years")),
                dcc.Graph(figure=bar_state_fig_2),
        ], style={'width': '100%',  'display': 'inline-block'}),
    html.Div([
            html.H3("Select the state name"),
            dcc.Dropdown(
                plot_6["state"].unique(),
                value='California',
                id='state_name'
            ),
        ], style={'width': '50%',  'display': 'inline-block'}),
    
        html.Div([
            dcc.Graph(id='city-state'),
        ], style={'width': '100%', 'float': 'left', 'display': 'inline-block'}),
    

],style={'width': '100%','display': 'inline-block'})

@app.callback(
    Output('city-state', 'figure'),
    Input('state_name', 'value'))

def update_graph(state_name):
    dff = plot_6[(plot_6["state"] == state_name) ]
    grouped= dff.groupby(['Year','City']).agg({'population': ['sum']})
    grouped.columns = ['population']
    grouped= grouped.reset_index()
    grouped=grouped.dropna()
    grouped=grouped.sort_values(by=['Year','City'])
    fig_4 = px.bar(dff, x="City", y="population",animation_frame="Year")
    return fig_4

@app.callback(
    Output('bar', 'figure'),
    Input('area_column', 'value'))
def update_graph(area_column):
    dff = plot_2[(plot_2["GTCBSAST_data"] == area_column)]
    fig_2 = px.bar(dff, y="PEMARITL_data",animation_frame="Year",hover_name='GTCBSAST_data',color="GTCBSAST_data",x='population')
    fig_2.update_layout(showlegend=False)
    fig_2.update_layout(
    yaxis_title='Marital status of ',
    xaxis_title='Total Population')
    
    return fig_2
@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'))

def update_graph(xaxis_column_name, yaxis_column_name):
    dff = plot_1[(plot_1["Mother_nat"] == xaxis_column_name) & (plot_1["Father_nat"] == yaxis_column_name) ]
    fig=px.scatter_geo(dff, 'lat', 'lon', 
               hover_data=['state', 'City','Father_nat','Mother_nat','population'],
               size='population',
               color='population',
               color_continuous_scale = px.colors.qualitative.Prism,
               scope="usa",
               animation_frame='Year')


       # fig.show()
    return fig


if __name__ == '__main__':
    app.run_server(port=8051)








