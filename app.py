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


# Shaping Gallery - Removing Middle Row/Column to Create Aisle
# Formula for Removal: gallery.remove(gallery[x*28+y])
# Traces for Massey Gallery floorplan run from 0 to 1595 + 1596 if including stage as a trace obj
# gallery.remove(gallery[x*28+y])
# Define the indices of the seats to remove
#to_remove_1 = [30*28+i for i in range(28)]
# Sort the indices in reverse order to avoid shifting
# to_remove_1.sort(reverse=True)
# Remove the seats from the list
# for index in to_remove_1:
#    gallery.pop(index)


to_remove_2 = [29*28+i for i in range(28)]
# Sort the indices in reverse order to avoid shifting
to_remove_2.sort(reverse=True)
# Remove the seats from the list
for index in to_remove_2:
    gallery.pop(index)

to_remove_3 = [28*28+i for i in range(28)]
# Sort the indices in reverse order to avoid shifting
to_remove_3.sort(reverse=True)
# Remove the seats from the list
for index in to_remove_3:
    gallery.pop(index)

to_remove_4 = [27*28+i for i in range(28)]
# Sort the indices in reverse order to avoid shifting
to_remove_4.sort(reverse=True)
# Remove the seats from the list
for index in to_remove_4:
    gallery.pop(index)


# Create lists to store the seats to be removed

# LH gallery first row seats removal
# first row seats to remove
# seats_to_remove = []
# second row seats to remove
# seats_to_remove = []

# LH gallery triangle corner
# seats_to_remove = [21, 22, 23, 24, 25, 26, 27, 50, 51, 52, 53, 54, 55,
#                   79, 80, 81, 82, 83, 108, 109, 110, 111, 137, 138, 139, 166, 167, 195]

# LH gallery trapezoid section
# seats_to_remove = [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
#                   45, 46, 74, 101, 129, 156, 184, 212, 168, 169, 170, 171, 172, 173, 174, 175,
#                   176, 177, 178, 179, 180, 181, 182, 183, 184, 212, 211, 210, 209, 208, 207
#                   206, 205, 204, 203, 202, 201, 200, 199, 198, 197, 196, 56, 84, 112, 140, 157, 102, 47, 20]

# RH gallery triangle corner
# seats_to_remove = [1505, 1506, 1507, 1508, 1509, 1510, 1511, 1478, 1479, 1480, 1481, 1482, 1483, 1451, 1452, 1453, 1454, 1455, 1424, 1425, 1426, 1427, 1397, 1398, 1399, 1370, 1371, 1343]

# RH gallery trapezoid section
# seats_to_remove = [1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1446, 1417, 1389, 1360, 1332, 1316, 1317, 1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1344 1345, 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357, 1359, 1428, 1400, 1372]

# *** Concatenated List of All Seats to Be Removed ***

seats_to_remove = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 50, 51, 52, 53, 54, 55, 56, 74, 79, 80, 81, 82, 83, 84, 101, 102, 108, 109, 110, 111, 112, 129, 137, 138, 139, 140, 156, 157, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 280, 281, 308, 309, 336, 337, 364, 365, 392, 393, 394, 420, 421, 422, 448, 449, 450, 476, 477, 478, 504, 505, 506, 532, 533, 534, 560, 561, 562, 563, 588, 589, 590, 591, 616, 617, 618, 619, 644, 645, 646, 647, 672, 673, 674, 675, 700, 701, 702, 703, 728, 729, 730, 731, 756, 757, 758, 759, 784, 785, 786, 787, 812, 813, 814, 815, 840, 841,
                   842, 843, 868, 869, 870, 871, 896, 897, 898, 899, 924, 925, 926, 927, 952, 953, 954, 980, 981, 982, 1008, 1009, 1010, 1036, 1037, 1038, 1064, 1065, 1066, 1092, 1093, 1094, 1120, 1121, 1148, 1149, 1176, 1177, 1204, 1205, 1277, 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1316, 1317, 1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1332, 1343, 1344, 1360, 1361, 1370, 1371, 1372, 1389, 1397, 1398, 1399, 1400, 1417, 1418, 1424, 1425, 1426, 1427, 1428, 1446, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1478, 1479, 1480, 1481, 1482, 1483, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511]

# Remove the seats from the gallery
for i in reversed(seats_to_remove):
    gallery.pop(i)


# end of gallery trimming/shaping
# -----------------

# ADDING STAGE IS A BETA TEST

# Create stage layout as a half moon
# Create a scatter trace for the stage
stage = go.Scatter(
    x=list(range(57)),
    y=([-2.5, -3, -3.5] + [-4]*(57-6) + [-3.5, -3, -2.5]),
    mode='lines',
    fill='toself',
    line=dict(width=2, color='darkgrey'),
    fillcolor='lightgrey',
    text=['STAGE'],
    textposition='bottom center',
    textfont=dict(color='black')  # set the text color to white
)

# Append the stage trace to the list of traces
gallery.append(stage)

# Update stage formatting
stage.update(fill='toself', fillcolor='lightgrey')


# ***** ADDING STAGE IS A BETA TEST

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
