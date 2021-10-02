# --------------------------------------------------------------------------------
# Tobias Haueter                                                        2021-09-27
# Chart plotting software for .csv files on localhost web browser.
#
# sudo apt install python3-plotly
# --------------------------------------------------------------------------------


import pandas as pd
import plotly.graph_objects as go

# read csv file and choose the delimiter.
df = pd.read_csv('testDATA/dataframe.pycharts', delimiter=',')  # <TAB>: delimiter='\t'

# Initialize figure with subplots
fig = go.Figure()

# Plot 01
fig.add_scatter(
    x=df['time'],
    y=df['rpm'],
    mode='lines',
    name='rpm [min-1]',
    line=dict(color="#1ca400")
)

# Plot 02
fig.add_scatter(
    x=df['time'],
    y=df['power'],
    mode='lines',
    name='power [kW]',
    line=dict(color="#0066ff")
)

# Plot 03
fig.add_scatter(
    x=df['time'],
    y=df['current'],
    mode='lines',
    name='ECU_current [A]',
    line=dict(color="#ff0000")
)

# Site properties
fig.update_layout(
    title='pyCHARTs - ECU Current Measurement',
    xaxis_title="x0_time = daily seconds - 10Hz",
    yaxis_title="y_axis",
    legend_title="Legend Title",
    showlegend=True,
    plot_bgcolor='#e3ebff'
)

fig.show()
