import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("processed_data.csv")

# Convert date and normalize region
df['date'] = pd.to_datetime(df['date'])
df['region'] = df['region'].str.lower()

# Create Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div(style={
    'backgroundColor': '#f4f6f9',
    'padding': '30px',
    'fontFamily': 'Arial'
}, children=[

    # Title
    html.H1("Soul Foods Sales Visualiser", style={
        'textAlign': 'center',
        'color': '#2c3e50',
        'marginBottom': '30px'
    }),

    # 🔥 Horizontal Radio Buttons (Professional)
    html.Div([
        html.Label("Select Region:", style={
            'fontSize': '20px',
            'fontWeight': '600',
            'marginBottom': '15px',
            'display': 'block',
            'textAlign': 'center'
        }),

        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East', 'value': 'east'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            inline=True,  # ✅ Horizontal alignment
            inputStyle={"marginRight": "6px"},
            labelStyle={
                'marginRight': '25px',
                'fontSize': '16px',
                'cursor': 'pointer'
            }
        )
    ], style={
        'textAlign': 'center',
        'marginBottom': '30px'
    }),

    # Graph container
    dcc.Graph(id='sales-graph', style={
        'backgroundColor': 'white',
        'padding': '10px',
        'borderRadius': '10px',
        'boxShadow': '0px 2px 8px rgba(0,0,0,0.1)'
    })

])

# Callback
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):

    # Filter data
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    # Group data
    sales_by_date = filtered_df.groupby('date')['sales'].sum().reset_index()

    # Create line chart
    fig = px.line(
        sales_by_date,
        x='date',
        y='sales',
        title='Pink Morsel Sales Over Time',
        labels={
            'date': 'Date',
            'sales': 'Total Sales'
        }
    )

    # 🔴 Safe vertical line (no errors)
    fig.add_shape(
        type="line",
        x0="2021-01-15",
        x1="2021-01-15",
        y0=0,
        y1=1,
        xref="x",
        yref="paper",
        line=dict(color="red", dash="dash", width=2)
    )

    fig.add_annotation(
        x="2021-01-15",
        y=1,
        yref="paper",
        text="Price Increase",
        showarrow=False,
        font=dict(color="red", size=12)
    )

    # Styling graph
    fig.update_layout(
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#2c3e50'),
        title_x=0.5
    )

    return fig


# Run app
if __name__ == '__main__':
    app.run(debug=True)