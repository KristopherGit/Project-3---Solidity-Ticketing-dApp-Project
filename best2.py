# Works DO NOT ALTER THIS IS THE BEST TRIAL VERSION YET (SEE TEXT BELOW FOR INTERACTION WITH ETHEREUM SMART CONTRACT)
# Streamlit integrated Image Library
from PIL import Image
import streamlit as st
import plotly.graph_objs as go
import numpy as np


#########################################################

# Import libraries to run Solidity smart contract & interact with json/files
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv

#########################################################

# Import 'requests' to handle json file requests to central JSONbin servers (to update already sold seats that are not available)
import requests

# Import config.py Config JSONbin config info (API Secret Key)
from config import Config

# Import Moralis API_KEYS (for NFT IPFS Storage)
from api_keys import MORALIS_API_KEY

# Initial Layout Mode to Wide (For Concert Hall Render to Fit Screen) -> Must be the first called Streamlit command
# Main Streamlit Page Configuration

st.set_page_config(page_title="Buttons Grid",
                   page_icon=":guardsman:", layout="wide")


# Set app.py streamlit custom color scheme for config.toml file
primary_color = "#0000FF"
secondary_color = "#010C80"
text_color = "#000000"
background_color = "#FFFFFF"

#########################################################

# Web3 Contract Loading & Execution

# load dotenv
load_dotenv()

# Define and connect to a Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Implement the contract helper function
# a.) Loads the contract only once using the streamlit cache feature
# b.) Connects to the contract once using the contract address & ABI


@st.cache(allow_output_mutation=True)
# Load the contract ABI
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/ticketholder_abi.json')) as f:
        ticketholder_abi = json.load(f)

    # Set the contract address (Ethereum address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=ticketholder_abi
    )

    return contract


# Load the ticketholder Ethereum contract
contract = load_contract()

#########################################################

# TickETHolder Main GUI Streamlit Page Setup
# Main Logo Addition Function


@st.cache
def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo


# Sidebar Main Logo Image
st.sidebar.image(
    add_logo(logo_path="tickETHolder_logo.png", width=500, height=500))

#########################################################

# Setup access to user Ethereum eth.accounts (MetaMask)
wallet_addresses = w3.eth.accounts


# Create sidebar for customer form submission
# with st.sidebar:
#    # Top header section
#    st.markdown("<p style='color: white; padding: 0; margin-top: 0px;'>ticket purchase form:</p>",
#                unsafe_allow_html=True)
#    # text_input for customer info
#    first_name_input = st.text_input(
#        label="first name", placeholder="required")
#    last_name_input = st.text_input(
#        label="last name", placeholder="required")
#
# Drop down for eth wallet addresses from customer
# wallet_addresses = ["0x1b1fA7D8fA78Cf9A1658f06D0345ab8Bdc47CBE7",
#                    "0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf",
#                    "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"]
# st.markdown("<p style='color: white; padding: 0; margin-top: 0px;'>select eth wallet:</p>",
#            unsafe_allow_html=True)
#    selected_address = st.selectbox(
#        "connect eth wallet", options=wallet_addresses)
#
#    if st.button("confirm buy:"):
#        tx_hash = contract.functions.buyTicket(
#            ticketId, first_name_input, last_name_input).transact({'from': selected_address})
#
#    # company copyright info at bottom of sidebar
#    for i in range(10):
#        st.write("")
#    st.markdown("<p style='color: white; font-size: 12px; margin-top: 0px;'>Copyright ©2023 tickETHolder.streamlit.app. All rights reserved.</p>",
#                unsafe_allow_html=True)


# Create columns for holding & centering the gallery layout
col1, col2 = st.columns([3, 1], gap="medium")

# Show concert_layout header
with col1:
    st.header("Venue: Massey Hall")

# Create a dictionary that holds the attributes of each seat but first reference it with session_state seats already coded
"st.session_state object:", st.session_state

# Create a dictionary for the gallery with seat names as keys and seat dictionaries as values
gallery = {}

# Instantiate each seat in a for-loop for each x,y-coord with attributes including: {x, y, name, price, bought=<boolean>, color=<#010C80>, owner_hash=address}
for x in range(57):
    for y in range(28):
        # Create a dictionary for the current seat
        seat = {
            'aisle': x,
            'row': y,
            'name': f'{x},{y}',
            'price': 71000000000000000,
            # 'bought': False,
            'color': '#1E90FF'
        }
        # Add the seat to the gallery dictionary
        gallery[seat['name']] = seat


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
        size=32,
        color='black'
    )
)
#print("Gallery dictionary")
#print("Index, key/value pairs:")
# print()
# for index, (key, value) in enumerate(gallery.items()):
#    print("Index:", index)
#    print("Key:", key)
#    print("Value:", value)

#########################################################

# Create & Call 'update_seat_colors' function that pulls updated seat colors from JSONbin based on sold seats

# JSONBin Bin Active URL
url = "https://api.jsonbin.io/v3/b/63e159c5c0e7653a0570f1d5"
# define headers for api request
headers = {"content-type": "application/json",
           "secret-key": Config.JSONBIN_SECRET_KEY,
           "X-Master-Key": '$2b$10$TBShXqVtrokNLIU1b2GD7upkZ7ZV6cgi1gv0rRXYVkS656gRM1tqq'}
response = requests.get(url, headers=headers)
data_json = response.json()


#########################################################

# Create a list of scatter traces to represent the seats in the gallery
# Create a list of scatter traces to represent the seats in the gallery
traces = []
for seat_number, seat in gallery.items():
    color = '#1E90FF'
    trace = go.Scatter(
        x=[seat['aisle']],
        y=[seat['row']],
        mode='markers',
        marker=dict(size=6, color=color),
        textfont=dict(
            size=20
        )
    )
    traces.append(trace)


#########################################################

#traces = []
# for seat in gallery.values():
    # Create a scatter trace for the current seat
    # trace = go.Scatter(
    #   x=[seat['aisle']],
    #   y=[seat['row']],
    #   mode='markers',
    #   marker=dict(size=6, color=seat['color']),
    #   textfont=dict(
    #       size=20
    #  )
    # )
    # Append the trace to the list of traces
    # traces.append(trace)

to_remove_2 = [29*28+i for i in range(28)]
# Sort the indices in reverse order to avoid shifting
to_remove_2.sort(reverse=True)
# Remove the seats from the list
for index in to_remove_2:
    traces.pop(index)

to_remove_3 = [28*28+i for i in range(28)]
# Sort the indices in reverse order to avoid shifting
to_remove_3.sort(reverse=True)
# Remove the seats from the list
for index in to_remove_3:
    traces.pop(index)

to_remove_4 = [27*28+i for i in range(28)]
# Sort the indices in reverse order to avoid shifting
to_remove_4.sort(reverse=True)
# Remove the seats from the list
for index in to_remove_4:
    traces.pop(index)

seats_to_remove = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 50, 51, 52, 53, 54, 55, 56, 74, 79, 80, 81, 82, 83, 84, 101, 102, 108, 109, 110, 111, 112, 129, 137, 138, 139, 140, 156, 157, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 280, 281, 308, 309, 336, 337, 364, 365, 392, 393, 394, 420, 421, 422, 448, 449, 450, 476, 477, 478, 504, 505, 506, 532, 533, 534, 560, 561, 562, 563, 588, 589, 590, 591, 616, 617, 618, 619, 644, 645, 646, 647, 672, 673, 674, 675, 700, 701, 702, 703, 728, 729, 730, 731, 756, 757, 758, 759, 784, 785, 786, 787, 812, 813, 814, 815, 840, 841,
                   842, 843, 868, 869, 870, 871, 896, 897, 898, 899, 924, 925, 926, 927, 952, 953, 954, 980, 981, 982, 1008, 1009, 1010, 1036, 1037, 1038, 1064, 1065, 1066, 1092, 1093, 1094, 1120, 1121, 1148, 1149, 1176, 1177, 1204, 1205, 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1316, 1317, 1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1332, 1343, 1344, 1360, 1361, 1370, 1371, 1372, 1389, 1397, 1398, 1399, 1400, 1417, 1418, 1424, 1425, 1426, 1427, 1428, 1446, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1478, 1479, 1480, 1481, 1482, 1483, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511]

# Remove the seats from the gallery
for i in reversed(seats_to_remove):
    traces.pop(i)

# Create stage layout as a half moon
# Create a scatter trace for the stage
# stage = go.Scatter(
#    x=list(range(57)),
#    y=([-2.5, -3, -3.5] + [-4]*(57-6) + [-3.5, -3, -2.5]),
    # x=list(range(57))[::-1],
    # y=[-2.5, -3, -3.5] + [-4.5]*(57-6) + [-3.5, -3, -2.5],
#    mode='lines',
#    fill='toself',
#    line=dict(width=2, color='darkgrey'),
#    fillcolor='lightgrey',
#    text=['STAGE'],
#    textposition='bottom center',
#    textfont=dict(color='black')  # set the text color to white
# )


def stage_y_values(x):
    return 6 * np.sin(x * np.pi / 56) - 4


x = np.array(list(range(57)))
y = stage_y_values(x)

stage = go.Scatter(
    x=x,
    y=y,
    mode='lines',
    fill='toself',
    line=dict(width=4, color='#333333'),
    fillcolor='#333333',
    text=['STAGE'],
    textposition='top center',
    textfont=dict(color='white')  # set the text color to white
)


# Append the stage trace to the list of traces
traces.append(stage)

# Update stage formatting
stage.update(fill='toself', fillcolor='#333333',
             line=dict(width=4, color='#333333'))

# Add a contour line to the bottom of the half-moon stage outline
bottom_line = go.Scatter(
    x=list(range(57)),
    y=[min(y) for i in range(57)],
    mode='lines',
    line=dict(width=2, color='#333333'),
)

# Append the bottom line trace to the list of traces
traces.append(bottom_line)

#########################################################

# Resort gallery layout sequentially

# Create an array of seat positions

#########################################################

# Update traces to color ones 'darkgrey' that appear in the 'ticketholders' JSONbin json server
# for index, trace in enumerate(traces):
#    print(f"index: {index}, trace: {trace}")


if 'record' in data_json and 'ticketholder' in data_json['record']:
    ticketholders = data_json['record']['ticketholder']
    for ticketholder in ticketholders[1:]:
        for index, trace in enumerate(traces):
            token_id = str(ticketholder['tokenID'])
            if token_id.isdigit() and int(token_id) - 1 == index:
                trace['marker']['color'] = 'darkgrey'
#########################################################

# Create a list of seats as 'Seat {i}' corresponding to each i in traces list
seat_options = [f'Seat {i}' for i in range(len(traces))]

if st.session_state:
    for seat_name, seat_color in st.session_state.items():
        seat_index = seat_options.index(seat_name)
        traces[seat_index]['marker']['color'] = seat_color
        gallery[list(gallery.keys())[seat_index]]['color'] = seat_color
        gallery[list(gallery.keys())[seat_index]]['bought'] = True

fig = go.Figure(data=traces, layout=layout)


def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
        fig.data[i].name = new_name
        gallery[list(gallery.keys())[i]]['name'] = new_name


custom_legend_name(seat_options)

fig.update_traces(textposition='top center')
fig.update_layout(autosize=True, width=950, height=600, annotations=[
    dict(
        text="S T A G E",
        font=dict(
            size=24,
            family='monospace',
            color='black'
        ),
        y=0.25
    )
], hoverlabel=dict(
    font=dict(
        size=20,
        color="white"
    )
))

#########################################################

### ***Select & Purchase Ticket Algorithms*** ###
# Includes python functions to interact with Solidity TickETHolder contract in the 'ticketholder.sol' file

# St.Selectbox - Selectbox dropdown for seat selection options

# with col1:
# selected_seat = st.selectbox('Purchase seat (ticket):', seat_options)

# St.Button - Confirm Seat With Session_State Gallery{key:"seat_name(x,y)" value:"seat(dic)"}

# Generate a placeholder list for holding seats for the customer
#selected_seats_list = []

#########################################################
# JSON Read/Write to Central Server - To Update Seat Color & Non-Sensitive Info for Data Analysis
#########################################################


def update_jsonbin(ticketId, first_name_input, last_name_input, selected_address, selected_seat):
    # jsonbin url for .json file data
    url = "https://api.jsonbin.io/v3/b/63e159c5c0e7653a0570f1d5"

    # define headers for api request
    headers = {"content-type": "application/json",
               "secret-key": Config.JSONBIN_SECRET_KEY,
               "X-Master-Key": '$2b$10$TBShXqVtrokNLIU1b2GD7upkZ7ZV6cgi1gv0rRXYVkS656gRM1tqq'}

    # retrieve most recent json from JSONbin
    response = requests.get(url, headers=headers)
    data = response.json()

    if "record" in data:
        data = data["record"]

    if "ticketholder" not in data:
        data["ticketholder"] = []

    ticket_id = ticketId
    counter = 0
    while any(d['tokenID'] == ticket_id for d in data["ticketholder"]):
        counter += 1
        ticket_id = f"{ticketId}_{counter}"

    # Access the row & aisle values from each trace (seat) that corresponds to each tokenId/seat number
    aisle = traces[ticket_id - 1]['x'][0]
    row = traces[ticket_id - 1]['y'][0]

    data["ticketholder"].append({
        "tokenID": ticket_id,
        "first_name": first_name_input,
        "last_name": last_name_input,
        "selected_address": selected_address,
        "seat_color": "#1E90FF",  # default blue/unsold
        "selected_seat": selected_seat,
        "aisle": aisle,
        "row": row
    })

    # send put request to jsonbin to update the json data
    response = requests.put(url, headers=headers, json=data)

    # check if request was successful
    if response.status_code == 200:
        st.write("json data was successfully updated to corresponding JSONbin")
    else:
        st.write("Error updating json data on JSONbin")
        st.write(response.text)


with col1:
    selected_seat = st.selectbox('select seat(s):', seat_options)
    if st.button('select seat(s)'):
        seat_index = seat_options.index(selected_seat)
        gallery[list(gallery.keys())[seat_index]]['color'] = '#00FF00'  # green
        st.write("")

        # if selected_seat:
        #    selected_seats_list.append(selected_seat)

        if selected_seat not in st.session_state:
            st.session_state[selected_seat] = gallery[list(
                gallery.keys())[seat_index]]['color'] = '#00FF00'  # green
    if st.button('confirm seat(s)'):
        st.write()

    if st.button('clear all selected seat(s)'):
        st.session_state.clear()

    concert_layout = st.plotly_chart(
        fig, use_container_width=False, height=400, width=1000)

    # Create sidebar for customer form submission
with st.sidebar:
    # Top header section
    st.markdown("<p style='color: white; padding: 0; margin-top: 0px;'>ticket purchase form:</p>",
                unsafe_allow_html=True)
    # text_input for customer info
    first_name_input = st.text_input(
        label="first name", placeholder="required")
    last_name_input = st.text_input(
        label="last name", placeholder="required")

    # Drop down for eth wallet addresses ('selected_address') from customer
    selected_address = st.selectbox(
        "connect eth wallet", options=wallet_addresses)

    # *** Important conversion ***
    # Convert selected_seat to its tokenId equivalent (where selected_seat = tokenId -1) or in Solidity ticketData struct: seatNumber = ticketId -1

    # Also create a placeholder list for the seat tickets & corresponding ticketIds
    seats_and_ticketIds_list = []

    # for selected_seat in selected_seats_list:
    #    seat_string_stripped_list = selected_seat.split(" ")
    #    # print(seat_string_stripped_list)
    #    seat_num_stripped = int(seat_string_stripped_list[1])
    #    # print(seat_num_stripped)
    #    ticketId = seat_num_stripped + 1
    #    # print("ticket_Id:")
    # print(ticketId)
    # print("selected_address:")
    # print(selected_address)
    #    if (selected_seat, ticketId):
    #        seats_and_ticketIds_list.append((selected_seat, ticketId))

    # print(seats_and_ticketIds_list)

    if st.button("confirm buy:"):
        selected_seats = list(st.session_state.keys())
        print(selected_seats)
        for selected_seat in selected_seats:
            seat_string_stripped_list = selected_seat.split(" ")
            seat_num_stripped = int(seat_string_stripped_list[1])
            ticketId = seat_num_stripped + 1
            tx_hash = contract.functions.buyTicket(
                ticketId, first_name_input, last_name_input).transact({'from': selected_address, 'value': 71000000000000000})
            receipt = w3.eth.waitForTransactionReceipt(tx_hash)
            st.write("Transaction receipt mined:")
            st.write(dict(receipt))
            update_jsonbin(ticketId, first_name_input,
                           last_name_input, selected_address, selected_seat)
            # check if request was successful
            # data = requests.get(
            #    url='https://api.jsonbin.io/v3/b/63dcac6fc0e7653a056dc7ab').json()

    # company copyright info at bottom of sidebar
    for i in range(8):
        st.write("")
    st.markdown("<p style='color: white; font-size: 12px; margin-top: 0px;'>Copyright ©2023 tickETHolder.streamlit.app. All rights reserved.</p>",
                unsafe_allow_html=True)

#########################################################
# Right hand side column section of code
#########################################################


def show_venue_contact_info():
    with col2:

        if (selected_seat != 'Seat 0'):
            st.markdown("<p style='color: white; padding: 0; margin-top: 0px;'>selected seat info:</p>",
                        unsafe_allow_html=True)
            st.write(selected_seat)
            seat_index = seat_options.index(selected_seat)
            st.write(gallery[list(gallery.keys())[seat_index]])

        # st.markdown("<p style='color: white; padding: 0; margin-top: 0px;'>select venue:</p>",
        #            unsafe_allow_html=True)
        venue_list = ["Massey Hall", "Opera House", "Danforth Music Hall", 'Koerner Hall',
                      "The Cameron House", "DROM Taberna", "Lee's Palace", "Roy Thompson Hall", "Horeshoe Tavern"]
        st.selectbox("select venue:", venue_list)

    # Creating spacing between seat seat info summary and contact info

    with col2:

        for i in range(3):
            st.write("")

        # Venue Image
        venue_image = Image.open('massey_hall_bw.png')
        st.image(venue_image, 'Massey Hall - North Entrance')

        # Title for Option to Select Venue Seating Area View
        st.markdown("<p style='color: white; padding: 0; margin-top: 0px;'>seating map section:</p>",
                    unsafe_allow_html=True)

        # Option for Selecting Gallery View
        gallery_1 = st.button("Gallery View")

        # Option for Selecting Balcony View
        gallery_1 = st.button("Balcony View")

        # Contact info
        # st.header("About Us:")
        st.markdown("<p style='color: white; font-size: 18px; margin-top: 0px;'>Contact Info:</p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>Phone: 416-555-5555</p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>Email: tickETHolder.info@gmail.com</p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>Chatbot Assistant: (Click Here)</p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size: 12px; margin-top: 0px;'>Developed on Remix IDE. Powered by Web3. All rights reserved.</p>",
                    unsafe_allow_html=True)

#########################################################


show_venue_contact_info()

#########################################################

#########################################################
# Print data to terminal for troubleshooting
# print("gallery.items()")

# for i, (key, value) in enumerate(gallery.items()):
#    if i == 200:
#        break
#    print(f"{key}: {value}")
#########################################################

# Appendix / Misc. Notes
# i.) QR Code Venue/Event Enter Format [Based on Solidity Variable/Call Format] (https://www.qr-code-generator.com/)
# use (https://pixlr.com/x/#editor) to piece NFT image together. Put into
# i.e. (Gorillaz Concert Event)
# bandName = Gorillaz
# uint concertDate = 08/10/2023 @ 8:00pm
# venueName = Massey Hall
# uint seatNumber = 07
