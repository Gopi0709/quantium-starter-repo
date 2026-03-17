import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("processed_data.csv")

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Group sales by date
sales_by_date = df.groupby('date')['sales'].sum().reset_index()

# Create line chart
fig = px.line(
    sales_by_date,
    x='date',
    y='sales',
    title='Pink Morsel Sales Over Time'
)

# Create app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Analysis"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)