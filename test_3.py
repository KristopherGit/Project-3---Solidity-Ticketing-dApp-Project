import streamlit as st
import plotly.graph_objs as go
import math

# Create a dictionary that holds the attributes of each seat
seats = {}

# Create a function that generates a grid of seats


def create_seat_grid():
    seat_traces = []
    for seat_name, seat_attributes in seats.items():
        x = ord(seat_name[0]) - ord('A')
        y = int(seat_name[1]) - 1
        r = math.sqrt(3) / 2
        seat_x = (x + (y % 2) * 0.5) * r
        seat_y = y * 1.5
        seat_trace = go.Scatter(
            x=[seat_x],
            y=[seat_y],
            mode='markers',
            marker=dict(
                size=10,
                color=seat_attributes['color']
            ),
            text=seat_name,
            hoverinfo='text'
        )
        seat_traces.append(seat_trace)
    return seat_traces


# Create a selectbox to select a seat
selected_seat = st.selectbox('Select a seat', list(seats.keys()))

# Create a button to change the color of the selected seat
if st.button('Change seat color'):
    # Here you would call the smart contract function to change the color of the seat
    # and update the value of the seat in the dictionary
    seats[selected_seat]['color'] = 'green'
    # Here you would save the updated dictionary to a JSON file

# Create a graph that shows the grid of seats
st.plotly_chart(go.Figure(data=create_seat_grid()))
