import streamlit as st
import plotly.express as px
import numpy as np
from IPython.display import display

np.random.seed(1)

x = np.random.rand(100)
y = np.random.rand(100)

fig = px.scatter(x=x, y=y, color_discrete_sequence=['#a3a7e4'])
fig.update_traces(marker_size=10)


def update_point(trace, points, selector):
    c = list(fig.data[0].marker.color)
    s = list(fig.data[0].marker.size)
    for i in points.point_inds:
        c[i] = '#bae2be'
        s[i] = 20
    fig.data[0].marker.color = c
    fig.data[0].marker.size = s


fig.data[0].on_click(update_point)

#st.plotly_chart(fig, use_container_width=True)
display(fig)
