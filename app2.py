# Streamlit integrated Image Library
from PIL import Image
import streamlit as st
from streamlit.components.v1 import html

# import plotly graph_objs library to draw the seating arrangements and define each seat individually
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt


# Initial Layout Mode to Wide (For Concert Hall Render to Fit Screen) -> Must be the first called Streamlit command
# Main Streamlit Page Configuration
st.set_page_config(page_title="Buttons Grid",
                   page_icon=":guardsman:", layout="wide")


# Set app.py streamlit custom color scheme
primary_color = "#0000FF"
secondary_color = "#010C80"
text_color = "#000000"
background_color = "#FFFFFF"

# Main Logo Addition Function


def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo


# Sidebar Main Logo Image
st.sidebar.image(
    add_logo(logo_path="tickETHolder_logo.png", width=500, height=500))


# Create sidebar for customer form submission
with st.sidebar:
    # Top header section
    st.markdown("<p style='color: white; padding: 0; margin-top: 0px;'>ticket purchase form:</p>",
                unsafe_allow_html=True)
    # text_input for customer info
    first_name_input = st.text_input(
        label="", placeholder="first name")
    last_name_input = st.text_input(
        label="", placeholder="last name")
    # Drop down for eth wallet addresses from customer
    wallet_addresses = ["0x1b1fA7D8fA78Cf9A1658f06D0345ab8Bdc47CBE7",
                        "0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf",
                        "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"]
    st.markdown("<p style='color: white; padding: 0; margin-top: 0px;'>select eth wallet:</p>",
                unsafe_allow_html=True)
    selected_address = st.selectbox(
        "", wallet_addresses)

    # company copyright info at bottom of sidebar
    for i in range(15):
        st.write("")
    st.markdown("<p style='color: white; font-size: 10px; margin-top: 10px;'>Copyright ©2023 tickETHolder.streamlit.app. All rights reserved.</p>",
                unsafe_allow_html=True)

# Create columns for holding & centering the gallery layout
col1, col2 = st.columns([3, 1], gap="medium")

# Create an empty list to store the scatter traces (in a gallery of seats)
# traces = []
gallery = []

# Create loop to iterate through all the seats in the gallery by their x & y co-ordinates (*original revert back to x=15, y=25 for range)
for x in range(57):
    for y in range(28):
        # Create a scatter trace for the current seat (seat = trace)
        seat = go.Scatter(
            x=[x],  # x-coordinate of the seat
            y=[y],  # y-coordinate of the seat
            mode='markers',  # set the trace type to markers (points)
            # set the marker properties (size and color)
            marker=dict(size=6, color='#010C80')
        )
        # Append the trace to the list of traces
        gallery.append(seat)

# Create a layout for the plot
layout = go.Layout(
    title='Section: Massey Hall (Gallery Level)',
    xaxis=dict(title='X-coordinate',
               autorange=True, showgrid=None, gridcolor=None, showticklabels=False, visible=False),
    yaxis=dict(title='Y-coordinate',
               autorange=True, showgrid=None, gridcolor=None, showticklabels=False, visible=False),
    showlegend=True,
    legend=dict(itemclick="toggleothers"),
    annotations=[
        dict(
            text='STAGE',
            x=28,
            y=-2.5,
            xanchor='center',
            yanchor='top',
            showarrow=False,
        )
    ],
    font=dict(
        family='monospace',
        size=24,
        color='black'
    )

)

# Original 'range' values for xaxis and yaxis = range=[-5, 20]

# Create a figure from the gallery list and layout
fig = go.Figure(data=gallery, layout=layout)
fig.update_layout(autosize=True, width=500, height=650)


# Renaming all legends from trace0, trace1, etc. to seat0, seat1: [trace -> seat]
# Where new_names is the list of names (i.e. gallery names)

def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
        fig.data[i].name = new_name


# Create seat_options list (each will have format 'Seat 0, Seat 1, etc. -> 'Seat [i]')
# The seat_options list has the final sequentially ordered list of seating based on the index gallery length
seat_options = [f'Seat {i}' for i in range(len(gallery))]
# Keep a second seat_index for utility if required
seat_index = [i for i in range(len(gallery))]
# Call the custom_legend_name function
custom_legend_name(seat_options)
fig.update_traces(textposition='top center')

# Show concert_layout header
with col1:
    st.header("Venue: Massey Hall")

# Show the concert_layout (plot) in the main streamlit body
with col1:
    concert_layout = st.plotly_chart(fig, use_container_width=True, height=800)


# Introduce a st.selectbox in order to create a dropdown menu to edited each seat (whether bought or sold) (as a 'trace' obj)
# seat_options = [f'Seat {i}' for i in range(len(gallery))]
with col1:
    selected_seat = st.selectbox('Purchase seat (ticket):', seat_options)

# Use st.button to change color of selected_seat to indicate whether bought or sold
with col1:
    if st.button('Choose seat'):
        concert_layout.update_trace(marker=dict(color='green'),
                                    selectedpoints=[
            int(selected_seat.split(" ")[1])]
        )

# Massey Hall History (Text)
with col2:
    st.header("About Us:")
    st.write("Contact Info:")
    st.write("Phone: 416-555-5555")
    st.write("Email: ticketholder.inquiryinfo@gmail.com")
    st.write("Chatbot Assistant: <Click Here>")
