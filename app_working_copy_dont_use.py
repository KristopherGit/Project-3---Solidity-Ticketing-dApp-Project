# tickETHolder dApp

# Streamlit integrated image library
from PIL import Image
import streamlit as st
import plotly.graph_objs as go
import numpy as np
# Import libraries to run Solidity smart contract & interact with json/files
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
# Import 'requests' to handle json file requests to central JSONbin servers (to update already sold seats that are not available)
import requests
# Import config.py Config JSONbin config info (API Secret Key)
from config import Config
# Import nft_generator() function from nftgen.py
from nftgen import nft_generator
# IMport the ipfsHash generator
from ipfsgen import ipfs_gen
# Import time for sleep delay
import time
# import fernet_cipher as frenciph (Fernet encryption for 'UsePass' built on AES cipher platform)
import fernet_cipher as fernciph
# from bs4 import BeautifulSoup
from bs4 import BeautifulSoup

# Initial Layout Mode to Wide (For Concert Hall Render to Fit Screen) -> Must be the first called Streamlit command
# Main Streamlit Page Configuration
st.set_page_config(page_title="Buttons Grid",
                   page_icon=":guardsman:", layout="wide")


# Set app.py streamlit custom color scheme for config.toml file
# primary_color = "#0000FF"
# secondary_color = "#010C80"
# text_color = "#000000"
# background_color = "#FFFFFF"

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

# tickETHolder Main GUI Streamlit Page Setup
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
        # calculates seat number
        #seat_num = y * 57 + x
        # Create a dictionary for the current seat
        seat = {
            'aisle': x,
            'row': y,
            'name': f'{x},{y}',
            'price': 71000000000000000,
            # 'bought': False,
            'color': '#1E90FF'
            # 'seat_num': seat_num

        }
        # Add the seat to the gallery dictionary
        gallery[seat['name']] = seat


# Create a layout for the plot

layout = go.Layout(
    title='Section: Massey Hall (Gallery Level)',
    xaxis=dict(title='X-coordinate',
               autorange=True, showgrid=None, gridcolor=None, showticklabels=False, visible=False),
    yaxis=dict(title='Y-coordinate',
               autorange=True, showgrid=None, gridcolor=None, showticklabels=False, visible=False, scaleanchor="x",  scaleratio=1),
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

#########################################################

# Pull updated seats color from JSONbin json archive to color sold seats grey downstream

# JSONBin Bin Active URL
url = "https://api.jsonbin.io/v3/b/63e7f171ebd26539d07b9ee0"
# define headers for api request
headers = {"content-type": "application/json",
           "secret-key": Config.JSONBIN_SECRET_KEY,
           "X-Master-Key": '$2b$10$TBShXqVtrokNLIU1b2GD7upkZ7ZV6cgi1gv0rRXYVkS656gRM1tqq'}
response = requests.get(url, headers=headers)
data_json = response.json()


#########################################################

# Create a list of scatter traces to represent the seats in the gallery
traces = []
for seat_number, seat in gallery.items():
    color = '#1E90FF'
    trace = go.Scatter(
        x=[seat['aisle']],
        y=[seat['row']],
        mode='markers',
        marker=dict(size=6, color=color),
        # text=[seat['seat_num']],
        textfont=dict(
            size=20
        )
    )
    traces.append(trace)

#########################################################

# Remove unnecessary traces to shape venue gallery layout

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

# Create stage layout as a half moon trace figure


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

# * modified 02/15/2023


# @st.cache(hash_funcs={list: lambda x: None})
# def rename_traces(traces):
# Initialize a counter for the seat number
#    seat_no = 0
# Iterate through the rows of the gallery
#    for y_coord in range(28):
# Iterate through the columns of the gallery
#        for x_coord in range(57):
# Check if there is a trace with this x and y coordinate
#            trace = next(
#                (t for t in traces if t['x'][0] == x_coord and t['y'][0] == y_coord), None)
#            if trace is not None:
# If there is a trace, rename it with the seat number
#                seat_name = f'Seat {seat_no}'
#                trace['name'] = seat_name
#                # Increment the seat number counter
#                seat_no += 1
# If there is no trace, move on to the next seat without incrementing the seat number counter
#    return traces

def rename_traces(traces):
    # Initialize a counter for the seat number
    seat_no = 0
    # Create a dictionary to store the traces by x and y coordinates
    traces_dict = {(t['x'][0], t['y'][0]): t for t in traces}
    # Iterate through the rows of the gallery
    for y_coord in range(28):
        # Iterate through the columns of the gallery
        for x_coord in range(57):
            # Check if there is a trace with this x and y coordinate
            trace = traces_dict.get((x_coord, y_coord))
            if trace is not None:
                # If there is a trace, rename it with the seat number
                seat_name = f'Seat {seat_no}'
                trace['name'] = seat_name
                # Increment the seat number counter
                seat_no += 1
            # If there is no trace, move on to the next seat without incrementing the seat number counter
    return traces


rename_traces(traces)

# for trace in traces:
#    x_coord = trace['x'][0]
#    y_coord = trace['y'][0]
#    if 0 <= x_coord <= 57 and y_coord <= 1:
#        print(f"x_coord: {x_coord}, y_coord: {y_coord}")
# * modified 02/15/2023


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
#seat_options = [f'Seat {i}' for i in range(len(traces))]
seat_options = []
for trace in traces:
    seat_options.append(trace['name'])
#seat_options = seat_options.sort(key=lambda e: (e is None, e))
# print(seat_options)

# Update recently created seats in venue pulling archived/cached seat_color from session_state that was created on previous run downstream
if st.session_state:
    for seat_name, seat_color in st.session_state.items():
        seat_index = seat_options.index(seat_name)
        traces[seat_index]['marker']['color'] = seat_color
        gallery[list(gallery.keys())[seat_index]]['color'] = seat_color
        gallery[list(gallery.keys())[seat_index]]['bought'] = True

# Plot seating layout
fig = go.Figure(data=traces, layout=layout)

# Create function to update gallery seat names


@st.cache
def custom_legend_name(new_names):
    for i, new_name in enumerate(new_names):
        fig.data[i].name = new_name
        gallery[list(gallery.keys())[i]]['name'] = new_name


# Update original gallery seating names with custom seat_options ('Seat {i}') name for better transparency
custom_legend_name(seat_options)

# Update traces/seats & add stage name
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
# JSON Read/Write to Central Server - To Update Seat Color & Non-Sensitive Info for Data Analysis
#########################################################


def update_jsonbin(ticketId, first_name_input, last_name_input, selected_address, selected_seat):
    # jsonbin url for .json file data
    url = "https://api.jsonbin.io/v3/b/63e7f171ebd26539d07b9ee0"

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

    # check to see if the json bin data was updated correctly by seeing if '200' status code was initiated
    if response.status_code == 200:
        st.write("json data was successfully updated to corresponding JSONbin")
    else:
        st.write("Error updating json data on JSONbin")
        st.write(response.text)


# Implement selectbox dropdown for seat options & when user selects seat name update seats in gallery to new 'color'= 'green' value
with col1:
    selected_seat = st.selectbox('select seat(s):', seat_options)
    if st.button('select seat(s)'):
        seat_index = seat_options.index(selected_seat)
        gallery[list(gallery.keys())[seat_index]]['color'] = '#00FF00'  # green
        st.write("")

        if selected_seat not in st.session_state:
            st.session_state[selected_seat] = gallery[list(
                gallery.keys())[seat_index]]['color'] = '#00FF00'  # green
    if st.button('confirm seat(s)'):
        st.write()

    if st.button('clear all selected seat(s)'):
        st.session_state.clear()

    concert_layout = st.plotly_chart(
        fig, use_container_width=False, height=400, width=1000)

#########################################################
# Right hand side column section of code
#########################################################


with col2:

    # Write selected seat dictionary attributes info to upper right hand corner
    if (selected_seat != 'Seat 0'):
        st.markdown("<p style='color: white; padding: 0; margin-top: 0px;'>selected seat info:</p>",
                    unsafe_allow_html=True)
        st.write(selected_seat)
        seat_index = seat_options.index(selected_seat)
        st.write(gallery[list(gallery.keys())[seat_index]])

    # venue_list
    # st.markdown("<p style='color: white; padding: 0; margin-top: 0px;'>select venue:</p>",
    #            unsafe_allow_html=True)
    venue_list = ["Massey Hall", "Opera House", "Danforth Music Hall", 'Koerner Hall',
                  "The Cameron House", "DROM Taberna", "Lee's Palace", "Roy Thompson Hall", "Horeshoe Tavern"]
    venue_select = st.selectbox("select venue:", venue_list)

    # event_list
    event_list = ["Gorillaz", "Fleetwood Mac",
                  "Bob Dylan", "Phoenix", "The Strokes"]
    event_select = st.selectbox("select event:", event_list)

    # date_select override
    date_select = 1660176000


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
# Create sidebar for customer form submission
with st.sidebar:
    # Top header section
    st.markdown("<p style='color: white; padding: 0; margin-top: 0px;'>ticket purchase form:</p>",
                unsafe_allow_html=True)
    # text_input for customer info
    first_name_input = st.text_input(
        label="first name", placeholder="optional")
    last_name_input = st.text_input(
        label="last name", placeholder="optional")
    # text_input for aes_cipher/hashing ipfsHash data
    usepass_input = st.text_input(
        label="tickETHholder UsePass¹:", placeholder="required")

    # Drop down for eth wallet addresses ('selected_address') from customer
    selected_address = st.selectbox(
        "connect eth wallet", options=wallet_addresses)

    # *** Important conversion ***
    # Convert selected_seat to its tokenId equivalent (where selected_seat = tokenId -1) or in Solidity ticketData struct: seatNumber = ticketId -1

    # Also create a placeholder list for the seat tickets & corresponding ticketIds
    seats_and_ticketIds_list = []

    # Confirm Buy section of code takes selected seats from session_state keys list, strips info to get seat number & convert to (ticketId) (Solidity: tokenId)
    # to interact with contract.functions.<function name> during 'buyTicket()' function process
    # get receipt from buyTicket() Solidity function transaction, create, print & save buy receipt, update JSONbin with seat numbers that were purchased
    # put seat variables into nft_generator function to build .png NFT image with associated event image & applicable qr code based on seat variable info
    # generate IPFS hash / Pinata gateway url
    # update ticket owners IPFS hash address by overwriting blank ipfsHash in their Solidity ticketData[tokenId].ipfsHash attributes
    # print IPFS image urls to sidebar for users to gain access to NFT ticket image

    if st.button("confirm buy:"):
        selected_seats = list(st.session_state.keys())
        print(selected_seats)
        # *New test
        nft_ticket_list = []
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
            nft_filepath = nft_generator(traces, ticketId, event_select,
                                         venue_select, selected_seat)
            print("nft_filepath: ", nft_filepath)
            time.sleep(2)
            ipfsHash_img = ipfs_gen(nft_filepath)
            print("ipfsHash_img URL (pre-encryption):", ipfsHash_img)

            # ****** testing 02/11/23 - usepass hashing

            # encrypted_ipfsHash_img = aes.hash_string(
            #    usepass_input, ipfsHash_img)
            encrypted_ipfsHash_img = fernciph.encrypt_url(
                ipfsHash_img, usepass_input)  # fernet encryption/decryption

            time.sleep(2)
            print("ipfsHash_img byte code (byte): ", encrypted_ipfsHash_img)
            ipfsHash_img_txhash = contract.functions.updateTicketIpfsHashID(ticketId, encrypted_ipfsHash_img).transact(
                {'from': selected_address})  # max gas to spend is 50 gas (50 gwei)
            ipfsHashupdate_receipt = w3.eth.waitForTransactionReceipt(
                ipfsHash_img_txhash)
            st.write("IpfsHash image url updated on buyer's nft:")
            st.write(dict(ipfsHashupdate_receipt))
            nft_ticket_list.append(encrypted_ipfsHash_img)

            # ****** testing 02/11/23 - usepass hashing

        st.sidebar.markdown("<p style='color: orange; font-size: 14px; margin-top: 0px;'>NFT Ticket List: </p>",
                            unsafe_allow_html=True)
        st.sidebar.write(nft_ticket_list)
        print("NFT Ticket List: ", nft_ticket_list)

    # **** testing 02/11/23 encrypt/decrypt nft tickets
    if st.button("retrieve tickets"):
        #decrypted_nft_ticket_list = []
        all_encrypted_ipfsHashes_from_owner = contract.functions.getAllIpfsHashes(
            selected_address).call()
        if len(all_encrypted_ipfsHashes_from_owner) > 0:
            st.markdown("<p style='color: white; padding: 0; margin-top: 0px;'>Viewable NFT Tickets Available:</p>",
                        unsafe_allow_html=True)
            for i in range(len(all_encrypted_ipfsHashes_from_owner)):

                # ipfsHash_decrypted = aes.get_string_from_hash(
                #    usepass_input, all_encrypted_ipfsHashes_from_owner[i])
                ipfsHash_decrypted_url = fernciph.decrypt_url(
                    all_encrypted_ipfsHashes_from_owner[i], usepass_input)
                response_ipfsHash_decrypted_url = requests.get(
                    ipfsHash_decrypted_url)
                print(f"ipfsHash_decrypted_url: {ipfsHash_decrypted_url}")

                if response_ipfsHash_decrypted_url.status_code == 200:
                    soup = BeautifulSoup(
                        response_ipfsHash_decrypted_url.text, 'html.parser')
                    # Go through code & find all links in the html
                    links = soup.find_all('a')
                    # Go though all links and find one with correct file extension
                    for link in links:
                        if '.png' in link.get('href'):
                            # Direct link to the .png file
                            nft_ticket_png_url = link.get('href')
                            break
                    concatenate_url = "https://gateway.pinata.cloud/" + nft_ticket_png_url
                    print("Full url: ", concatenate_url)
                else:
                    print("Error - Unable to retrieve html from url")
                #ipfsHash_decrypted = ipfsHash_decrypted.rstrip("%10")
                #ipfsHash_decrypted = ipfsHash_decrypted.replace("%10", "")
                st.markdown(f"[NFT Ticket {i + 1}]({concatenate_url})")

            # **** testing 02/11/23 encrypt/decrypt nft tickets

            # company copyright info at bottom of sidebar
    for i in range(4):
        st.write("")
    st.markdown("<p style='color: white; font-size: 12px; margin-top: 0px;'>Copyright ©2023 tickETHolder.streamlit.app. All rights reserved.</p>",
                unsafe_allow_html=True)
    # Display contract address to the sidebar for user knowledge/troubleshooting
    if contract is None:
        st.write("Unable to connect to the deployed contract.")
        st.markdown("<p style='color: red; font-size: 16px; margin-top: 0px;'><b>Unable to Connect to ETH Test Network.</b></p>",
                    unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: green; font-size: 16px; margin-top: 0px;'><b>Successfully connected to the deployed contract at address:.</b></p>",
                    unsafe_allow_html=True)
        st.write(contract.address)

#########################################################
