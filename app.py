import dash
from dash import dcc, html
from dash_table import DataTable
import pandas as pd

# Incorporate data
df = pd.read_csv("./storage/NIS_2019_Hospital.csv")

# Initialize the app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    DataTable(
        id='my-datatable',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records'),
        style_table={'height': '1000px', 'overflowY': 'auto'},
        style_header={'text-align': 'center'},
        page_size=100
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)