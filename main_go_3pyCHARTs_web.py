# --------------------------------------------------------------------------------
# Tobias Haueter                                                        2021-09-27
# Chart plotting software for .csv files on localhost web browser.
# .csv -> comma separated value
#
# sudo apt install python3-plotly
# https://plotly.com/python/subplots/
# --------------------------------------------------------------------------------


import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# read csv file and choose the delimiter.
df = pd.read_csv('testDATA/dataframe.pycharts', delimiter=',')  # <TAB>: delimiter='\t'

# Initialize figure with subplots
fig = make_subplots(
    rows=3, cols=1,
    shared_xaxes=True,
    shared_yaxes=False,
    vertical_spacing=0.05
)

# Plot 01
fig.add_trace(go.Scatter(
    x=df['time'],
    y=df['rpm'],
    mode='lines',
    name='rpm [min-1]',
    line=dict(color="#1ca400")
), row=1, col=1)

fig.update_xaxes(
    title_text="",
    row=1, col=1)  # range=[10, 50], showgrid=False, type="log"

fig.update_yaxes(
    title_text="y1_rpm",
    row=1, col=1)  # range=[10, 50], showgrid=False, type="log"

# Plot 02
fig.add_trace(go.Scatter(
    x=df['time'],
    y=df['power'],
    mode='lines',
    name='power [kW]',
    line=dict(color="#0066ff")
), row=2, col=1)

fig.update_xaxes(
    title_text="",
    row=2, col=1)  # range=[10, 50], showgrid=False, type="log"

fig.update_yaxes(
    title_text="y2_power",
    row=2, col=1)  # range=[10, 50], showgrid=False, type="log"

# Plot 03
fig.add_trace(go.Scatter(
    x=df['time'],
    y=df['current'],
    mode='lines',
    name='ECU_current [A]',
    line=dict(color="#ff0000")
), row=3, col=1)

fig.update_xaxes(
    title_text="x0_time = daily seconds - 10Hz",
    row=3, col=1)  # range=[10, 50], showgrid=False, type="log"

fig.update_yaxes(
    title_text="y3_current",
    row=3, col=1)  # range=[10, 50], showgrid=False, type="log"

# site properties
fig.update_layout(
    title='pyCHARTs - ECU Current Measurement',
    legend_title="Legend Title",
    plot_bgcolor='#e3ebff',
    showlegend=True)

fig.show()
