# Import Streamlit as gui interface
import streamlit as st
# Import libraries to run Solidity smart contract & interact with json/files
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
# Import segno library (qr code generator)
import segno
import qrcode
# Import PIL image editor
from PIL import Image, ImageFont, ImageDraw, ImageOps
# Import datetime for UNIX data conversions
import datetime
# Import JSON Request library
import requests
# Import venues info
import venues


#########################################################
# Setup Admin Dashboard / Minter Admin Console / NFT Image Constructor Web Interface
#########################################################
st.set_page_config(page_title="Buttons Grid",
                   page_icon=":guardsman:", layout="wide")

# Create columns for holding & centering the gallery layout
col1, col2 = st.columns(2)

# Sidebar Main Logo Image
# Main Logo Addition Function


# @st.cache
def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

#########################################################

# Connect to Web3 & Provide Interface for Custom ABI Contract Switching

#########################################################


st.sidebar.markdown("<p style='color: white; font-size: 28px; margin-top: 0px;'><b><u>Admin Dashboard</u></b></p>",
                    unsafe_allow_html=True)
st.sidebar.image(
    add_logo(logo_path="Image_Data/tickETHolder_logo.png", width=500, height=500))

# Web3 Contract Loading & Execution
# load dotenv
load_dotenv()

# Define and connect to a Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Connected ETH wallet
wallet_addresses = w3.eth.accounts

selected_address = st.sidebar.selectbox(
    "connect eth wallet", options=wallet_addresses)
st.sidebar.write("Connection Status:")

if w3.isConnected():
    #st.write("Connected to ETH Test Network.")
    st.sidebar.markdown("<p style='color: green; font-size: 16px; margin-top: 0px;'><b>Connected to ETH Test Network.</b></p>",
                        unsafe_allow_html=True)
else:
    #st.write("Unable to Connect to ETH Test Network.")
    st.sidebar.markdown("<p style='color: red; font-size: 16px; margin-top: 0px;'><b>Unable to Connect to ETH Test Network.</b></p>",
                        unsafe_allow_html=True)

# Current Smart Contract Address
current_smart_contract_address = st.sidebar.text_input(
    "Deployed Smart Contract Address:", placeholder=None)

# Create button for updating contract address
if st.sidebar.button("Update Contract Address"):
    with open(".env", "w") as env_file:
        env_file.write(
            "WEB3_PROVIDER_URI=http://127.0.0.1:7545\n"
            f"SMART_CONTRACT_ADDRESS={current_smart_contract_address}")
        st.success("New contract address has been updated successfully.")
    os.environ.update(dict(line.strip().split('=') for line in open('.env')))


# Open ticketholder_abi.json for ticketholer.sol file

with open(Path('./contracts/compiled/ticketholder_abi.json')) as f:
    # with open(Path(f'./contracts/compiled/{abi_contract_file_name}')) as f:
    ticketholder_abi = json.load(f)

    # Set the contract address (Ethereum address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=ticketholder_abi


    )

#########################################################

# Create display for contract connection status & type for admin confirmation & troubleshooting
if contract is None:
    st.sidebar.write("Unable to connect to the deployed contract.")
    st.sidebar.markdown("<p style='color: red; font-size: 16px; margin-top: 0px;'><b>Unable to Connect to ETH Test Network.</b></p>",
                        unsafe_allow_html=True)
else:
    st.sidebar.markdown("<p style='color: green; font-size: 16px; margin-top: 0px;'><b>Successfully connected to the deployed contract at address:.</b></p>",
                        unsafe_allow_html=True)
    st.sidebar.write(contract.address)

#########################################################

# File uploader to load specific ABI contract - Note: NOT WORKING DO NOT TOUCH
abi_contract_file = st.sidebar.file_uploader(
    "Upload the ABI contract (.json) file", type=["json"])

# Add 'Deploy Contract' button to deploy the contract to the Ethereum network
if st.sidebar.button("Connect to ABI"):
    if abi_contract_file is not None:
        st.write("Filename: ", abi_contract_file.name)
        abi_contract_file_name = abi_contract_file.name
        contract = load_contract(abi_contract_file_name)


# getTicketDetails) Solidity smart contract function
for i in range(3):
    st.sidebar.write("")
st.sidebar.markdown("<p style='color: white; font-size: 20px; margin-top: 0px;'><b><u>getTicketDetails</u></b></p>",
                    unsafe_allow_html=True)
ticket_tokenId = st.sidebar.number_input("tokenId:")
ticket_tokenId = int(ticket_tokenId)
st.sidebar.write("The tokenId value is %d", int(ticket_tokenId))
if st.sidebar.button("Ticket Details"):
    result = contract.functions.getTicketDetails(ticket_tokenId).call()
    _owner = result[0]
    _ownerFirstName = result[1]
    _ownerLastName = result[2]
    _eventName = result[3]
    _concertDate = result[4]
    _price = result[5]
    _venueName = result[6]
    _seatNumber = result[7]
    _seatColor = result[8]
    _ipfsHash = result[9]

    st.sidebar.write("owner: ", _owner)
    st.sidebar.write("owner first name ", _ownerFirstName)
    st.sidebar.write("owner last name ", _ownerLastName)
    st.sidebar.write("event name: ", _eventName)
    st.sidebar.write("concert date: ", _concertDate)
    st.sidebar.write("price ", _price)
    st.sidebar.write("venue name ", _venueName)
    st.sidebar.write("seat number: ", _seatNumber)
    st.sidebar.write("seat color: ", _seatColor)
    st.sidebar.write("ipfs Hash: ", _ipfsHash)

    # getSeatsMintedSoFar Solidity smart contract function
st.sidebar.markdown("<p style='color: white; font-size: 20px; margin-top: 0px;'><b><u>getSeatsMintedSoFar</u></b></p>",
                    unsafe_allow_html=True)
if st.sidebar.button("Seats Minted (So Far)"):
    seats_minted_so_far = contract.functions.getSeatsMintedSoFar().call()
    st.sidebar.write("Total Seats Minted (So Far): ", seats_minted_so_far)

    # getSeatsMintedSoFar Solidity smart contract function
st.sidebar.markdown("<p style='color: white; font-size: 20px; margin-top: 0px;'><b><u>MAX_TICKETS</u></b></p>",
                    unsafe_allow_html=True)
if st.sidebar.button("Get Max Tickets"):
    max_tix = contract.functions.MAX_TICKETS().call()
    st.sidebar.write("Maximum number of tickets : ", max_tix)


# Show minter_layout header
# mint() Solidity smart contract function & #setMAX_TICKETS Solidity smart contract function
with col1:
    with st.container():

        # load venue names from the venues_dictionary.json JSON file (the original venue builder file from form input in col2 to build venue functions [venues.py])
        with open("json/venues_dictionary.json", "r") as file:
            venueDictionary = json.load(file)
            venueNamesJSONList = list(venueDictionary.keys())

        # create session_state to save selectedVenueNameNew for multiple refreshers
        # if 'venueNameNew' not in st.session_state:
        if 'selected_venue' not in st.session_state:
            st.session_state.selected_venue = venueNamesJSONList[0]

        # event and venue generator admin user text input requirements (eventNameNew, venueNameNew, dateTimeNew, hourTimeNew, smartContractNew)
        st.markdown("<p style='color: white; font-size: 28px; margin-top: 0px;'><u><b>Event & Venue Generator:</b></u></p>",
                    unsafe_allow_html=True)
        eventNameNew = st.text_input("Enter event:", placeholder="")
        venueNameNew = st.selectbox(
            "Select venue:", venueNamesJSONList, index=venueNamesJSONList.index(st.session_state.selected_venue))
        dateTimeNew = st.date_input(
            "Enter event date:", datetime.date(2023, 1, 1))
        hourTimeNewString = st.time_input(
            "Enter event time (24hr time format):", datetime.time(20, 0)).strftime("%H:%M")
        hourTimeNew = datetime.datetime.strptime(hourTimeNewString, "%H:%M")

        # concatenate the dateTimeNew + hourTimeNew in order to get a combined net UNIX timestamp
        dateTimeHourTimeCombinedNew = datetime.datetime.combine(dateTimeNew, datetime.datetime.min.time(
        )) + datetime.timedelta(hours=hourTimeNew.hour, minutes=hourTimeNew.minute)

        unixTimeStampFloatNew = dateTimeHourTimeCombinedNew.timestamp()

        # unixTimeStampFloatNew = datetime.datetime.combine(
        #     dateTimeNew, datetime.datetime.min.time()).timestamp()

        unixTimeStampNew = int(unixTimeStampFloatNew)
        smartContractNew = st.text_input(
            "Enter associated smart contract:", placeholder="")
        seatJSONBinURLNew = st.text_input(
            "Enter associated JSONbin URL (for purchased seat memory):", placeholder="")

        # convert dateTimeNew datetime format to str to store in event_dictionary.json file
        dateTimeNewString = dateTimeNew.strftime("%Y-%m-%d")

        # create dictionary to store events
        #eventForJSONInput = {"eventList": []}

        # package all event related variables into a dictionary for JSON submission & setup
        eventForJSONInput = {
            "eventName": eventNameNew,
            "venueName": venueNameNew,
            "dateTime": dateTimeNewString,
            "hourTime": hourTimeNewString,
            "timeStamp": str(unixTimeStampNew),
            "smartContract": smartContractNew,
            "seatJSONBinURL": seatJSONBinURLNew
        }
        # eventForJSONInput = {
        #     "eventName": eventNameNew,
        #     "venueName": venueNameNew,
        #     "dateTime": dateTimeNewString,
        #     "timeStamp": unixTimeStampNew,
        #     "smartContract": smartContractNew
        # }

        st.session_state.selected_venue = venueNameNew
        print(st.session_state.selected_venue)

        selectedEventNameNewText = st.text(f"Selected event: {eventNameNew}")
        selectedVenueNameNewText = st.text(f"Selected venue: {venueNameNew}")
        selectedDateTimeNewText = st.text(
            f"Selected date & time: {dateTimeNew} @ {hourTimeNewString}. UNIX timestamp format: {unixTimeStampNew}")
        selectedSmartContractText = st.text(
            f"Selected smart contract: {contract.address}")
        selectedseatJSONBinURLNewText = st.text(
            f"Selected seat bin url: {seatJSONBinURLNew}")

        st.markdown("<p style='color: green; font-size: 18px; margin-top: 0px;'><u><b>Enter event details for event_dictionary.json database:</b></u></p>",
                    unsafe_allow_html=True)
        if st.button("Submit Event Details"):
            # with open("json/event_dictionary.json", "a") as file:
            with open("json/event_dictionary.json", "r") as file:
                eventDictionary = json.load(file)
            # append new event to "eventList" list (which is the key to the list of dictionaries (value) ["eventList] = key, list of dictionaries = value)
            eventDictionary["eventList"].append(eventForJSONInput)
            # save upadated eventDictionary to file
            with open("json/event_dictionary.json", "w") as file:
                json.dump(eventDictionary, file, indent=4)
                # file.write("\n")
            st.success(
                "Event successfully added to event_dictionary.json database", icon="✅")
        st.markdown("<p style='color: green; font-size: 18px; margin-top: 0px;'><u><b>View All Scheduled Events.json database:</b></u></p>",
                    unsafe_allow_html=True)
        if st.button("View"):
            with open("json/event_dictionary.json", "r") as file:
                data = json.load(file)
                eventList = data["eventList"]
                # st.write(eventList)
                #eventsList = [json.loads(line) for line in file]
            with st.container():
                st.markdown("<p style='color: green; font-size: 18px; margin-top: 0px;'><u><b>Events Database (Master List):</b></u></p>",
                            unsafe_allow_html=True)
                for event in eventList:
                    st.write(event)

            # if st.button("Submit Event & Venue to Master JSON List"):
            #    eventList.append(eventNameNew)

        with open("json/event_dictionary.json", "r") as file:
            # load data from event_dictionary.json file
            data = json.load(file)
            # use "eventList" key from the data from the json file to get the key's value. in this case the "eventList" value is the list of event dictionaries
            eventListValue = data.get("eventList", [])
            print(eventListValue)
            # generate a list with all unique "eventName" names
            # check to see if there's only on dictionary 'event' entry in the entire "eventList" list, if so create a list from it so it follows convention and can be used
            # in st.selectbox still later on from the "eventName" st.selectbox dropdown list
            if isinstance(eventListValue, dict):
                eventListValue = [eventListValue]
            print(eventListValue)

            # first creates a set of unique "eventName" values taken from the "eventList" key value pair 'eventListValue' (value of the key-value pair)
            masterEventsList = list(
                set(value["eventName"] for value in eventListValue))
            masterEventsList.sort()
            print(masterEventsList)

        #st.header("Minter Admin Console")
        st.markdown("<p style='color: white; font-size: 28px; margin-top: 0px;'><u><b>Minter Admin Console:</b></u></p>",
                    unsafe_allow_html=True)
        st.write("Event Contract Generator Form:")
        st.write("File: ticketholder.sol -> contract.functions.mint")
        st.write("")
        st.write("")
        # Set Maximum Tickets to Batch/Sell
        st.write("Set Maximum Tickets Available for Mint/Purchase:")
        # for trial purposes set to max Massey Hall gallery size
        _maxNumberOfTickets = st.number_input("Enter max tickets", 1217)
        if st.button("Set Max Tickets"):
            set_max_tickets = contract.functions.setMAX_TICKETS(
                _maxNumberOfTickets).transact({"from": selected_address})
            tx_receipt = w3.eth.waitForTransactionReceipt(set_max_tickets)
            st.write("Transaction receipt:", tx_receipt)

        _ownerFirstName = st.text_input(
            "Enter string memory _ownerFirstName", "First Name")
        _ownerLastName = st.text_input(
            "Enter string memory _ownerLastName", "Last Name")
        # _eventName = st.text_input(
        #    "Enter string memory _eventName", "Event Name")
        _eventName = st.selectbox(
            "Select string memory _eventName", masterEventsList)

        # function for obtaining all possible venues for a unique event (each 'event' is a dictionary structure, and are entered as a list where the entire list is a value corresponding to the "eventList" key)
        def obtain_all_venues_for_event(eventName):
            with open("json/event_dictionary.json", "r") as file:
                data = json.load(file)
                # if not isinstance(data, list):
                eventList = data["eventList"]
                venues = list(
                    set(value["venueName"] for value in eventList if value['eventName'] == eventName))
                venues.sort()
                return venues

        # use the 'obtain_all_venues_for_event' function to obtain list of unique venues pertaining to the specific '_eventName'
        masterVenuesList = obtain_all_venues_for_event(_eventName)

        # selectbox list of all venues pertaining to above _eventName
        _venueName = st.selectbox(
            "Select string memory _venueName", masterVenuesList)

        # function for obtaining all possible concert dates (UNIX format) for a unique event (_eventName) at a specific venue (_venueName)
        def obtain_date_for_event_venue(venueName):
            with open("json/event_dictionary.json", "r") as file:
                data = json.load(file)
                eventList = data["eventList"]
                dates = list(
                    set(value["timeStamp"] for value in eventList if value['venueName'] == venueName))
                dates.sort()
                return dates

        def obtain_date_string_for_event_venue(venueName):
            with open("json/event_dictionary.json", "r") as file:
                data = json.load(file)
                eventList = data["eventList"]
                dates = list(
                    set(value["dateTime"] for value in eventList if value["venueName"] == venueName))
                dates.sort()
                return dates

        # use the 'obtain_date_for_event_venue' function to obtain the unique timeStamp (UNIX format) for a unique event (_eventName) at a specific venue (_venueName)
        masterDatesList = obtain_date_for_event_venue(_venueName)

        # convert date string elements to int
        masterDatesList = [int(date) for date in masterDatesList]

        # convert all masterDatesList items from string to int
        # for date in masterDatesList:
        #     print(type(date))
        #     date_int = int(date)
        #     print(type(date_int))
        #     masterDatesList.remove(date)
        #     masterDatesList.append(date_int)
        #     masterDatesList.sort()

        # selectbox list for all dates pertaining to above _venueName (and hence, _eventName)
        _concertDate = st.selectbox(
            "Select uint _concertDate [UNIX Format]", masterDatesList)

        # _venueName = st.selectbox(
        #     "Select string memory _eventName", masterVenuesList)
        # _concertDate = st.number_input(
        #     "Enter uint _concertDate [UNIX Format]", 1660176000)
        gwei_price = st.number_input("Enter uint _price (in Gwei)", 71000000)
        # _venueName = st.text_input(
        #    "Enter string memory _venueName", "Venue Name")
        _seatColor = "#5A5A5A"
        batchSize = st.number_input(
            "Enter event ticket batch size (minting genesis: 0 to seatsMintedSoFar, nth batch afterwards: _seatsMintedSoFar += numToMint)", 0)

        # Gwei to wei converter function
        _price = int(gwei_price * 10**9)  # in wei

        # Mint batchSize of Tickets
        if st.button("Mint Batch"):
            mint = contract.functions.mint(_ownerFirstName, _ownerLastName,
                                           _eventName, 1660176000, _price, _venueName, _seatColor, batchSize).transact({"from": selected_address})
            tx_receipt = w3.eth.waitForTransactionReceipt(mint)
            st.write("Transaction receipt:", tx_receipt)

with col2:
    #st.header("NFT Image Constructor")
    st.markdown("<p style='color: white; font-size: 28px; margin-top: 0px;'><u><b>Venue Generator & Admin Database:</b></u></p>",
                unsafe_allow_html=True)

    # Load the venues_dictionary.json from JSON file
    with open("json/venues_dictionary.json", "r") as file:
        venues_dictionary_json = json.load(file)

    # Form Submission for Venue Addition
    venue_name = st.text_input("venue name: ")
    section_name = st.text_input("section name: ")
    section_function_name = st.text_input("section function name: ")

    if st.button("Add to venues"):
        # check to see if venue_name already exists as a main key in the venues_dictionary.json file
        if venue_name in venues_dictionary_json:
            # check if section_name already exists as a value in the venues_dictionary.json file
            if section_name in venues_dictionary_json[venue_name]:
                st.write("Section name currently exists. No updates made.")
            else:
                # check to see if function already exists in the venues.py venue layout builder file
                if hasattr(venues, section_function_name):
                    # add section/function to existing venue
                    section_function = getattr(venues, section_function_name)
                    venues_dictionary_json[venue_name][section_name] = section_function.__name__
                    # venues_dictionary_json[venue_name][section_name] = getattr(
                    #    venues, section_function_name)
                    st.write(
                        f"Added section '{section_name}' to venue '{venue_name}' with function '{section_function_name}'.")
                else:
                    st.write(
                        f"Function '{section_function_name}' not found in venues.py file.")

        else:
            # check if function exists in venues.py
            if hasattr(venues, section_function_name):
                # add new venue with corresponding new section/function
                venues_dictionary_json[venue_name] = {
                    section_name: getattr(venues, section_function_name.__name__)}
                st.write(
                    f"Added venue '{venue_name}' with section '{section_name}' and function '{section_function_name}'.")
            else:
                st.write(
                    f"Function '{section_function_name}' not found in venues.py layout builder file. No updates have occurred.")

        with open("json/venues_dictionary.json", "w") as file:
            json.dump(venues_dictionary_json, file, indent=4)

    # def add_venues(venue_name, section_name, section_function_name):
    #     if venue_name not in venues.venue_dictionary:
    #         venues.venue_dictionary[venue_name] = {}
    #         venues.venue_dictionary[venue_name][section_name] = getattr(
    #             venues, section_function_name)
    #     elif section_name not in venues.venue_dictionary[venue_name]:
    #         venues.venue_dictionary[venue_name][section_name] = getattr(
    #             venues, section_function_name)
    #     else:
    #         if not callable(venues.venue_dictionary[venue_name][section_name]):
    #             venues.venue_dictionary[venue_name][section_name] = getattr(
    #                 venues, section_function_name)

    # Add venue, section & section function to venues.venue_dictionary
    # if st.button("Add to venues"):
    #     add_venues(venue_name, section_name, section_function_name)

    # Add to the venues.py 'venue_section' dictionary if it does not already exist based on previous text_input from admin
    # if venue_name and section_name and section_function:
    #     if venue_name not in venues.venue_dictionary:
    #         venues.venue_dictionary[venue_name] = {}
    #     venues.venue_dictionary[venue_name][section_name] = eval(
    #         section_function)

    if st.button("Display Venue Database"):
        # Load the venues_dictionary.json from JSON file
        with open("json/venues_dictionary.json", "r") as file:
            venues_dictionary_json = json.load(file)

        def venue_database():
            # Display all current venues & their respective sections
            st.markdown(
                "### Venues, Sections & Section Builder Function", unsafe_allow_html=True)
            i = 1
            # Retrieve the keys of the venues.py venue_section dictionary database
            for venueName, venueSection in venues_dictionary_json.items():
                st.markdown(
                    f"<span style= 'color: green; font-family:monospace;'>{i}.)&nbsp;{venueName}</span>", unsafe_allow_html=True)
                for sectionName, sectionFunction in venueSection.items():
                    st.markdown(
                        f"\t&nbsp;&nbsp;&nbsp;&nbsp; <span style= 'color: green; font-family:monospace;'>{sectionName}: {sectionFunction}</span>", unsafe_allow_html=True)
                    #st.write(f"{sectionName}: {sectionFunction.__name__}")
                i += 1
        venue_database()
    # venue_database()

    for i in range(10):
        st.write("")
    st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'><b>Remix IDE Hyperlink:</b></p>",
                unsafe_allow_html=True)
    st.write("https://remix-beta.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.17+commit.8df45f5f.js")


# NFT Generator Functions - CURRENTLY NOT IMPLEMENTED

# JSONBin Bin Active URL
url = "https://api.jsonbin.io/v3/b/63df0c52ace6f33a22d68450"
# define headers for api request
headers = {"content-type": "application/json",
           "X-Master-Key": '$2b$10$TBShXqVtrokNLIU1b2GD7upkZ7ZV6cgi1gv0rRXYVkS656gRM1tqq'}
response = requests.get(url, headers=headers)
data_json = response.json()

record = data_json["record"]
ticket_holders = {}

for ticketholder in data_json['record']['ticketholder'][1:]:
    ticketholder_dict = {}
    tokenID = ticketholder['tokenID']
    for key, value in ticketholder.items():
        if isinstance(value, int):
            ticketholder_dict[key] = value
        else:
            ticketholder_dict[key] = str(value)
    ticket_holders[tokenID] = ticketholder_dict

# print(ticket_holders)

# Extracting attributes from ticket_holders dictionary to save as dynamic variables to automate
# ticket_holders_event_value = ticket_holders[i][]

# NFT For-Loop Automatic NFT Generator
for ticketId, info in ticket_holders.items():
    #print(f"ticketId [key]", ticketId)
    #print(f"info [value]", info)
    for key, value in info.items():
        #print(f'key:', key)
        #print(f'value:', value)
        event_ticket_holders = _eventName
        venue_ticket_holders = _venueName

        aisle_ticket_holders = info['aisle']
        row_ticket_holders = info['row']
        seat_ticket_holders = info['selected_seat']


#########################################################

# NFT Image Gen Program

#########################################################

# NFT For-Loop Automatic NFT Generator
for ticketId, info in ticket_holders.items():
    #print(f"ticketId [key]", ticketId)
    #print(f"info [value]", info)
    for key, value in info.items():
        #print(f'key:', key)
        #print(f'value:', value)
        event_ticket_holders = "Gorillaz"
        venue_ticket_holders = "Massey Hall"

        aisle_ticket_holders = str(info['aisle'])
        row_ticket_holders = str(info['row'])
        seat_ticket_holders = str(info['selected_seat'])

        #########################################################

        # Create Background Template to Overlay Foreground Images
        img = Image.new('RGB', (1000, 600), color='black')
        img.save('Image_Data/black_background_ticket.png')

        #########################################################

        # Create Event/Venue Info Text Box
        white_blank = Image.open("Image_Data/white_blank_square.png")
        black_blank = Image.open("Image_Data/black_blank_square.png")
        font = ImageFont.truetype('/Library/Fonts/Arial Black.ttf', 13)
        font_time_small = ImageFont.truetype(
            '/Library/Fonts/Arial Black.ttf', 13)

        # Get Black Blank as Canvas Template
        draw = ImageDraw.Draw(black_blank)

        # Create 'event_text' & 'venue_text' text variables to be added for event & venue info
        event_text = event_ticket_holders
        venue_text = venue_ticket_holders

        # Fetch UNIX event date stamp from Solidity and convert to formatted_date_time format ('%m/%d/%Y %H:%M:%S')
        date_time = datetime.datetime.fromtimestamp(
            _concertDate)  # UNIX timestamp variable inputs here
        formatted_date_time = date_time.strftime('%m/%d/%Y %H:%M:%S')

        # Create aisle, row & seat text variables
        aisle_text = "Aisle " + aisle_ticket_holders
        row_text = "Row " + row_ticket_holders
        selected_seat_text = seat_ticket_holders

        # Create info box ticket component

        draw.text((15, 20), event_text, (255, 255, 255), font=font)
        draw.text((15, 50), venue_text, (255, 255, 255), font=font)
        draw.text((15, 80), formatted_date_time,
                  (255, 255, 255), font=font_time_small)
        draw.text((15, 110), aisle_text, (255, 255, 255), font=font)
        draw.text((15, 140), row_text, (255, 255, 255), font=font)
        draw.text((15, 170), selected_seat_text, (255, 255, 255), font=font)

        # Draw image to 'draw' canvas and save as .png
        black_blank.save("Image_Data/text_box.png")

        #########################################################

        # Import Background Template & Foreground Images for Overlay to Complete NFT Ticket

        #########################################################

        # Create border for background image
        def add_border(im, border_width, color):
            width, height = im.size
            new_im = Image.new("RGBA", (width + 2 * border_width,
                                        height + 2 * border_width), color)
            new_im.paste(im, (border_width, border_width))
            return new_im

        # Open the background image
        #background = Image.open("Image_Data/black_background_ticket.png")
        background = Image.new('RGBA', (400, 600), (0, 0, 0, 255))

        # Integrate background & border together
        border_width = 10
        border_color = "white"
        background = add_border(background, border_width, border_color)

        # Open the text info image
        text_info_bottom_left = Image.open(
            "Image_Data/text_box.png").convert('RGBA')

        # Open the artwork image
        artwork = Image.open(
            "Image_Data/gorillaz_art.png").convert('RGBA')

        # Resize the artwork image
        artwork = artwork.resize((350, 350))

        # Resize the foreground to 200x200
        #foreground = foreground.resize((200, 200))

        # Overlay the text_info_bottom_left text onto the left bottom corner of the black template background image
        background.alpha_composite(
            text_info_bottom_left, (10, (background.height - text_info_bottom_left.height) - 10))

        # Overlay the artwork image onto the center of the black template background image
        background.alpha_composite(
            artwork, ((background.width-artwork.width)//2, (background.height-artwork.height)//2 - 50))

        #########################################################

        # QR Code Generator

        #text = "testing"

        # Concatenate all strings together
        qr_code_text = (event_text + "," + "\n" +
                        venue_text + "," + "\n" +
                        formatted_date_time + "," + "\n" +
                        aisle_text + "," + "\n" +
                        row_text + "," + "\n" +
                        selected_seat_text
                        )
        # print(qr_code_text)

        # Generate QR Code from text input (qr_code_text)
        qr_code = segno.make(qr_code_text)

        # Save QR Code Text
        qr_code.save("Image_Data/qr_code_text.png", scale=7)

        #  Open the QR Code Text image
        qr_code_img = Image.open(
            "Image_Data/qr_code_text.png").convert('RGBA')

        # Resize the foreground to 200x200
        qr_code_img = qr_code_img.resize((125, 125))

        # Overlay the text_info_bottom_left text onto the left bottom corner of the black template background image
        background.alpha_composite(
            qr_code_img, (275, (background.height - qr_code_img.height) - 20))

        #qr_code = segno.make(text)
        #qr_code.save("test.png", scale=7)
        # print(segno.__version__)

        #########################################################

        # Save as NFT ticket
        background.save(
            f"NFT_Tickets/NFT_ticket_{event_text}_{venue_text}_{selected_seat_text}.png")

#########################################################
