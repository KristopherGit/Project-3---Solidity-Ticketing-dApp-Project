import streamlit as st
import plotly.graph_objs as go

# Create data
x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]
seat_names = ["Seat 1", "Seat 2", "Seat 3", "Seat 4", "Seat 5"]
colors = ["red"]*len(x)  # set initial color to red
seat_colors = dict(zip(seat_names, colors))

# Get session state to preserve trace variable
seat_colors = st.experimental_get_session_state()

# Create trace
trace = go.Scatter(x=x, y=y, mode='markers', marker=dict(color=colors))

# Create figure
fig = go.Figure(data=[trace])

# Create selectbox
options = seat_names
selected_seat = st.selectbox("Select a seat:", options)

# Create button
if st.button("Change color"):
    if selected_seat in seat_colors:
        seat_colors[selected_seat] = "green"
    trace.marker.color = [seat_colors[seat] for seat in seat_names]
    st.experimental_set_session_state(seat_colors)

st.plotly_chart(fig)
