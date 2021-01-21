# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.express as px
# import pandas as pd

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# # assume you have a "long-form" data frame
# # see https://plotly.com/python/px-arguments/ for more options
# df = pd.read_csv('https://raw.githubusercontent.com/daniel-dc-cd/data_science/master/module_3_Python/data/titanic.csv')
# fig = px.bar(df, x="Sex", y="Survived")#color="City", barmode="group")
# fig1 = px.bar(df, x ="Survived")

# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),

#     html.Div(children='''
#         Dash: A web application framework for Python.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# #     dcc.Graph(
# #         id='example-grap',
# #         figure=fig1
# #     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)
import seaborn as sns
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
df = pd.read_csv('https://raw.githubusercontent.com/daniel-dc-cd/data_science/master/module_3_Python/data/titanic.csv')
f= df.groupby(df['Pclass']).sum()
df1 = df
df1.loc[df1['Age'] <=13, 'Category'] = 'Child'
df1.loc[df1['Age'] >13, 'Category'] = 'Adult'
df1.loc[df1['Age'].isna()==True, 'Category'] = 'Null'

app = dash.Dash()
app.layout = html.Div([
html.Div([
html.Div([
html.H1("Titanic Dashboard"),
html.H3("Sex: Survived"),
dcc.Graph(id="g1", figure= px.bar(df, x="Sex", y="Survived", color="Sex"))
], className="six columns"),

    html.Div([
        html.H3('Age Vs Fare'),
        dcc.Graph(id='g2', figure=px.scatter(df, x="Age", y="Fare", color="Age", hover_name="Fare",
                 log_x=True, size_max=60))
    ], className="six columns"),
   

    html.Div([
        html.H3('Number of passenger in each class'),
        dcc.Graph(id='g3', figure=px.bar(f, x=f.index, y="PassengerId", color= f.index))
    ], className="six columns"),
    
     html.Div([
        html.H3('Age Category: Survived'),
        dcc.Graph(id='g4', figure=px.bar(df1, x="Category", y="Survived", color="Category"))
    ], className="six columns"),
    

#      html.Div([
#         html.H3('Age Category: Survived vs Dead'),
#         dcc.Graph(id='g5', figure=px.bar(df1, x="Category", y=df1[df1['Survived']==0].Survived))
#     ], className="six columns"),

        
], className="row")
])

app.css.append_css({
"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css 304"
})

if __name__ == '__main__':
    app.run_server(debug=True)