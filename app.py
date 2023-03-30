# tickETHolder dApp

# Streamlit integrated image library
from PIL import Image
import streamlit as st  # Note: Requires Version: 1.17.0
# Note: Requires Version 4.14.3 to run without dedacted errors
import plotly.graph_objs as go
import numpy as np
# Import libraries to run Solidity smart contract & interact with json/files
import os
import json
from web3 import Web3  # Note: Requires Version: 5.31.3
from pathlib import Path
from dotenv import load_dotenv
# Import 'requests' to handle json file requests to central JSONbin servers (to update already sold seats that are not available)
import requests  # Note: Requires Version: 2.28.1
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
# Import gallery, balcony, mezzanine section from venues
import venues as ven
# Import minter_nft_gen.py program
#from minter_nft_gen import obtain_all_venues_for_event, obtain_date_for_event_venue, obtain_date_string_for_event_venue

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
#w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI"),
          request_kwargs={'timeout': 35}))

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
    add_logo(logo_path="Image_Data/tickETHolder_logo.png", width=550, height=550))

#########################################################

# Setup access to user Ethereum eth.accounts (MetaMask)
wallet_addresses = w3.eth.accounts

# Create columns for holding & centering the gallery layout
col1, col2 = st.columns([4, 1], gap="small")

# Create col2 right hand side event, venue & date selector that determines the venue & sections to be imported
# access event_dictionary master events list to compile unique events, venues, dates & associated JSONbin info

with col2:
    with open("json/event_dictionary.json", "r") as file:
        data = json.load(file)
        eventListValue = data.get("eventList", [])
        print("eventList values:", eventListValue)
        masterEventsList = list(
            set(value["eventName"] for value in eventListValue))
        masterEventsList.sort()
        print("masterEventsList:", masterEventsList)

    # event_list
    # event_list = ["Gorillaz", "Fleetwood Mac",
    #               "Bob Dylan", "Phoenix", "The Strokes"]
    # event_select = st.selectbox("select event:", event_list)
    _eventName = st.selectbox("select event:", masterEventsList)

    # function to fetch all venues for a particular eventName
    @st.cache(allow_output_mutation=True)
    def obtain_all_venues_for_event(eventName):
        with open("json/event_dictionary.json", "r") as file:
            data = json.load(file)
            # if not isinstance(data, list):
            eventList = data["eventList"]
            venues = list(
                set(value["venueName"] for value in eventList if value['eventName'] == eventName))
            venues.sort()
            return venues

    # function for obtaining all possible venues for a unique event (each 'event' is a dictionary structure and are entered in list format where the entirety of the list is a value corresponding to the "eventList" key name)
    masterVenuesList = obtain_all_venues_for_event(_eventName)

    # _venueName variable represents selectbox list choice of all possible unique events available for one event
    _venueName = st.selectbox("select venue:", masterVenuesList)

    # function to fetch all dates for a particular event & venue combination
    @st.cache(allow_output_mutation=True)
    def obtain_date_string_for_event_venue(_eventName, _venueName):
        with open("json/event_dictionary.json", "r") as file:
            data = json.load(file)
            eventList = data["eventList"]
            dates = list(
                set(value["dateTime"] for value in eventList if value["venueName"] == _venueName and value["eventName"] == _eventName))
            dates.sort()
            return dates

    # function for obtaining all possible concert dates (UNIX format) for a unique event (_eventName) at a specific venue (_venueName)
    masterDatesList = obtain_date_string_for_event_venue(
        _eventName, _venueName)

    # _concertDate variable represents selectbox list choice of all dates pertaining to the above _venueName (and hence, _eventName)
    _concertDate = st.selectbox("select event date:", masterDatesList)

    # retrieve the "unique_id" based on unique "_eventName", "_venueName" and "_concertDate"
    @st.cache(allow_output_mutation=True)
    def obtain_unique_id(_eventName, _venueName, _concertDate):
        with open("json/event_dictionary.json", "r") as file:
            data = json.load(file)
            eventList = data["eventList"]
            uniqueids = list(set(value["unique_id"] for value in eventList if value["eventName"] ==
                             _eventName and value["venueName"] == _venueName and value["dateTime"] == _concertDate))
            return uniqueids

    # retrieve "_uniqueIdList" for "unique_id" then retrieve what should be the only item in the list at index 0
    _uniqueIdList = obtain_unique_id(_eventName, _venueName, _concertDate)
    print("_uniqueIdList: ", _uniqueIdList)
    _uniqueId = _uniqueIdList[0]
    print("_uniqueId: ", _uniqueId)

    # function that will fetch the 'seat JSONbin url' that corresponds to its associated _eventName, _venueName & _concertDate above

    @st.cache(allow_output_mutation=True)
    def obtain_seat_json_for_event(_eventName, _venueName, _concertDate):
        with open("json/event_dictionary.json", "r") as file:
            data = json.load(file)
            eventList = data["eventList"]
            jsonBinURL = list(set(value["seatJSONBinURL"] for value in eventList if value["eventName"]
                              == _eventName and value["venueName"] == _venueName and value["dateTime"] == _concertDate))
            return jsonBinURL

    # _jsonBinURL variable represents selectbox list choice of JSONbin URL pertaining to the above associated _eventName, _venueName & _concertDate
    _jsonBinURLList = obtain_seat_json_for_event(
        _eventName, _venueName, _concertDate)

    # get the first (and should be only) JSONBin json url address to read/write to the concert venue seat purchased memory
    _jsonBinURL = _jsonBinURLList[0]

    # print("_jsonBinURL:", _jsonBinURL)
    # print(type(_jsonBinURL))

    # function that will generate a list of available seating sections for the specific venue selected above
    @st.cache(allow_output_mutation=True)
    def obtain_venue_section(_venueName):
        with open("json/venues_dictionary.json", "r") as file:
            data = json.load(file)
            #venue_list = list(data.keys())
            if _venueName in data.keys():
                section_name_list = list(data[_venueName].keys())
                section_function_list = list(data[_venueName].values())
                section_dictionary = dict(
                    zip(section_name_list, section_function_list))
                return section_dictionary  # section_name_list#, section_function_list
            else:
                return []

    # function for obtaining all possible sections pertaining to the above _venueName
    masterSectionDict = obtain_venue_section(_venueName)

    # _sectionName variable represents selectbox list choice of all sections pertaining to the corresponding _venueName input
    _sectionName = st.selectbox(
        "seating map section:", masterSectionDict.keys())
    # print(_sectionName)

    # connect to and populate the venue.py saved venue layouts to create visual representation of available & purchased seats for the above chosen _venueName (as a function of _eventName)
    # print(masterSectionDict[_sectionName])
    # print(type(masterSectionDict[_sectionName]))

    sectionFunctionNameString = masterSectionDict[_sectionName]
    # print("sectionFunctionNameString", sectionFunctionNameString)

    venueSectionFunctionName = getattr(ven, sectionFunctionNameString)
    # print(type(venueSectionFunctionName))

# Show concert_layout header
with col1:
    # st.header("tickETHolder")
    st.markdown("<p style='color: #B3A301; font-size: 24px; margin-top: 0px;'><b>tickETHolder™</b></p>",
                unsafe_allow_html=True)

# Create a dictionary that holds the attributes of each seat but first reference it with session_state seats already coded
#"st.session_state object:", st.session_state

# Import gallery & traces from venues.py as venue_massey_hall
# gallery, traces = ven.create_venue_massey_hall_gallery()
try:
    gallery, traces = venueSectionFunctionName()
    #print("gallery:", gallery)
    #print("traces:", traces)
except:
    st.markdown("<p style='color: #B3A301; font-size: 16px; margin-top: 0px;'><b>Venue section under construction. Please check back.</b></p>",
                unsafe_allow_html=True)
    image = Image.open('Image_Data/under_construction.jpeg')
    st.image(image, caption='Maintenance underway.')
    gallery, traces = {}, []


# print("from venues.py import gallery:")
# print(gallery)
# print("from venues.py import traces: ")
# print(traces)


# # Create a dictionary for the gallery with seat names as keys and seat dictionaries as values
# gallery = {}

# # Instantiate each seat in a for-loop for each x,y-coord with attributes including: {x, y, name, price, bought=<boolean>, color=<#010C80>, owner_hash=address}
# for x in range(57):
#     for y in range(28):
#         # Create a dictionary for the current seat
#         seat = {
#             'aisle': x,
#             'row': y,
#             'name': f'{x},{y}',
#             'price': 71000000000000000,
#             # 'bought': False,
#             'color': '#1E90FF'
#         }
#         # Add the seat to the gallery dictionary
#         gallery[seat['name']] = seat


# Create a layout for the plot
@st.cache(allow_output_mutation=True)
def concert_layout(gallery):
    largest_x_value = max(seat['x'] for seat in gallery.values())
    center_x_value = largest_x_value/2
    layout = go.Layout(
        title=dict(text=str(_sectionName),
                   font=dict(
                       family='monospace',
                       color='#B3A301'
        )
        ),
        xaxis=dict(title='X-coordinate',
                   autorange=True, showgrid=None, gridcolor=None, showticklabels=False, visible=False),
        yaxis=dict(title='Y-coordinate',
                   autorange=True, showgrid=None, gridcolor=None, showticklabels=False, visible=False),
        showlegend=False,
        legend=dict(itemclick="toggleothers"),
        annotations=[
            dict(
                text='STAGE',
                # x=center_x_value,
                # y=-2.5,
                # xanchor='center',
                # yanchor='top',
                showarrow=False,
            )
        ],
        font=dict(
            family='monospace',
            size=32,
            color='black'
        )
    )
    return layout


layout = concert_layout(gallery)

#########################################################

# Pull updated seats color from JSONbin json archive to color sold seats grey downstream

# JSONBin Bin Active URL
# url = "https://api.jsonbin.io/v3/b/63efe266c0e7653a057997d1"
url = _jsonBinURL
# define headers for api request
headers = {"content-type": "application/json",
           "secret-key": Config.JSONBIN_SECRET_KEY,
           "X-Master-Key": '$2b$10$TBShXqVtrokNLIU1b2GD7upkZ7ZV6cgi1gv0rRXYVkS656gRM1tqq'}
response = requests.get(url, headers=headers)
data_json = response.json()


#########################################################

# # Create a list of scatter traces to represent the seats in the gallery
# traces = []
# for seat_number, seat in gallery.items():
#     color = '#1E90FF'
#     trace = go.Scatter(
#         x=[seat['aisle']],
#         y=[seat['row']],
#         mode='markers',
#         marker=dict(size=6, color=color),
#         textfont=dict(
#             size=20
#         )
#     )
#     traces.append(trace)

# #########################################################

# # Remove unnecessary traces to shape venue gallery layout

# to_remove_2 = [29*28+i for i in range(28)]
# # Sort the indices in reverse order to avoid shifting
# to_remove_2.sort(reverse=True)
# # Remove the seats from the list
# for index in to_remove_2:
#     traces.pop(index)

# to_remove_3 = [28*28+i for i in range(28)]
# # Sort the indices in reverse order to avoid shifting
# to_remove_3.sort(reverse=True)
# # Remove the seats from the list
# for index in to_remove_3:
#     traces.pop(index)

# to_remove_4 = [27*28+i for i in range(28)]
# # Sort the indices in reverse order to avoid shifting
# to_remove_4.sort(reverse=True)
# # Remove the seats from the list
# for index in to_remove_4:
#     traces.pop(index)

# seats_to_remove = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 50, 51, 52, 53, 54, 55, 56, 74, 79, 80, 81, 82, 83, 84, 101, 102, 108, 109, 110, 111, 112, 129, 137, 138, 139, 140, 156, 157, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 280, 281, 308, 309, 336, 337, 364, 365, 392, 393, 394, 420, 421, 422, 448, 449, 450, 476, 477, 478, 504, 505, 506, 532, 533, 534, 560, 561, 562, 563, 588, 589, 590, 591, 616, 617, 618, 619, 644, 645, 646, 647, 672, 673, 674, 675, 700, 701, 702, 703, 728, 729, 730, 731, 756, 757, 758, 759, 784, 785, 786, 787, 812, 813, 814, 815, 840, 841,
#                    842, 843, 868, 869, 870, 871, 896, 897, 898, 899, 924, 925, 926, 927, 952, 953, 954, 980, 981, 982, 1008, 1009, 1010, 1036, 1037, 1038, 1064, 1065, 1066, 1092, 1093, 1094, 1120, 1121, 1148, 1149, 1176, 1177, 1204, 1205, 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1316, 1317, 1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1332, 1343, 1344, 1360, 1361, 1370, 1371, 1372, 1389, 1397, 1398, 1399, 1400, 1417, 1418, 1424, 1425, 1426, 1427, 1428, 1446, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475, 1478, 1479, 1480, 1481, 1482, 1483, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511]

# # Remove the seats from the gallery
# for i in reversed(seats_to_remove):
#     traces.pop(i)

# # Create stage layout as a half moon trace figure


# def stage_y_values(x):
#     return 6 * np.sin(x * np.pi / 56) - 4


# x = np.array(list(range(57)))
# y = stage_y_values(x)

# stage = go.Scatter(
#     x=x,
#     y=y,
#     mode='lines',
#     fill='toself',
#     line=dict(width=4, color='#333333'),
#     fillcolor='#333333',
#     text=['STAGE'],
#     textposition='top center',
#     textfont=dict(color='white')  # set the text color to white
# )


# # Append the stage trace to the list of traces
# traces.append(stage)

# # Update stage formatting
# stage.update(fill='toself', fillcolor='#333333',
#              line=dict(width=4, color='#333333'))

# # Add a contour line to the bottom of the half-moon stage outline
# bottom_line = go.Scatter(
#     x=list(range(57)),
#     y=[min(y) for i in range(57)],
#     mode='lines',
#     line=dict(width=2, color='#333333'),
# )

# # Append the bottom line trace to the list of traces
# traces.append(bottom_line)

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
# seat_options = [f'Seat {i}' for i in range(len(traces))] # works with original gallery only
# sorted_seats = sorted(gallery.items(), key=lambda x: x[0])
# seat_options = [seat[0] for seat in sorted_seats]
seat_options = [seat for seat in sorted(gallery.keys())]

# Update recently created seats in venue pulling archived/cached seat_color from session_state that was created on previous run downstream
try:
    if st.session_state:
        for seat_name, seat_color in st.session_state.items():
            gallery[seat_name]['color'] = seat_color
            gallery[seat_name]['bought'] = True
            for trace in traces:
                if trace.name == seat_name:
                    trace.marker.color = seat_color
                    break
            # seat_index = seat_options.index(seat_name)
            # traces[seat_index]['marker']['color'] = seat_color
            # gallery[list(gallery.keys())[seat_index]]['color'] = seat_color
            # gallery[list(gallery.keys())[seat_index]]['bought'] = True
except:
    None
# Plot seating layout
fig = go.Figure(data=traces, layout=layout)

# Create function to update gallery seat names


# def custom_legend_name(new_names):
#     for i, new_name in enumerate(new_names):
#         fig.data[i].name = new_name
#         gallery[list(gallery.keys())[i]]['name'] = new_name


# Update original gallery seating names with custom seat_options ('Seat {i}') name for better transparency
# custom_legend_name(seat_options)

# Update traces/seats & add stage name
fig.update_traces(textposition='top center', hoverlabel=(dict(namelength=-1)))
fig.update_layout(
    title={
        'text': str(_sectionName),
        'font': {'family': 'monospace', 'color': '#B3A301'}
    },
    title_font=dict(
        family='monospace',
        size=18,
        color='#B3A301'
    ),
    autosize=True, width=900, height=675, annotations=[
        dict(
            text="S T A G E",
            font=dict(
                size=24,
                family='monospace',
                color='#B3A301'
            ),
            x=((traces[-2].x[-1] + traces[-2].x[0]) / 2),
            y=min(traces[-2].y) + 2
        )
    ], hoverlabel=dict(
        font=dict(
            size=16,
            color="#B3A301"
        )
    ))

#########################################################
# JSON Read/Write to Central Server - To Update Seat Color & Non-Sensitive Info for Data Analysis
#########################################################


def update_jsonbin(ticketId, first_name_input, last_name_input, selected_address, selected_seat):
    # jsonbin url for .json file data
    # url = "https://api.jsonbin.io/v3/b/63efe266c0e7653a057997d1"
    url = _jsonBinURL

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
        #seat_index = seat_options.index(selected_seat)
        # gallery[list(gallery.keys())[seat_index]]['color'] = '#00FF00'  # green
        gallery[selected_seat]['color'] = '#00FF00'  # green
        st.write("")

        if selected_seat not in st.session_state:
            # st.session_state[selected_seat] = gallery[list(
            #     gallery.keys())[seat_index]]['color'] = '#00FF00'  # green
            st.session_state[selected_seat] = gallery[selected_seat]['color']
    if st.button('confirm seat(s)'):
        st.success(
            f"{selected_seat} successfully confirmed.", icon="✅")
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
    try:
        if (selected_seat != 'Seat 0'):
            st.markdown("<p style='color: B3A301; padding: 0; margin-top: 0px;'>selected seat info:</p>",
                        unsafe_allow_html=True)
            st.write(selected_seat)
            seat_index = seat_options.index(selected_seat)
            # st.write(gallery[list(gallery.keys())[seat_index]])
            st.write(gallery[selected_seat])
    except:
        None

    # # access event_dictionary master events list to compile unique events, venues, dates & associated JSONbin info
    # with open("json/event_dictionary.json", "r") as file:
    #     data = json.load(file)
    #     eventListValue = data.get("eventList", [])
    #     print("eventList values:", eventListValue)
    #     masterEventsList = list(
    #         set(value["eventName"] for value in eventListValue))
    #     masterEventsList.sort()
    #     print("masterEventsList:", masterEventsList)

    # # event_list
    # # event_list = ["Gorillaz", "Fleetwood Mac",
    # #               "Bob Dylan", "Phoenix", "The Strokes"]
    # # event_select = st.selectbox("select event:", event_list)
    # _eventName = st.selectbox("select event:", masterEventsList)

    # # function for obtaining all possible venues for a unique event (each 'event' is a dictionary structure and are entered in list format where the entirety of the list is a value corresponding to the "eventList" key name)
    # masterVenuesList = obtain_all_venues_for_event(_eventName)

    # # _venueName variable represents selectbox list choice of all possible unique events available for one event
    # _venueName = st.selectbox("select venue:", masterVenuesList)

    # # function for obtaining all possible concert dates (UNIX format) for a unique event (_eventName) at a specific venue (_venueName)
    # masterDatesList = obtain_date_string_for_event_venue(_venueName)

    # # _concertDate variable represents selectbox list choice of all dates pertaining to the above _venueName (and hence, _eventName)
    # _concertDate = st.selectbox("select event date:", masterDatesList)

    # venue_list
    # st.markdown("<p style='color: white; padding: 0; margin-top: 0px;'>select venue:</p>",
    #            unsafe_allow_html=True)
    # venue_list = ["Massey Hall", "Opera House", "Danforth Music Hall", 'Koerner Hall',
    #               "The Cameron House", "DROM Taberna", "Lee's Palace", "Roy Thompson Hall", "Horeshoe Tavern"]
    # venue_select = st.selectbox("select venue:", venue_list)

    # date_select override
    # date_select = 1660176000


with col2:

    for i in range(3):
        st.write("")

    # Venue Image
    venue_image = Image.open('Image_Data/massey_hall_bw.png')
    st.image(venue_image, 'Massey Hall - North Entrance')

    # # Title for Option to Select Venue Seating Area View
    # st.markdown("<p style='color: #807501; padding: 0; margin-top: 0px;'><b>seating map section:</b></p>",
    #             unsafe_allow_html=True)

    # # Option for Selecting Gallery View
    # gallery_1 = st.button("Gallery View")

    # # Option for Selecting Balcony View
    # gallery_1 = st.button("Balcony View")

    # Contact info
    # st.header("About Us:")
    st.markdown("<p style='color: #B3A301; font-size: 18px; margin-top: 0px;'>Contact Info:</p>",
                unsafe_allow_html=True)
    st.markdown("<p style='color: #B3A301; font-size: 14px; margin-top: 0px;'>Phone: 416-555-5555</p>",
                unsafe_allow_html=True)
    st.markdown("<p style='color: #B3A301; font-size: 14px; margin-top: 0px;'>Email: tickETHolder.info@gmail.com</p>",
                unsafe_allow_html=True)
    st.markdown("<p style='color: #B3A301; font-size: 14px; margin-top: 0px;'>Chatbot Assistant: (Click Here)</p>",
                unsafe_allow_html=True)
    st.markdown("<p style='color: #B3A301; font-size: 12px; margin-top: 0px;'>Developed on Remix IDE. Powered by Web3. All rights reserved.</p>",
                unsafe_allow_html=True)


#########################################################
# Create sidebar for customer form submission
with st.sidebar:
    # Top header section
    # st.markdown("<p style='color: #B3A301; padding: 0; margin-top: 0px;'><b>ticket purchase form:</b></p>",
    #            unsafe_allow_html=True)
    st.markdown(
        """
    <style>
    .stTextInput {
        margin-right: 1px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
    # text_input for customer info
    first_name_input = st.text_input(
        label="first name", placeholder="first name")
    last_name_input = st.text_input(
        label="last name", placeholder="last name")
    # text_input for aes_cipher/hashing ipfsHash data
    usepass_input = st.text_input(
        label="tickETHholder UsePass¹:", placeholder="required")
    # Drop down for eth wallet addresses ('selected_address') from customer
    selected_address = st.selectbox(
        "connect eth wallet", options=wallet_addresses)

    # *** Important conversion ***
    # Convert selected_seat to its tokenId equivalent (where selected_seat = tokenId -1) or in Solidity ticketData struct: seatNumber = ticketId -1

    # Also create a placeholder list for the seat tickets & corresponding ticketIds
    #seats_and_ticketIds_list = []

    # Confirm Buy section of code takes selected seats from session_state keys list, strips info to get seat number & convert to (ticketId) (Solidity: tokenId)
    # to interact with contract.functions.<function name> during 'buyTicket()' function process
    # get receipt from buyTicket() Solidity function transaction, create, print & save buy receipt, update JSONbin with seat numbers that were purchased
    # put seat variables into nft_generator function to build .png NFT image with associated event image & applicable qr code based on seat variable info
    # generate IPFS hash / Pinata gateway url
    # update ticket owners IPFS hash address by overwriting blank ipfsHash in their Solidity ticketData[tokenId].ipfsHash attributes
    # print IPFS image urls to sidebar for users to gain access to NFT ticket image

    if st.button("confirm buy"):
        selected_seats = list(st.session_state.keys())
        # print(selected_seats)
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
            nft_filepath = nft_generator(traces, ticketId, _eventName,
                                         _venueName, selected_seat)
            #print("nft_filepath: ", nft_filepath)
            time.sleep(2)
            ipfsHash_img = ipfs_gen(nft_filepath)
            #print("ipfsHash_img URL (pre-encryption):", ipfsHash_img)

            # ****** testing 02/11/23 - usepass hashing

            # encrypted_ipfsHash_img = aes.hash_string(
            #    usepass_input, ipfsHash_img)
            encrypted_ipfsHash_img = fernciph.encrypt_url(
                ipfsHash_img, usepass_input)  # fernet encryption/decryption

            time.sleep(2)
            #print("ipfsHash_img byte code (byte): ", encrypted_ipfsHash_img)
            ipfsHash_img_txhash = contract.functions.updateTicketIpfsHashID(ticketId, encrypted_ipfsHash_img).transact(
                {'from': selected_address})  # max gas to spend is 50 gas (50 gwei)
            ipfsHashupdate_receipt = w3.eth.waitForTransactionReceipt(
                ipfsHash_img_txhash)
            st.write("IpfsHash image url updated on buyer's nft:")
            st.write(dict(ipfsHashupdate_receipt))
            # nft_ticket_list.append(encrypted_ipfsHash_img)
            nft_ticket_list.append(ipfsHash_img)

            # ****** testing 02/11/23 - usepass hashing
        st.success(
            f"{len(nft_ticket_list)} ticket(s) successfully purchased.", icon="✅")
        st.sidebar.markdown("<p style='color: #B3A301; font-size: 14px; margin-top: 0px;'>NFT Ticket List: </p>",
                            unsafe_allow_html=True)
        st.sidebar.write(nft_ticket_list)
        #print("NFT Ticket List: ", nft_ticket_list)
        if len(nft_ticket_list) == 1:
            ticket = nft_ticket_list[0]
            st.sidebar.markdown(f"[NFT Ticket Hyperlink]({ticket})")
        else:
            for i, ticket in enumerate(nft_ticket_list):
                st.sidebar.markdown(
                    f"[NFT Ticket {i + 1} Hyperlink]({ticket})")

    # **** testing 02/11/23 encrypt/decrypt nft tickets
    if st.button("retrieve tickets"):
        #decrypted_nft_ticket_list = []
        all_encrypted_ipfsHashes_from_owner = contract.functions.getAllIpfsHashes(
            selected_address).call()
        print(f"Selected Address (Wallet Address): {selected_address}")
        print(
            f"All encrypted ipfsHashes from owner: {all_encrypted_ipfsHashes_from_owner}")
        if len(all_encrypted_ipfsHashes_from_owner) > 0:
            st.markdown("<p style='color: #B3A301; padding: 0; margin-top: 0px;'><b>Viewable NFT Tickets Available:</b></p>",
                        unsafe_allow_html=True)
            for i in range(len(all_encrypted_ipfsHashes_from_owner)):

                # ipfsHash_decrypted = aes.get_string_from_hash(
                #    usepass_input, all_encrypted_ipfsHashes_from_owner[i])
                ipfsHash_decrypted_url = fernciph.decrypt_url(
                    all_encrypted_ipfsHashes_from_owner[i], usepass_input)
                response_ipfsHash_decrypted_url = requests.get(
                    ipfsHash_decrypted_url)
                print(f"ipfsHash_decrypted_url: {ipfsHash_decrypted_url}")

                time.sleep(1)
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
                    #concatenate_url = "https://gateway.pinata.cloud/" + nft_ticket_png_url
                    concatenate_url = "https://peach-fancy-koala-731.mypinata.cloud" + nft_ticket_png_url

                    print("Full url: ", concatenate_url)
                else:
                    print("Error - Unable to retrieve html from url")
                time.sleep(1)
                #ipfsHash_decrypted = ipfsHash_decrypted.rstrip("%10")
                #ipfsHash_decrypted = ipfsHash_decrypted.replace("%10", "")
                st.markdown(f"[NFT Ticket {i + 1}]({concatenate_url})")

            # **** testing 02/11/23 encrypt/decrypt nft tickets

            # company copyright info at bottom of sidebar
    # for i in range(4):
    #    st.write("")
    # Display contract address to the sidebar for user knowledge/troubleshooting
    if contract is None:
        st.write("Unable to connect to the deployed contract.")
        st.markdown("<p style='color: red; font-size: 15px; margin-top: 0px;'><b>Unable to Connect to ETH Test Network.</b></p>",
                    unsafe_allow_html=True)
    else:
        st.markdown("<p style='color: green; font-size: 15px; margin-top: 0px;'><span style='color: #B3A301;'>Contract Status:</span><b><span style='color: green; font-size: 16px;'> Connected</span></b></p>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style='color: #B3A301; font-size: 15px; margin-top: 0px;'>Contract Address: <b>{contract.address}</b></p>",
                    unsafe_allow_html=True)
        # st.write(contract.address)
    st.markdown("<p style='color: #B3A301; font-size: 12px; margin-top: 0px;'><b>Copyright ©2023 tickETHolder.streamlit.app. All rights reserved.</b></p>",
                unsafe_allow_html=True)

#########################################################
