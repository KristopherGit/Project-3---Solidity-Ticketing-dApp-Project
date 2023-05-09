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
def load_contract(smart_contract_address):

    # Load the contract ABI
    with open(Path('./contracts/compiled/ticketholder_abi.json')) as f:
        ticketholder_abi = json.load(f)

    # Set the contract address (Ethereum address of the deployed contract)
    # contract_address = os.getenv("SMART_CONTRACT_ADDRESS") <--- original code connected to the .env file prior to 05/06/2023
    contract_address = smart_contract_address

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=ticketholder_abi
    )

    return contract

#########################################################

# Global Dictionary Variables


# Load the ticketholder Ethereum contract
# contract = load_contract() <-- original code connected to the .env file prior to 05/06/2023
contract = None

# Variable to hold the NFT Artwork Image File Name
_artworkName = None


#########################################################

# tickETHolder Main GUI Streamlit Page Setup
# Main Logo Addition Function


# @st.cache
def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo


# Sidebar Main Logo Image
st.sidebar.image(
    add_logo(logo_path="Image_Data/tickETHolder_logo.png", width=650, height=425), output_format="auto", use_column_width="auto")
st.markdown(f'''
    <style>
    section[data-testid="stSidebar"] .css-ng1t4o {{width: 14rem;}}
    </style>
''', unsafe_allow_html=True)

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
        # print("eventList values:", eventListValue)
        masterEventsList = list(
            set(value["eventName"] for value in eventListValue))
        masterEventsList.sort()
        # print("masterEventsList:", masterEventsList)

    # event_select = st.selectbox("select event:", event_list)
    _eventName = st.selectbox("select event:", masterEventsList)

    # function to fetch all venues for a particular eventName
    # @st.cache(allow_output_mutation=True)
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
    # @st.cache(allow_output_mutation=True)
    def obtain_date_string_for_event_venue(_eventName, _venueName):
        with open("json/event_dictionary.json", "r") as file:
            data = json.load(file)
            eventList = data["eventList"]
            dates = list(
                set(value["dateTime"] for value in eventList if value["venueName"] == _venueName and value["eventName"] == _eventName))
            dates.sort()
            times = list(set(value["hourTime"] for value in eventList if value["venueName"]
                         == _venueName and value["eventName"] == _eventName))
            times.sort()
            return dates, times

    # function for obtaining all possible concert dates (UNIX format) for a unique event (_eventName) at a specific venue (_venueName)
    masterDatesList, masterTimesList = obtain_date_string_for_event_venue(
        _eventName, _venueName)

    # _concertDate variable represents selectbox list choice of all dates pertaining to the above _venueName (and hence, _eventName)
    _concertDate = st.selectbox("event date:", masterDatesList)
    print("_concertDate: ", _concertDate)
    print("_concertDate type: ", type(_concertDate))

    # _concertTime = st.selectbox represents selectbox list choice of all date-times pertaining to the above _venueName (and hence, _eventName)
    _concertTime = st.selectbox("event time: ", masterTimesList)
    print("_concertTime: ", _concertTime)
    print("_concertTime type: ", type(_concertTime))

    # retrieve the "unique_id" based on unique "_eventName", "_venueName" and "_concertDate"
    # @st.cache(allow_output_mutation=True)
    def obtain_unique_id_and_artwork_id(_eventName, _venueName, _concertDate):
        with open("json/event_dictionary.json", "r") as file:
            data = json.load(file)
            eventList = data["eventList"]
            uniqueids = list(set(value["unique_id"] for value in eventList if value["eventName"] ==
                             _eventName and value["venueName"] == _venueName and value["dateTime"] == _concertDate))
            artworkids = list(set(value["nftArtwork"] for value in eventList if "nftArtwork" in value and value["eventName"]
                              == _eventName and value["venueName"] == _venueName and value["dateTime"] == _concertDate))
            return uniqueids, artworkids

    # retrieve "_uniqueIdList" for "unique_id" then retrieve what should be the only item in the list at index 0
    _uniqueIdList, _artworkNameNew = obtain_unique_id_and_artwork_id(
        _eventName, _venueName, _concertDate)
    print("_uniqueIdList: ", _uniqueIdList)
    _uniqueId = _uniqueIdList[0]
    print("_uniqueId: ", _uniqueId)

    # set artworkids [_artworkNameNew] equal to the _artworkName variable
    _artworkName = _artworkNameNew[0]
    print("_artworkName: ", _artworkName)

    # function that gets the smart contract address for a specific event name
    # @st.cache(allow_output_mutation=True)
    def obtain_smart_contract_address_for_event(_uniqueId):
        with open("json/event_dictionary.json", "r") as file:
            data = json.load(file)
            eventList = data["eventList"]
            for event in eventList:
                if event["unique_id"] == _uniqueId:
                    smart_contract_address = str(event["smartContract"])
            # smart_contract_address = value["smartContract"] for value in eventList if value["unique_id"] == _uniqueId
            # smart_contract_address = str(smart_contract_address)
            return smart_contract_address

    # obtain smart contract address using above defined obtain_smart_contract_address_for_event that pulls data fro the json/event_dictionary.json json file
    smart_contract_address = obtain_smart_contract_address_for_event(_uniqueId)
    # set the contract attributes (contract_address & abi from ticketholder.json abi) previously defined prior to the 'with col_1:' statement
    contract = load_contract(smart_contract_address)

    # function that will fetch the 'seat JSONbin url' that corresponds to its associated _eventName, _venueName & _concertDate above

    # @st.cache(allow_output_mutation=True)
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
    # @st.cache(allow_output_mutation=True)
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
    # print("_sectionName: ", _sectionName)

    # connect to and populate the venue.py saved venue layouts to create visual representation of available & purchased seats for the above chosen _venueName (as a function of _eventName)
    # print(masterSectionDict[_sectionName])
    # print(type(masterSectionDict[_sectionName]))

    sectionFunctionNameString = masterSectionDict[_sectionName]
    # print("sectionFunctionNameString: ", sectionFunctionNameString)

    venueSectionFunctionName = getattr(ven, sectionFunctionNameString)
    # print(type(venueSectionFunctionName))

    # Obtain gallery={} equivalent dictionary data from .json file to be passed into the venues.py 'create_..' functions to be converted to gallery = {} below
    # match section name from the unique_Id matching .json file to the _sectionName (key) and use that to obtain the values sectionFunctionNameString (value)
    # ****** added 03/30/2023
    # @st.cache(allow_output_mutation=True)
    def obtain_venue_section_json_dictionary(_sectionName, _uniqueId):
        with open(f"event_venue_library/{_uniqueId}", "r") as file:
            data = json.load(file)
            if _sectionName in data["venueSections"][0]:
                return data["venueSections"][0][_sectionName]
            else:
                return None
    # ****** added 03/30/2023

    # call the 'obtain_venue_section_json_dictionary' and map dictionary result to dictionary variable to be taken in as a parameter to the venues.py unique function
    galleryDictInput = obtain_venue_section_json_dictionary(
        _sectionName, _uniqueId)
    #print("galleryDictInput: ", galleryDictInput)


# Show concert_layout header
with col1:
    # st.header("tickETHolder")
    # st.markdown("<p style='color: #B3A301; font-size: 24px; margin-top: 0px;'><b>tickETHolder™</b></p>",
    #             unsafe_allow_html=True)

    # Create a dictionary that holds the attributes of each seat but first reference it with session_state seats already coded
    #"st.session_state object:", st.session_state

    # Import gallery & traces from venues.py as venue_massey_hall
    # gallery, traces = ven.create_venue_massey_hall_gallery()
    try:
        gallery, traces, fig = venueSectionFunctionName(galleryDictInput)
        #print("gallery:", gallery)
        #print("traces:", traces)
    except:
        st.markdown("<p style='color: #B3A301; font-size: 16px; margin-top: 0px;'><b>Venue section under construction. Please check back.</b></p>",
                    unsafe_allow_html=True)
        image = Image.open('Image_Data/under_construction.jpeg')
        st.image(image, caption='Maintenance underway.')
        gallery, traces, fig = {}, [], {}

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

if 'record' in data_json and 'ticketholder' in data_json['record']:
    ticketholders = data_json['record']['ticketholder']
    for ticketholder in ticketholders[1:]:
        for index, trace in enumerate(traces):
            token_id = str(ticketholder['tokenID'])
            if token_id.isdigit() and int(token_id) == index:
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
        for seat_key, seat_value in st.session_state.items():
            gallery[seat_key]['color'] = seat_value['color']
            gallery[seat_key]['bought'] = False
            for trace in traces:
                if trace.name == seat_key:
                    trace.marker.color = seat_value['color']
                    break
            # seat_index = seat_options.index(seat_name)
            # traces[seat_index]['marker']['color'] = seat_color
            # gallery[list(gallery.keys())[seat_index]]['color'] = seat_color
            # gallery[list(gallery.keys())[seat_index]]['bought'] = True
except:
    None

#########################################################
# JSON Read/Write to Central Server - To Update Seat Color & Non-Sensitive Info for Data Analysis
#########################################################


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def update_jsonbin(_jsonBinURL, ticketId, first_name_input, last_name_input, selected_address, selected_seat):
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

    # ticket_id = ticketId
    # counter = 0
    # while any(d['tokenID'] == ticket_id for d in data["ticketholder"]):
    #     counter += 1
    #     ticket_id = f"{ticketId}_{counter}"

    # # Access the row & aisle values from each trace (seat) that corresponds to each tokenId/seat number
    # aisle = traces[ticket_id - 1]['x'][0]
    # row = traces[ticket_id - 1]['y'][0]

    data["ticketholder"].append({
        "tokenID": ticketId,
        "first_name": first_name_input,
        "last_name": last_name_input,
        "selected_address": selected_address,
        "seat_color": "#1E90FF",  # default blue/unsold
        "name": selected_seat["name"],
        "sec": selected_seat["sec"],
        "row": selected_seat["row"],
        "seat number": selected_seat["seat number"]
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

    button_container_1 = st.container()
    with button_container_1:

        if st.button('select seat(s)'):
            #seat_index = seat_options.index(selected_seat)
            # gallery[list(gallery.keys())[seat_index]]['color'] = '#00FF00'  # green
            gallery[selected_seat]['color'] = '#00FF00'  # green
            # print("gallery[selected_seat]: ", gallery[selected_seat])
            st.write("")

            if selected_seat not in st.session_state:
                # st.session_state[selected_seat] = gallery[list(
                #     gallery.keys())[seat_index]]['color'] = '#00FF00'  # green
                st.session_state[selected_seat] = gallery[selected_seat]
                # st.session_state[selected_seat] = gallery[selected_seat]
                print("st.session_state[selected_seat]: ",
                      st.session_state[selected_seat])
        if st.button('confirm seat(s)'):
            st.success(
                f"{selected_seat} successfully confirmed.", icon="✅")
            st.write()

        if st.button('clear all selected seat(s)'):
            st.session_state.clear()

    # concert_layout = st.plotly_chart(
    #     fig, use_container_width=False, height=400, width=1000)
    fig.update(data=traces)
    concert_layout = st.plotly_chart(
        fig, use_container_width=False, height=400, width=1000)
    st.session_state

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

with col2:

    for i in range(3):
        st.write("")

    # Venue Image - * Note needs to be remade with venue associated image
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
        try:
            # selected_seats = list(st.session_state.keys())
            selected_seats = st.session_state
            print(selected_seats)
            # *New test
            nft_ticket_list = []
            # for selected_seat in selected_seats:
            for selected_seat_key, selected_seat_value in selected_seats.items():
                # create a dictionary to hold the name & ipfsHash_img for each ticket
                ticket_dictionary = {}
                # seat_string_stripped_list = selected_seat.split(" ")
                # seat_num_stripped = int(seat_string_stripped_list[1])
                ticketId = selected_seat_value["tokenID"]
                print("ticketId: ", ticketId)
                # ticketId = seat_num_stripped + 1
                tx_hash = contract.functions.buyTicket(
                    ticketId, first_name_input, last_name_input, selected_seat_value["name"]).transact({'from': selected_address, 'value': (selected_seat_value["price"]["_gweiValue"]*1000000000)})
                # tx_hash = contract.functions.buyTicket(
                #     ticketId, first_name_input, last_name_input).transact({'from': selected_address, 'value': 71000000000000000})

                # receipt = w3.eth.waitForTransactionReceipt(tx_hash)

                st.write("Transaction hash:")
                # st.write(dict(tx_hash))
                st.write(tx_hash)
                # update_jsonbin(ticketId, first_name_input,
                #                last_name_input, selected_address, selected_seat)
                update_jsonbin(_jsonBinURL, ticketId, first_name_input,
                               last_name_input, selected_address, selected_seat_value)
                # nft_filepath = nft_generator(traces, ticketId, _eventName,
                #                              _venueName, selected_seat)
                nft_filepath = nft_generator(_artworkName, _eventName,
                                             _venueName, _concertDate, _concertTime, selected_seat_value)
                #print("nft_filepath: ", nft_filepath)
                time.sleep(1)
                ipfsHash_img = ipfs_gen(nft_filepath)
                #print("ipfsHash_img URL (pre-encryption):", ipfsHash_img)

                # ****** testing 02/11/23 - usepass hashing

                # encrypted_ipfsHash_img = aes.hash_string(
                #    usepass_input, ipfsHash_img)
                encrypted_ipfsHash_img = fernciph.encrypt_url(
                    ipfsHash_img, usepass_input)  # fernet encryption/decryption

                time.sleep(1)
                #print("ipfsHash_img byte code (byte): ", encrypted_ipfsHash_img)
                ipfsHash_img_txhash = contract.functions.updateTicketIpfsHashID(ticketId, encrypted_ipfsHash_img).transact(
                    {'from': selected_address})  # max gas to spend is 50 gas (50 gwei)
                # ipfsHashupdate_receipt = w3.eth.waitForTransactionReceipt(
                #     ipfsHash_img_txhash)
                st.write("IpfsHash image url updated on buyer's nft:")
                # st.write(dict(ipfsHash_img_txhash))
                st.write(ipfsHash_img_txhash)
                # add ticket name & ipfsHash_img info to the single ticket dictionary
                ticket_dictionary = {
                    "ticket name": f'{_eventName} {_venueName} {_concertDate} {_concertTime} {selected_seat_value["name"]}',
                    "ipfsHash Image": ipfsHash_img
                }

                # nft_ticket_list.append(encrypted_ipfsHash_img)
                # nft_ticket_list.append(ipfsHash_img)
                nft_ticket_list.append(ticket_dictionary)

                # ****** testing 02/11/23 - usepass hashing
            st.success(
                f"{len(nft_ticket_list)} ticket(s) successfully purchased.", icon="✅")
            st.sidebar.markdown("<p style='color: #B3A301; font-size: 14px; margin-top: 0px;'>NFT Ticket List: </p>",
                                unsafe_allow_html=True)
            # st.sidebar.write(nft_ticket_list)
            #print("NFT Ticket List: ", nft_ticket_list)
            if len(nft_ticket_list) == 1:
                ticket = nft_ticket_list[0]
                st.sidebar.markdown(
                    f'[NFT Ticket: {ticket["ticket name"]}]({ticket["ipfsHash Image"]})')
            else:
                for i, ticket in enumerate(nft_ticket_list):
                    st.sidebar.markdown(
                        # f"[NFT Ticket {i + 1} Hyperlink]({ticket})")
                        f'[{i + 1}. NFT Ticket No. {i + 1}: {ticket["ticket name"]}]({ticket["ipfsHash Image"]})')
        except Exception as e:
            st.write("Error", e)

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
        st.markdown("<p style='color: green; font-size: 15px; margin-top: 0px;'><span style='color: #B3A301;'>Contract Connection Status:</span><b><span style='color: green; font-size: 16px;'> Connected</span></b></p>",
                    unsafe_allow_html=True)
        st.markdown(f"<p style='color: #B3A301; font-size: 15px; margin-top: 0px;'>Contract Address: <b>{contract.address}</b></p>",
                    unsafe_allow_html=True)
        # st.write(contract.address)
    st.markdown("<p style='color: #B3A301; font-size: 12px; margin-top: 0px;'><b>Copyright ©2023 tickETHolder.streamlit.app. All rights reserved.</b></p>",
                unsafe_allow_html=True)

#########################################################
