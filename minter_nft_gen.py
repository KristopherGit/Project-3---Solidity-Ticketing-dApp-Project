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
# Import shutil, inspect, and importlib.util for file content copying (i.e. create unique event specific functions from venue.py function content)
import shutil
import inspect
import importlib.util
import importlib
import time


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


# Load tickETHolder logo via add_logo() function
st.sidebar.image(
    add_logo(logo_path="Image_Data/ticketholder_minter_logo_v1.png", width=650, height=425), output_format="auto", use_column_width="auto")

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
    # st.write("Connected to ETH Test Network.")
    st.sidebar.markdown("<p style='color: green; font-size: 16px; margin-top: 0px;'><b>Connected to ETH Test Network.</b></p>",
                        unsafe_allow_html=True)
else:
    # st.write("Unable to Connect to ETH Test Network.")
    st.sidebar.markdown("<p style='color: red; font-size: 16px; margin-top: 0px;'><b>Unable to Connect to ETH Test Network.</b></p>",
                        unsafe_allow_html=True)

# Current Smart Contract Address
current_smart_contract_address = st.sidebar.text_input(
    "Enter Smart Contract Address:", placeholder=None)

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

# Set the contract address display encapsulated within the container in the sidebar itself
# Add the contract.address event id later on down in the code

container_1 = st.sidebar.container()

if contract is None:
    container_1.write("Unable to connect to the deployed contract.")
    container_1.markdown("<p style='color: red; font-size: 16px; margin-top: 0px;'><b>Unable to Connect to ETH Test Network.</b></p>",
                         unsafe_allow_html=True)
else:
    # container_1.markdown("<p style='color: green; font-size: 16px; margin-top: 0px;'><b>Successfully connected to the deployed contract at address:.</b></p>",
    #                      unsafe_allow_html=True)
    container_1.markdown("<p style='color: green; font-size: 16px; margin-top: 0px;'><b>Successfully connected to the deployed contract at address: </b><span style='color:white'> {}</span></p>".format(contract.address),
                         unsafe_allow_html=True)
    # container_1.write(contract.address)
    print("contract.address: ", contract.address)

    # Find the contract.address associated event in the json/event_dictionary.json
    with open("json/event_dictionary.json", "r") as file:
        # load data from event_dictionary.json file
        data = json.load(file)
        eventList = data["eventList"]

    for event in eventList:
        if event["smartContract"] == contract.address:
            # container_1.write(f'unique_id: {event["unique_id"]}')
            container_1.markdown("<p style='color: green; font-size: 16px; margin-top: 0px;'><b>unique_id: </b><span style='color:white'> {}</span></p>".format(event["unique_id"]),
                                 unsafe_allow_html=True)


# if contract is None:
#     st.sidebar.write("Unable to connect to the deployed contract.")
#     st.sidebar.markdown("<p style='color: red; font-size: 16px; margin-top: 0px;'><b>Unable to Connect to ETH Test Network.</b></p>",
#                         unsafe_allow_html=True)
# else:
#     st.sidebar.markdown("<p style='color: green; font-size: 16px; margin-top: 0px;'><b>Successfully connected to the deployed contract at address:.</b></p>",
#                         unsafe_allow_html=True)
#     st.sidebar.write(contract.address)
#     print("contract.address: ", contract.address)

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
ticket_tokenId = st.sidebar.number_input("tokenId:", step=1, format="%d")
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
    _seatName = result[8]
    _seatColor = result[9]
    _ipfsHash = result[10]

    st.sidebar.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>owner: <span style='color:green; font-size: 13px; font-family: monospace; background-color: #0E1117; padding: 2px;'> {}</span></p>".format(_owner),
                        unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>_ownerFirstName: <span style='color:green; font-size: 13px; font-family: monospace; background-color: #0E1117; padding: 2px;'> {}</span></p>".format(_ownerFirstName),
                        unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>_ownerLastName: <span style='color:green; font-size: 13px; font-family: monospace; background-color: #0E1117; padding: 2px;'> {}</span></p>".format(_ownerLastName),
                        unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>_eventName: <span style='color:green; font-size: 13px; font-family: monospace; background-color: #0E1117; padding: 2px;'> {}</span></p>".format(_eventName),
                        unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>_concertDate [UNIX format]: <span style='color:green; font-size: 13px; font-family: monospace; background-color: #0E1117; padding: 2px;'> {}</span></p>".format(_concertDate),
                        unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>_price: <span style='color:green; font-size: 13px; font-family: monospace; background-color: #0E1117; padding: 2px;'> {}</span></p>".format(_price),
                        unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>_venueName: <span style='color:green; font-size: 13px; font-family: monospace; background-color: #0E1117; padding: 2px;'> {}</span></p>".format(_venueName),
                        unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>_tokenIdNumber: <span style='color:green; font-size: 13px; font-family: monospace; background-color: #0E1117; padding: 2px;'> {}</span></p>".format(_seatNumber),
                        unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>_seatName: <span style='color:green; font-size: 13px; font-family: monospace; background-color: #0E1117; padding: 2px;'> {}</span></p>".format(_seatName),
                        unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>_seatColor: <span style='color:green; font-size: 13px; font-family: monospace; background-color: #0E1117; padding: 2px;'> {}</span></p>".format(_seatColor),
                        unsafe_allow_html=True)
    st.sidebar.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'>_ipfsHash: <span style='color:green; font-size: 13px; font-family: monospace; background-color: #0E1117; padding: 2px;'> {}</span></p>".format(_ipfsHash),
                        unsafe_allow_html=True)

    # st.sidebar.text("owner: ", _owner)
    # st.sidebar.text("owner first name ", _ownerFirstName)
    # st.sidebar.write("owner last name ", _ownerLastName)
    # st.sidebar.write("event name: ", _eventName)
    # st.sidebar.write("concert date: ", _concertDate)
    # st.sidebar.write("price: ", _price)
    # st.sidebar.write("venue name: ", _venueName)
    # st.sidebar.write("token Id number: ", _tokenIdNumber)
    # st.sidebar.write("seat name: ", _seatName)
    # st.sidebar.write("seat color: ", _seatColor)
    # st.sidebar.write("ipfs Hash: ", _ipfsHash)

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

for i in range(5):
    st.sidebar.write("")
st.sidebar.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'><b>Remix IDE Hyperlink:</b></p>",
                    unsafe_allow_html=True)
st.sidebar.write(
    "https://remix-beta.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.17+commit.8df45f5f.js")


# Show minter_layout header
# mint() Solidity smart contract function & #setMAX_TICKETS Solidity smart contract function
with col1:
    with st.container():

        # load venue names from the venues_dictionary.json JSON file (the original venue builder file from form input in col2 to build venue functions [venues.py])
        with open("json/venues_dictionary.json", "r") as file:
            venueDictionary = json.load(file)
            venueNamesJSONList = list(venueDictionary.keys())
            venueNamesJSONList.sort()
            # Add 'None' spacer item to the list so that in the streamlit app it doesn't pre-select a venue item and pre-populate the dynamic price st.number_input boxes
            venueNamesJSONList = [None] + venueNamesJSONList

        # create session_state to save selectedVenueNameNew for multiple refreshers
        # if 'venueNameNew' not in st.session_state:

        # removed 03/29/2023 @ 7:17 PM -> cluttering up the event_dictionary.json
        # if 'selected_venue' not in st.session_state:
        #    st.session_state.selected_venue = venueNamesJSONList[0]

        # event and venue generator admin user text input requirements (eventNameNew, venueNameNew, dateTimeNew, hourTimeNew, smartContractNew)
        st.markdown("<p style='color: white; font-size: 28px; margin-top: 0px;'><u><b>2.) Event & Venue Generator:</b></u></p>",
                    unsafe_allow_html=True)
        eventNameNew = st.text_input("Enter event:", placeholder="")
        venueNameNew = st.selectbox(
            "Select venue:", venueNamesJSONList)
        # venueNameNew = st.selectbox(
        #     "Select venue:", venueNamesJSONList, index=venueNamesJSONList.index(st.session_state.selected_venue))
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

        # prompt admin user to select nft artwork image for the associated event using the file_uploader() method
        raw_artwork_file = st.file_uploader(
            "Raw artwork NFT image (.png):", type=[".png"])
        print("raw_artwork_file: ", raw_artwork_file)

        unixTimeStampNew = int(unixTimeStampFloatNew)
        smartContractNew = st.text_input(
            "Enter associated smart contract:", value="0x85A15452938D53a2a7DAE730C4f1489dC0a337e1")
        seatJSONBinURLNew = st.text_input(
            "Enter associated JSONbin URL (for purchased seat memory):", value="https://api.jsonbin.io/v3/b/63efe266c0e7653a057997d1")

        # convert dateTimeNew datetime format to str to store in event_dictionary.json file
        dateTimeNewString = dateTimeNew.strftime("%Y-%m-%d")

        # create dictionary to store events
        # eventForJSONInput = {"eventList": []}

        # package all event related variables into a dictionary for JSON submission & setup
        # note all strings

        if venueNameNew != None:
            eventForJSONInput = {
                # "unique_id": f'{eventNameNew}_{venueNameNew}_{dateTimeNewString}.json',
                "unique_id": f'{eventNameNew.replace(" ", "_")}_{venueNameNew.replace(" ", "_")}_{dateTimeNewString.replace(" ", "_")}.json',
                "eventName": eventNameNew,
                "venueName": venueNameNew,
                "dateTime": dateTimeNewString,
                "hourTime": hourTimeNewString,
                "timeStamp": str(unixTimeStampNew),
                "smartContract": smartContractNew,
                "seatJSONBinURL": seatJSONBinURLNew,
                "nftArtwork": f'{eventNameNew.replace(" ", "_")}_{venueNameNew.replace(" ", "_")}_{dateTimeNewString.replace(" ", "_")}.png'
            }

            # st.session_state.selected_venue = venueNameNew
            # print(st.session_state.selected_venue)

            selectedUniqueIDNewText = st.text(
                f'Unique Id: {eventNameNew.replace(" ", "_")}_{venueNameNew.replace(" ", "_")}_{dateTimeNewString.replace(" ", "_")}.json')
            selectedEventNameNewText = st.text(
                f"Selected event: {eventNameNew}")
            selectedVenueNameNewText = st.text(
                f"Selected venue: {venueNameNew}")
            selectedDateTimeNewText = st.text(
                f"Selected date & time: {dateTimeNew} @ {hourTimeNewString}. UNIX timestamp format: {unixTimeStampNew}")
            selectedSmartContractText = st.text(
                f"Selected smart contract: {contract.address}")
            selectedseatJSONBinURLNewText = st.text(
                f"Selected seat bin url: {seatJSONBinURLNew}")
            selectedNFTArtworkText = st.text(
                f'NFT Artwork: {eventNameNew.replace(" ", "_")}_{venueNameNew.replace(" ", "_")}_{dateTimeNewString.replace(" ", "_")}.png')

            # Function to create unique event .py file and functions based on event, venue and date data
            # **** new added 03/15/2023
            # **************

            # unique pricing
            # update unique price values for unique 'sec'/'seat's of a venue
            venue_file = venueNameNew + ".json"
            venue_file_path = os.path.join(
                "json/venue_template_json/", venue_file)
            with open(venue_file_path, 'r') as file:
                venue_json_dict_copy = json.load(file)

            # get all the unique 'sec' values in the venue
            unique_sections = set()
            for unique_sec in venue_json_dict_copy["venueSections"]:
                for seat in unique_sec.values():
                    for key, value in seat.items():
                        # print(f"{key}: {value}")
                        unique_sections.add(value['sec'])
            # print(unique_sec)

            # create st.number_input boxes for each unique 'sec' value
            for unique_sec in sorted(unique_sections):
                price = st.number_input(
                    f"Enter price for section {unique_sec}", value=0)
                # update price value for all seats with the current 'sec' value
                for section_dict in venue_json_dict_copy["venueSections"]:
                    # print(section_dict)
                    for seat in section_dict.values():
                        for key, value in seat.items():
                            if value["sec"] == unique_sec:
                                value["price"] = {
                                    "CAD": price, "_gweiValue": None}

            def create_unique_event_functions(event_name, venue_name, event_date):
                # check if there's a matching .json file name in the json/venue_template_json directory
                venue_template_json_files = os.listdir(
                    "json/venue_template_json")
                matching_file = None
                for filename in venue_template_json_files:
                    if filename.replace(".json", "") == venue_name:
                        matching_file = filename
                        break

                if matching_file:
                    # copy the matching file to a new file in the event_venue_library dir for storage/use
                    new_filename = f'event_venue_library/{eventNameNew.replace(" ", "_")}_{venueNameNew.replace(" ", "_")}_{dateTimeNewString.replace(" ", "_")}.json'
                    shutil.copy(
                        f'json/venue_template_json/{matching_file}', new_filename)
                else:
                    st.warning(
                        f"No matching template found for the selected venue {venue_name}.")

            def create_unique_nft_artwork(raw_artwork_file, event_name, venue_name, event_date):
                # determine if the raw_artwork_file exists and is of correct .png format
                try:
                    if raw_artwork_file is not None:

                        # pull file name attribute from the raw_artwork_file
                        raw_artwork_file_name = raw_artwork_file.name

                        # establish directory to place the nft artwork file
                        file_dest_dir = "event_venue_library/nft_artwork"

                        # create new file name format
                        nft_artwork_filename = f'{eventNameNew.replace(" ", "_")}_{venueNameNew.replace(" ", "_")}_{dateTimeNewString.replace(" ", "_")}.png'

                        # establish the destination pathway
                        file_path = os.path.join(
                            file_dest_dir, nft_artwork_filename)

                        # save the chosen uploaded file via the established destination path
                        with open(file_path, "wb") as file:
                            file.write(raw_artwork_file.getbuffer())

                        st.success(
                            f"NFT artwork image file {nft_artwork_filename} uploaded, copied & allocated to appropriate directory successfully.")
                except:
                    st.warning(
                        "Problem with uploaded file. Check file format is .png")

                    # **** new added 03/15/2023
                    # **************

            st.markdown("<p style='color: green; font-size: 18px; margin-top: 0px;'><u><b>Enter event details for event_dictionary.json database:</b></u></p>",
                        unsafe_allow_html=True)

            ##########
            # Submit Event Details (Start) #

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

                # create actual unique_id event, date and venue file (f'{eventNameNew}_{venueNameNew}_{dateTimeNewString}.py')
                # def create_unique_event_functions(event_name, venue_name, event_date)
                create_unique_event_functions(
                    eventNameNew, venueNameNew, dateTimeNewString)

                # create unique NFT artwork file allocated to directory event_venue_library/nft_artwork
                create_unique_nft_artwork(
                    raw_artwork_file, eventNameNew, venueNameNew, dateTimeNewString)

                # update the unique event .json with the new prices based on the section 'sec' price setting above
                # re-open the unique .json created above with the 'create_unique_event_functions' to update .json with new 'price' per 'sec'
                event_file_path = f'event_venue_library/{eventNameNew.replace(" ", "_")}_{venueNameNew.replace(" ", "_")}_{dateTimeNewString.replace(" ", "_")}.json'
                with open(event_file_path, 'r') as file:
                    event_json_dict = json.load(file)

                for target_dict in event_json_dict["venueSections"]:
                    for seat in target_dict.values():
                        for key, value in seat.items():
                            # compare the 'sec' value with the 'sec' value in the 'venue_json_dict_copy' <- original updated dictionary from above
                            for section_dict in venue_json_dict_copy["venueSections"]:
                                for seat_copy in section_dict.values():
                                    for key_copy, value_copy in seat_copy.items():
                                        if value_copy['sec'] == value['sec']:
                                            # update the price value with the corresponding updated new price value from the 'venue_json_dict_copy'
                                            value['price'] = value_copy['price']

                # save the updated unique new event .json file
                with open(event_file_path, 'w') as file:
                    json.dump(event_json_dict, file, indent=4)

                # loop through all the 'sec' seat values and update the price according to 'sec'
                # for section_dict in event_json_dict["venueSections"]:
                #     for seat in section_dict.values():
                #         for key, value in seat.items():
                #             if value['sec'] == unique_sec:
                #                 value['price'] = price

            ##########
            # Submit Event Details (End) #

                st.success(
                    f'{eventNameNew.replace(" ", "_")}_{venueNameNew.replace(" ", "_")}_{dateTimeNewString.replace(" ", "_")} successfully added to event_dictionary.json database", icon="✅"')
            st.markdown("<p style='color: green; font-size: 18px; margin-top: 0px;'><u><b>View All Scheduled Events.json database:</b></u></p>",
                        unsafe_allow_html=True)
        if st.button("View"):
            with open("json/event_dictionary.json", "r") as file:
                data = json.load(file)
                eventList = data["eventList"]
                # st.write(eventList)
                # eventsList = [json.loads(line) for line in file]
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
            # print(eventListValue)
            # generate a list with all unique "eventName" names
            # check to see if there's only on dictionary 'event' entry in the entire "eventList" list, if so create a list from it so it follows convention and can be used
            # in st.selectbox still later on from the "eventName" st.selectbox dropdown list
            if isinstance(eventListValue, dict):
                eventListValue = [eventListValue]
            # print(eventListValue)

            # first creates a set of unique "eventName" values taken from the "eventList" key value pair 'eventListValue' (value of the key-value pair)
            masterEventsList = list(
                set(value["eventName"] for value in eventListValue))
            masterEventsList.sort()
            # print(masterEventsList)

        # st.header("Minter Admin Console")
        st.markdown("<p style='color: white; font-size: 28px; margin-top: 0px;'><u><b>3.) Minter Request Admin Console:</b></u></p>",
                    unsafe_allow_html=True)
        # st.write("Event Contract Generator Form:")
        # st.write("File: ticketholder.sol -> contract.functions.mint")
        # st.write("")
        # st.write("")
        # # Set Maximum Tickets to Batch/Sell
        # st.write("Set Maximum Tickets Available for Mint/Purchase:")
        # # for trial purposes set to max Massey Hall gallery size
        # _maxNumberOfTickets = st.number_input("Enter max tickets", 1217)
        # if st.button("Set Max Tickets"):
        #     set_max_tickets = contract.functions.setMAX_TICKETS(
        #         _maxNumberOfTickets).transact({"from": selected_address})
        #     tx_receipt = w3.eth.waitForTransactionReceipt(set_max_tickets)
        #     st.write("Transaction receipt:", tx_receipt)

        # new added 03/15/2023
        # create code to get the 'unique_id' from the json/event_dictionary to get all info required to fill form to generate tickets
        # function for obtaining all unique ids, therefore all scheduled events possible to autocomplete form more efficient

        # def obtain_all_unique_ids():
        #     with open("json/event_dictionary.json", 'r') as file:
        #         data = json.load(file)
        #         eventList = data["eventList"]
        #         unique_ids = list(set(value["unique_id"]
        #                           for value in eventList))
        #         unique_ids.sort()
        #         return unique_ids

        # # call obtain_all_unique_ids
        # masterUniqueIds = obtain_all_unique_ids()

        # _unique_ids = st.selectbox(
        #     "Select event (unique_id):", masterUniqueIds)

        # create function to produce new dictionary that uses 'unique_id' as the key and value is dictionary of 'unique_id' properties/components
        def obtain_all_unique_ids():
            with open("json/event_dictionary.json", 'r') as file:
                data = json.load(file)
                eventList = data["eventList"]
                unique_ids_dict = {}
                for value in eventList:
                    unique_id = value["unique_id"]
                    unique_ids_dict[unique_id] = {
                        "eventName": value["eventName"],
                        "venueName": value["venueName"],
                        "dateTime": value["dateTime"],
                        "hourTime": value["hourTime"],
                        "timeStamp": value["timeStamp"],
                        "smartContract": value["smartContract"],
                        "seatJSONBinURL": value["seatJSONBinURL"]
                    }
                # print(unique_ids_dict)
                return unique_ids_dict

        # call the obtain all unique ids function and save returned dictionary to variable
        masterUniqueIdsDictionary = obtain_all_unique_ids()

        # create 'unique_Ids' list based on the above dictionary & sort() alphabetically
        masterUniqueIdsList = list(masterUniqueIdsDictionary.keys())
        masterUniqueIdsList.sort()

        _uniqueId = st.selectbox(
            "Select event (unique_id): ", masterUniqueIdsList, key='masterUniqueIdsList_2')
        # print('_uniqueId: ', _uniqueId)

        if _uniqueId:
            _uniqueIdValues = masterUniqueIdsDictionary[_uniqueId]
            _eventName = _uniqueIdValues["eventName"]
            _venueName = _uniqueIdValues["venueName"]
            _dateTime = _uniqueIdValues["dateTime"]
            _hourTime = _uniqueIdValues["hourTime"]
            _timeStamp = int(_uniqueIdValues["timeStamp"])
            _smartContract = _uniqueIdValues["smartContract"]
            _seatContract = _uniqueIdValues["seatJSONBinURL"]

        # Form text_input & unique_id selected output prior to batch minting nft ticket
        # _ownerFirstName = st.text_input(
        #     "enter string memory _ownerFirstName", "First Name")
        # _ownerLastName = st.text_input(
        #     "enter string memory _ownerLastName", "Last Name")

        # _ownerFirstName "first name" string holder
        _ownerFirstName = "first name"
        # _ownerLastName "last name" string holder
        _ownerLastName = "last name"
        # _seatColor = "#5A5A5A" hex color string holder, dark grey indicating a seat has been purchase (last resort to call from blockchain to determine objective seatColor)
        _seatColor = "#5A5A5A"

        st.write("")
        st.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'><u>Information to be Added to Blockchain Metadata:</u></p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'>string memory _ownerFirstName:  <span style='color:green'> first name </span></p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'>string memory _ownerLastName:  <span style='color:green'> last name </span></p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'>string memory _eventName: <span style='color:green'> {}</span></p>".format(_eventName),
                    unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'>string memory _venueName: <span style='color:green'> {}</span></p>".format(_venueName),
                    unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'>string memory _concertDate [UNIX Format]: <span style='color:green'> {}</span></p>".format(_timeStamp),
                    unsafe_allow_html=True)
        st.write("")
        st.markdown("<p style='color: white; font-size: 14px; margin-top: 0px;'><u>Additional Event JSON Data:</u></p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'>_dateTime: <span style='color:green'> {}</span></p>".format(_dateTime),
                    unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'>_hourTime: <span style='color:green'> {}</span></p>".format(_hourTime),
                    unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'>_smartContract address: <span style='color:green'> {}</span></p>".format(_smartContract),
                    unsafe_allow_html=True)
        st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'>_seatContract JSON Bin URL: <span style='color:green'> {}</span></p>".format(_seatContract),
                    unsafe_allow_html=True)
        st.write("")

        print("_timeStamp :", _timeStamp)
        print("_timeStamp type() :", type(_timeStamp))

        # st.write("Set Maximum Tickets Available for Mint/Purchase:")
        # for trial purposes set to max Massey Hall gallery size

        def return_total_venue_seats(_venueName):
            # Open the venue_template_json .json file that corresponds to the accompanying _venueName and set as data

            json_path = os.path.join(
                "json/venue_template_json", f'{_venueName}.json')
            print("json_path: ", json_path)
            with open(json_path, 'r') as file:
                data = json.load(file)

            # Get a list of all unique seat names from seat value in list of sections
            uniqueSeatNames = set()
            for venue_section in data["venueSections"]:
                for section_name, section_data in venue_section.items():
                    for seat_name, seat_data in section_data.items():
                        uniqueSeatNames.add(seat_data["name"])

            # Get total number of unique seats from the length of uniqueSeatNames
            numberOfSeats = len(uniqueSeatNames)

            return numberOfSeats

        _total_venue_seats = return_total_venue_seats(_venueName)

        _maxNumberOfTickets = st.number_input(
            "Enter maximum number of tickets to be minted (default placeholder value is max venue capacity):", _total_venue_seats)
        # if st.button("Set Max Tickets"):
        #     set_max_tickets = contract.functions.setMAX_TICKETS(
        #         _maxNumberOfTickets).transact({"from": selected_address})
        #     tx_receipt = w3.eth.waitForTransactionReceipt(set_max_tickets)
        #     st.write("Transaction receipt:", tx_receipt)

        if contract.address == _smartContract:

            # Create function to set maximum number of tickets (placeholder dependant on max venue capacity size)
            if st.button("Set Max Tickets"):
                set_max_tickets = contract.functions.setMAX_TICKETS(
                    _maxNumberOfTickets).transact({"from": selected_address})
                tx_receipt = w3.eth.waitForTransactionReceipt(set_max_tickets)
                st.write("Transaction receipt:", tx_receipt)

            # Create function using API to recover the eth_cad_rate

            @st.cache(allow_output_mutation=True)
            def retrieve_eth_cad_conversion():
                response = requests.get(
                    'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=cad')
                cad_to_eth_exchange_rate = response.json()
                return float(cad_to_eth_exchange_rate['ethereum']['cad'])

            # Implement a button that automatically locks in the current eth_cad_rate without repetitively recalling the coingecko API (careful of timeouts if mutation set to FALSE)
            if st.button("Set current ETH/CAD rate"):
                eth_cad_rate = retrieve_eth_cad_conversion()
                st.write("Current ETH/CAD conversion rate: ", eth_cad_rate)

            # Clear caches in order to recall API from above 'retrieve_eth_cad_conversion' functions. This will reset and clear the cache until 'retrieve_eth_cad_conversion' is run again
            if st.button("Refresh & Recall ETH/CAD API"):
                st.runtime.legacy_caching.clear_cache()
                st.success(
                    "ETH/CAD cache cleared. Press 'Set current ETH/CAD rate to retrieve new rate from API.")

            print("current eth_cad_rate: ", retrieve_eth_cad_conversion())

            st.success(
                'unique_id event _smartContract address compatible to connected contract. Max Ticket & Mint Batch function buttons unlocked.')
            container_1.success("Matched to 'Minter Request Admin' Console")

            # Using the selected '_uniqueId' event .json file sort out and store the unique sec, row & seat number
            # unique_secs = set()
            # unique_rows = set()
            # unique_seat_number = set()

            # Iterate through the venue sections
            event_file_path = f'event_venue_library/{_uniqueId}'
            with open(event_file_path, 'r') as file:
                event_json_dict = json.load(file)

                # Create a list to hold all unqiue venue sections to refine selection on where to start batch minting in the venue
                section_names = []
                for venue_dict in event_json_dict["venueSections"]:
                    all_seats_minted = True
                    for section_key, section_value in venue_dict.items():
                        mintable_seats_exist = False
                        # print("section_key: ", section_key)

                        for seat_key, seat_value in section_value.items():
                            if not seat_value["minted"]:
                                mintable_seats_exist = True
                                all_seats_minted = False
                                break
                        if mintable_seats_exist:
                            section_names.append(section_key)
                    if all_seats_minted:
                        section_names.remove(section_key)
                        # print("section_value: ", section_value)
                        # if any(not seat_data["minted"] for seat_data in section_value.values()):
                        #     section_names.append(section_key)
                venueSectionSelected = st.selectbox(
                    "Venue Section To Mint: ", list(set(section_names)))

                # Create an empty list holder for select batch group of seats
                selected_batch_seats_list = []

                if venueSectionSelected:
                    # Retrieve the section dictionary corresponding to the selected venue section
                    section_dict = next((section for section in event_json_dict["venueSections"] if section.get(
                        venueSectionSelected)), None)

                    # Generate section_value dictionary & save to said variable based on the section_key (venueSectionSelected) from above
                    if section_dict:
                        section_key = venueSectionSelected
                        section_value = section_dict[section_key]

                        # Generate list of unique "sec" values in the selected section based on selected 'venueSectionSelected'
                        sec_values = sorted(list(set(
                            seat_data["sec"] for seat_data in section_value.values() if not seat_data["minted"])))

                        if sec_values:
                            # Generate a selectbox for the unique "sec" values
                            sec_selected = st.selectbox(
                                "Section ('sec') To Mint: ", sec_values)

                            # Filter & refine the row options available within 'sec' that have not been "minted" yet
                            row_options = [seat_data["row"] for seat_data in section_value.values(
                            ) if seat_data["sec"] == sec_selected and not seat_data["minted"]]

                            # Create list of unique "row" values for the selected "sec" value
                            row_values = sorted(set(row_options))

                            # Admin prompted to refine seat minting options down to "row" within selected "sec"
                            row_selected = st.selectbox(
                                "Row ('row') To Mint: ", row_values)

                            # Prompt user to enter batch size of tickets to mint into NFTs
                            batchSize = st.number_input(
                                "Enter event ticket batch size (minting genesis: 0 to seatsMintedSoFar, nth batch afterwards: _seatsMintedSoFar += numToMint)", 0)

                            # Filter down to the seat options available to the admin that are still able to be minted
                            seat_options = [seat_data["seat number"] for seat_data in section_value.values(
                            ) if seat_data["sec"] == sec_selected and seat_data["row"] == row_selected and not seat_data["minted"]]

                            # Create a list of unique "name" (seat names) for the selected "row" value
                            seat_values = sorted(set(seat_options), key=int)
                            # print("seat_values: ", seat_values)

                            # Write out to the admin the seats still available that haven't been minted into NFT seats
                            # seat_number_selected = st.selectbox(
                            #     "Available seat options: ", seat_values)

                            # Split the seat numbers into batches
                            try:
                                seat_batch_groups = [seat_values[i: i + batchSize]
                                                     for i in range(0, len(seat_values), batchSize)]
                                # print("seat_batch_groups: ", seat_batch_groups)

                                # Important: If last batch is < batch size, take the remainder batch group to its own list on the seat_batch_groups list
                                if len(seat_batch_groups) > 0 and len(seat_batch_groups[-1]) < batchSize:
                                    # Remove & return the last remainder element on the list
                                    remainderBatch = seat_batch_groups.pop()
                                    seat_batch_groups.append(remainderBatch)

                                # Construct a list of customized labels for the dropdown list to present to the admin user
                                seat_batch_groups_labels = [
                                    f"{(batch[0])}:{(batch[-1])}" for batch in seat_batch_groups]

                                # Generate a selectbox for user to choose from with dropdown (st.selectbox)
                                # *** Important: added 05/01/2023 -> st.empty() container created to hold seat dropdown list items to be used for refresh after minting to remove minted seats dynamically
                                seat_container_1 = st.empty()

                                # seat_batch_group_selected = st.selectbox( <-- Original before st.empty() variable was added
                                seat_batch_group_selected = seat_container_1.selectbox(
                                    "Seat(s) ('seat number') Range To Mint: ", seat_batch_groups_labels,  key=f"first_invoke_of_seat_container_1")
                                # print("seat_batch_group_selected: ",
                                #       seat_batch_group_selected)

                                # Display the seat_batch_group_selected in a printout format
                                st.write("Seat groups selected:",
                                         seat_batch_group_selected)

                                # Create the lower & upper bound int from the seat_batch_group_selected range
                                start, end = [
                                    int(num) for num in seat_batch_group_selected.split(":")]

                                # Create a list of integers based on the lower & upper limit values in the mini-list of seat_batch_group_selected_numbers
                                seat_batch_group_selected_numbers = list(
                                    range(start, end + 1))
                                # print("seat_batch_group_selected_numbers: ",
                                #       seat_batch_group_selected_numbers)

                                # Retrieve the metadata from the original seat_data (seat_options) by filtering out only the seats selected based on "seat number" (seat_data["seat number"])
                                # selected_batch_seats_list = []
                                selected_batch_seats_list.clear()
                                for seat_num in seat_batch_group_selected_numbers:
                                    for seat in section_value.values():
                                        if seat["sec"] == sec_selected and seat["row"] == row_selected and not seat["minted"]:
                                            #print("seat: ", seat)
                                            if int(seat["seat number"]) == seat_num:
                                                selected_batch_seats_list.append(
                                                    seat)
                                                break
                                # print("selected_batch_seats_list: ",
                                #      selected_batch_seats_list)
                                # st.experimental_set_buffer(0)
                                st.write("selected_batch_seats_list: ",
                                         selected_batch_seats_list)

                                # Perform fiat currency/wei conversion (i.e. CAD/wei)
                                eth_cad_rate = retrieve_eth_cad_conversion()

                                # Batch Mint Function
                                try:
                                    if st.button("Mint Batch"):
                                        # Create empty list for 'pending' transaction hashes
                                        tx_hashes_list = []
                                        for seat in selected_batch_seats_list:
                                            if not seat["minted"] or seat["minted"] == False or seat["minted"] == "false":
                                                _gweiValue = int(
                                                    ((seat["price"]["CAD"]/eth_cad_rate)) * 1000000000)
                                                _seatName = seat["name"]
                                                _batchSize = 1

                                                mint = contract.functions.mint(
                                                    _ownerFirstName,
                                                    _ownerLastName,
                                                    _eventName,
                                                    _timeStamp,
                                                    _gweiValue,
                                                    _venueName,
                                                    _seatName,
                                                    _seatColor,
                                                    _batchSize
                                                ).transact({'from': selected_address})

                                                # Get the tx_hash from the raw transaction
                                                tx_hash = mint.hex()

                                                # Get seat name of the seat that will be minted
                                                # i.e. 'Sec 100 Row A Seat 1':
                                                # seat_dict_holder = {
                                                #     seat["name"]: tx_hash}

                                                seat_dict_holder = {
                                                    "name": seat["name"],
                                                    "tx_hash": tx_hash,
                                                    "_gweiValue": _gweiValue
                                                }

                                                # Append pending transaction tx_hash to the tx_hashes_list to be awaiting updating the event .json "minted" = tx_hash
                                                tx_hashes_list.append(
                                                    seat_dict_holder)
                                                # print("tx_hashes_list: ",
                                                #      tx_hashes_list)

                                        st.write(
                                            "Transaction Hash List: ", tx_hashes_list)

                                        # Create empty list to hold finalized 'mint pending' list of seats that are in the process of being queued for minting
                                        mint_pending_seats = []

                                        # Iterate through all venue sections & seats in the event_venue_library/{_uniqueId}
                                        event_file_path = f'event_venue_library/{_uniqueId}'
                                        with open(event_file_path, 'r') as file:
                                            event_json_dict = json.load(file)

                                            # Create a list to hold all unique venue sections to refine selection on where to start batch minting in the venue
                                            section_names = []
                                            for venue_dict in event_json_dict["venueSections"]:
                                                # all_seats_minted = True
                                                for section_key, section_value in venue_dict.items():
                                                    # mintable_seats_exist = False
                                                    # print("section_key: ", section_key)
                                                    for seat_key, seat_value in section_value.items():
                                                        # Update event .json with seat["minted"] = tx_hash pending status hash to be used later to confirm mint successful with tx_receipt manually
                                                        for seat_placeholder in tx_hashes_list:
                                                            if seat_key == seat_placeholder["name"] and not seat_value["minted"]:
                                                                # Replace the seat_value["minted"]: false with seat_value["minted"]: "tx_hash" value
                                                                seat_value["minted"] = seat_placeholder["tx_hash"]
                                                                # Add the updated _gweiValue to the seat_value["price"] sub-dictionary so there's the CAD and wei values stored
                                                                seat_value["price"]["_gweiValue"] = seat_placeholder["_gweiValue"]

                                                                # Append the seat_value that had its seat_value["minted"] updated to the tx_hash value to the mint_pending_seats list
                                                                mint_pending_seats.append(
                                                                    seat_value)
                                                                # st.write(
                                                                #     seat_value)

                                        # Update the unique event .json file now with the updated changes to seat["minted"] = tx_hash after the minting process to store the hashes to lookup on the blockchain later to get a tx_receipt to confirm completion
                                        with open(event_file_path, 'w') as file:
                                            json.dump(event_json_dict,
                                                      file, indent=4)
                                        # Print success and notify admin of updated event .json seat["minted"] tx_hash mint pending value
                                        st.success(
                                            "Mint Batch Pending Completed. Check back for tx_receipt later.")
                                        # Print the mint_pending_seats list for the most current batch just currently queued for batch mint
                                        st.write(
                                            "Mint Pending Seats List: ", mint_pending_seats)

                                        # *** Important: added 05/01/2023 -> st.empty() container created to hold seat dropdown list items to be used for refresh after minting to remove minted seats dynamically
                                        event_file_path = f'event_venue_library/{_uniqueId}'
                                        with open(event_file_path, 'r') as file:
                                            event_json_dict = json.load(file)

                                            # Create a list to hold all unqiue venue sections to refine selection on where to start batch minting in the venue
                                            section_names = []

                                            # Create variable for selectbox_counter_num to keep track of unique st.selectbox (selectbox_container_1 dropdown boxes) used to dynamically updated seats that have already been minted, required unfortunately
                                            selectbox_counter_num = 0

                                            for venue_dict in event_json_dict["venueSections"]:
                                                all_seats_minted = True
                                                for section_key, section_value in venue_dict.items():
                                                    mintable_seats_exist = False
                                                    # print("section_key: ", section_key)

                                                    for seat_key, seat_value in section_value.items():
                                                        if not seat_value["minted"]:

                                                            # *** Important: added 05/01/2023 -> st.empty() container created to hold seat dropdown list items to be used for refresh after minting to remove minted seats dynamically
                                                            # With mint batch completed, now filter the remaining seats that can still be minted
                                                            remaining_seats_to_mint = [seat_value["seat number"] for seat_value in section_value.values(
                                                            ) if seat_value["sec"] == sec_selected and seat_value["row"] == row_selected and not seat_value["minted"]]

                                                            # Update the dropdown list with seats that still qualify to be minted
                                                            with seat_container_1:
                                                                st.selectbox(
                                                                    "Seat(s) ('seat number') Range To Mint: ", [
                                                                        f"{(batch[0])}:{(batch[-1])}" for batch in seat_batch_groups if len(set(batch) & set(remaining_seats_to_mint)) > 0], key=f"selectbox-{sec_selected}-{row_selected}-{selectbox_counter_num}"
                                                                )
                                                                selectbox_counter_num += 1
                                except Exception as e:
                                    st.write(
                                        "Batch transaction hashing (tx_hash): ", e)

                            except:
                                st.warning(
                                    "Batch size must be greater than zero.")

                # for key, value in seat.items():
                # print("key: ", key)
                # print("values: ", value)

            # def cad_to_wei_converter():
            #     _price_CAD = st.number_input("Enter uint _price (in $CAD)", 0)
            #     # Put in API request to api.coingecko.com/api to obtain ETH/CAD exchange rate
            #     response = requests.get(
            #         'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=cad')
            #     cad_to_eth_exchange_rate = response.json()
            #     eth_cad_rate = float(
            #         cad_to_eth_exchange_rate['ethereum']['cad'])
            #     # CAD to ETH
            #     ethValue = _price_CAD / eth_cad_rate
            #     # Conversion of ETH to wei
            #     weiValue = w3.toWei(ethValue, 'ether')
            #     _priceConversionOutput = st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'>price in $ CAD and wei: <span style='color:white'> ${} CAD</span>, <span style='color:green'> [{:,} wei]</span></p>".format(_price_CAD, weiValue),
            #                                          unsafe_allow_html=True)

            #     return _priceConversionOutput

            # **** new added 03/16/2023

            # _venueName = st.text_input(
            #    "Enter string memory _venueName", "Venue Name")
            # _seatColor = "#5A5A5A"
            # batchSize = st.number_input(
            #     "Enter event ticket batch size (minting genesis: 0 to seatsMintedSoFar, nth batch afterwards: _seatsMintedSoFar += numToMint)", 0)

            # CAD to Gwei/wei converter function

            # *** Keep function for final conversion to send into Solidity below
            # Gwei to wei converter function
            # _price = int(gwei_price * 10**9)  # in wei

            # Mint batchSize of Tickets
            # if st.button("Mint Batch"):
            #     mint = contract.functions.mint(_ownerFirstName, _ownerLastName,
            #                                    _eventName, 1660176000, weiValue, _venueName, _seatColor, batchSize).transact({"from": selected_address})
            #     tx_receipt = w3.eth.waitForTransactionReceipt(mint)
            #     st.write("Transaction receipt:", tx_receipt)

        else:
            st.warning('Warning: unique_id event _smartContract address not compatible to connected contract. Please select corresponding unique_id event from above selectbox.', icon="⚠️")
            container_1.warning(
                'Unmatched to Minter Request Admin Console event (_uniqueId)')
        # Enter CAD ticket price using CoinGecko API
        # def cad_to_gwei_converter(_price_CAD):

        #     # Put in API request to api.coingecko.com/api to obtain ETH/CAD exchange rate
        #     response = requests.get(
        #         'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=cad')
        #     cad_to_eth_exchange_rate = response.json()
        #     eth_cad_rate = float(cad_to_eth_exchange_rate['ethereum']['cad'])
        #     # CAD to ETH
        #     ethValue = _price_CAD / eth_cad_rate
        #     # Conversion of ETH to wei
        #     weiValue = w3.toWei(ethValue, 'ether')

        #     return weiValue

        # #     "Enter uint _concertDate [UNIX Format]", 1660176000)
        # _price_CAD = st.number_input("Enter uint _price (in $CAD)", 0)
        # weiValue = cad_to_gwei_converter(_price_CAD)
        # st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'>price in $ CAD and wei: <span style='color:white'> ${} CAD</span>, <span style='color:green'> [{:,} wei]</span></p>".format(_price_CAD, weiValue),
        #             unsafe_allow_html=True)

        # def cad_to_wei_converter():
        #     _price_CAD = st.number_input("Enter uint _price (in $CAD)", 0)
        #     # Put in API request to api.coingecko.com/api to obtain ETH/CAD exchange rate
        #     response = requests.get(
        #         'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=cad')
        #     cad_to_eth_exchange_rate = response.json()
        #     eth_cad_rate = float(cad_to_eth_exchange_rate['ethereum']['cad'])
        #     # CAD to ETH
        #     ethValue = _price_CAD / eth_cad_rate
        #     # Conversion of ETH to wei
        #     weiValue = w3.toWei(ethValue, 'ether')
        #     _priceConversionOutput = st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'>price in $ CAD and wei: <span style='color:white'> ${} CAD</span>, <span style='color:green'> [{:,} wei]</span></p>".format(_price_CAD, weiValue),
        #                                          unsafe_allow_html=True)

        #     return _priceConversionOutput

        # # **** new added 03/16/2023

        # # _venueName = st.text_input(
        # #    "Enter string memory _venueName", "Venue Name")
        # _seatColor = "#5A5A5A"
        # batchSize = st.number_input(
        #     "Enter event ticket batch size (minting genesis: 0 to seatsMintedSoFar, nth batch afterwards: _seatsMintedSoFar += numToMint)", 0)

        # # CAD to Gwei/wei converter function

        # # *** Keep function for final conversion to send into Solidity below
        # # Gwei to wei converter function
        # # _price = int(gwei_price * 10**9)  # in wei

        # # Mint batchSize of Tickets
        # if st.button("Mint Batch"):
        #     mint = contract.functions.mint(_ownerFirstName, _ownerLastName,
        #                                    _eventName, 1660176000, weiValue, _venueName, _seatColor, batchSize).transact({"from": selected_address})
        #     tx_receipt = w3.eth.waitForTransactionReceipt(mint)
        #     st.write("Transaction receipt:", tx_receipt)


with col2:
    # st.header("NFT Image Constructor")
    st.markdown("<p style='color: white; font-size: 28px; margin-top: 0px;'><u><b>1.) Venue Generator & Admin Database:</b></u></p>",
                unsafe_allow_html=True)

    # Load the venues_dictionary.json from JSON file
    with open("json/venues_dictionary.json", "r") as file:
        venues_dictionary_json = json.load(file)

    # Form Submission for Venue Addition
    venue_name = st.text_input("Venue name: ")
    section_name = st.text_input("Section name: ")
    section_function_name = st.text_input("Section function name: ")

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
                    venues_dictionary_json[venue_name][section_name] = section_function_name
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
                    section_name: section_function_name}
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
                    # st.write(f"{sectionName}: {sectionFunction.__name__}")
                i += 1
        venue_database()

    #########################################################

    # Minter Transaction Receipt Generator

    #########################################################

    # Minting Transaction Confirmation Receipt Requester
    st.markdown("<p style='color: white; font-size: 28px; margin-top: 0px;'><u><b>4.) Minter Transaction Receipt Generator (Final):</b></u></p>",
                unsafe_allow_html=True)

    # call the obtain all unique ids function and save returned dictionary to variable
    masterUniqueIdsDictionary = obtain_all_unique_ids()

    # create 'unique_Ids' list based on the above dictionary & sort() alphabetically
    masterUniqueIdsList = list(masterUniqueIdsDictionary.keys())
    # add a 'None' placeholder so the st.selectbox list will default on 'None' and not set off the conditions of the other if statements to keep dashboard generic
    masterUniqueIdsList.sort()
    masterUniqueIdsList = [None] + masterUniqueIdsList

    _uniqueId = st.selectbox(
        "Select event (unique_id): ", masterUniqueIdsList)

    if _uniqueId:
        _uniqueIdValues = masterUniqueIdsDictionary[_uniqueId]
        _eventName = _uniqueIdValues["eventName"]
        _venueName = _uniqueIdValues["venueName"]
        _dateTime = _uniqueIdValues["dateTime"]
        _hourTime = _uniqueIdValues["hourTime"]
        _timeStamp = int(_uniqueIdValues["timeStamp"])
        _smartContract = _uniqueIdValues["smartContract"]
        _seatContract = _uniqueIdValues["seatJSONBinURL"]

    if contract.address == _smartContract and _uniqueId != None:
        container_1.success(
            "Matched to 'Minter Transaction Receipt Generator (Final)'")
    else:
        container_1.warning(
            "Unmatched to 'Minter Transaction Receipt Generator (Final)'")

    if _uniqueId != None:
        # Iterate through the venue sections
        event_file_path = f'event_venue_library/{_uniqueId}'
        with open(event_file_path, 'r') as file:
            event_json_dict = json.load(file)

            # Create a list to hold all unique venue sections to refine selection on where to start updating the minting status (find all seats minted=True)
            section_names_2 = []
            for venue_dict in event_json_dict["venueSections"]:
                all_seats_minted = True
                for section_key, section_value in venue_dict.items():
                    mintable_seats_exist = False
                    # print("section_key: ", section_key)

                    for seat_key, seat_value in section_value.items():
                        if seat_value["minted"] not in [False, True, "false", "true", "True", "False"]:
                            mintable_seats_exist = True
                            all_seats_minted = False
                            break
                    if mintable_seats_exist:
                        section_names_2.append(section_key)

                if all_seats_minted and len(section_names_2) > 0:
                    section_names_2.remove(section_key)
                    # print("section_value: ", section_value)
                    # if any(not seat_data["minted"] for seat_data in section_value.values()):
                    #     section_names.append(section_key)
            venueSectionSelected = st.selectbox(
                "Venue Section To Update: ", list(set(section_names_2)))

            # Create an empty list holder for select batch group of seats
            selected_batch_seats_list = []

            if venueSectionSelected:
                # Retrieve the section dictionary corresponding to the selected venue section
                section_dict = next((section for section in event_json_dict["venueSections"] if section.get(
                    venueSectionSelected)), None)

                # Generate section_value dictionary & save to said variable based on the section_key (venueSectionSelected) from above
                if section_dict:
                    section_key = venueSectionSelected
                    section_value = section_dict[section_key]

                    # Generate list of unique "sec" values in the selected section based on selected 'venueSectionSelected'
                    sec_values = sorted(list(set(
                        seat_data["sec"] for seat_data in section_value.values() if seat_data["minted"] not in [False, True, "false", "true", "True", "False"])))

                    if sec_values:
                        # Generate a selectbox for the unique "sec" values
                        sec_selected = st.selectbox(
                            "Section ('sec') To Update Mint Status ['minted']: ", sec_values)

                        # Filter & refine the row options available within 'sec' that have not been "minted" yet
                        row_options = [seat_data["row"] for seat_data in section_value.values(
                        ) if seat_data["sec"] == sec_selected and seat_data["minted"] not in [False, True, "false", "true", "True", "False"]]

                        # Create list of unique "row" values for the selected "sec" value
                        row_values = sorted(set(row_options))

                        # Admin prompted to refine seat minting options down to "row" within selected "sec"
                        row_selected = st.selectbox(
                            "Row ('row') To Update Mint Status ['minted']: ", row_values)

                        # Prompt user to enter batch size of tickets to mint into NFTs
                        batchSize = st.number_input(
                            "Enter ticket batch size (to lookup to confirm minted status): ", 0, key="batchSize_tx_receipt")

                        # Filter down to the seat options available to the admin that are still able to be minted
                        seat_options = [seat_data["seat number"] for seat_data in section_value.values(
                        ) if seat_data["sec"] == sec_selected and seat_data["row"] == row_selected and seat_data["minted"] not in [False, True, "false", "true", "True", "False"]]

                        # Create a list of unique "name" (seat names) for the selected "row" value
                        seat_values = sorted(set(seat_options), key=int)
                        # print("seat_values: ", seat_values)

                        # Split the seat numbers into batches
                        try:
                            seat_batch_groups = [seat_values[i: i + batchSize]
                                                 for i in range(0, len(seat_values), batchSize)]
                            # print("seat_batch_groups: ", seat_batch_groups)

                            # Important: If last batch is < batch size, take the remainder batch group to its own list on the seat_batch_groups list
                            if len(seat_batch_groups) > 0 and len(seat_batch_groups[-1]) < batchSize:
                                # Remove & return the last remainder element on the list
                                remainderBatch = seat_batch_groups.pop()
                                seat_batch_groups.append(remainderBatch)

                            # Construct a list of customized labels for the dropdown list to present to the admin user
                            seat_batch_groups_labels = [
                                f"{(batch[0])}:{(batch[-1])}" for batch in seat_batch_groups]

                            # Generate a selectbox for user to choose from with dropdown (st.selectbox)
                            # *** Important: added 05/01/2023 -> st.empty() container created to hold seat dropdown list items to be used for refresh after minting to remove minted seats dynamically
                            seat_container_1 = st.empty()

                            # seat_batch_group_selected = st.selectbox( <-- Original before st.empty() variable was added
                            seat_batch_group_selected = seat_container_1.selectbox(
                                "Seat(s) ('seat number') Range To Update Mint Status [minted']: ", seat_batch_groups_labels,  key=f"third_invoke_of_seat_container_1")
                            # print("seat_batch_group_selected: ",
                            #       seat_batch_group_selected)

                            # Display the seat_batch_group_selected in a printout format
                            st.write("Seat groups selected:",
                                     seat_batch_group_selected)

                            # Create the lower & upper bound int from the seat_batch_group_selected range
                            start, end = [
                                int(num) for num in seat_batch_group_selected.split(":")]

                            # Create a list of integers based on the lower & upper limit values in the mini-list of seat_batch_group_selected_numbers
                            seat_batch_group_selected_numbers = list(
                                range(start, end + 1))
                            # print("seat_batch_group_selected_numbers: ",
                            #       seat_batch_group_selected_numbers)

                            # Retrieve the metadata from the original seat_data (seat_options) by filtering out only the seats selected based on "seat number" (seat_data["seat number"])
                            # selected_batch_seats_list = []
                            selected_batch_seats_list.clear()
                            for seat_num in seat_batch_group_selected_numbers:
                                for seat in section_value.values():
                                    if seat["sec"] == sec_selected and seat["row"] == row_selected and seat["minted"] not in [False, True, "false", "true", "True", "False"]:
                                        #print("seat: ", seat)
                                        if int(seat["seat number"]) == seat_num:
                                            selected_batch_seats_list.append(
                                                seat)
                                            break
                            # print("selected_batch_seats_list: ",
                            #      selected_batch_seats_list)
                            # st.experimental_set_buffer(0)
                            st.write("selected_batch_seats_list: ",
                                     selected_batch_seats_list)

                            try:
                                # Create markdown text to indicate to admin user button will check tx_hash on chain & update seat['minted'] = True if tx_receipt is confirmed
                                st.write(
                                    "Check tx_hashes on-chain & update event .json minted status if completed on selected batch size:")
                                # st.button for "Confirm Mint Status"
                                if st.button("Update Mint Status"):

                                    # *** added 05/05/2023

                                    tx_receipt_list = []
                                    for seat in selected_batch_seats_list:
                                        if seat["minted"] not in [False, True, "false", "true", "True", "False"]:

                                            # important: get the transaction hash from the previous tx_hash request that was saved to the unique event .json ["minted"] key/value pair
                                            tx_hash = seat["minted"]
                                            # _batchSize = 1

                                            # get transaction receipt
                                            tx_receipt = w3.eth.getTransactionReceipt(
                                                tx_hash)

                                            # If the transaction receipt exists (minting completed) assign a temp key/value seat['minted'] = True
                                            # Important: Use tx
                                            if tx_receipt is not None:
                                                seat["minted"] = True
                                                log = tx_receipt['logs'][0]
                                                token_Id = int(
                                                    log['data'][-64:], 16)
                                                print("token_Id: ", token_Id)

                                            seat_dict_holder = {
                                                "name": seat["name"],
                                                "minted": True,
                                                "tx_receipt": tx_receipt,
                                                "tokenID": token_Id
                                            }

                                            # Append pending transaction tx_hash to the tx_hashes_list to be awaiting updating the event .json "minted" = tx_hash
                                            tx_receipt_list.append(
                                                seat_dict_holder)

                                    st.write(
                                        "Transaction Receipt List: ", tx_receipt_list)

                                    # Create empty list to hold finalized 'mint pending' list of seats that are in the process of being queued for minting
                                    confirm_minted_seats = []

                                    # Iterate through all venue sections & seats in the event_venue_library/{_uniqueId}
                                    event_file_path = f'event_venue_library/{_uniqueId}'
                                    with open(event_file_path, 'r') as file:
                                        event_json_dict = json.load(file)

                                        # Create a list to hold all unique venue sections to refine selection on where to start batch minting in the venue
                                        section_names = []
                                        for venue_dict in event_json_dict["venueSections"]:
                                            # all_seats_minted = True
                                            for section_key, section_value in venue_dict.items():
                                                # mintable_seats_exist = False
                                                # print("section_key: ", section_key)
                                                for seat_key, seat_value in section_value.items():
                                                    # Update event .json with seat["minted"] = tx_receipt (minting completed receipt) status
                                                    for seat_placeholder in tx_receipt_list:
                                                        if seat_key == seat_placeholder["name"] and seat_value["minted"] not in [False, True, "false", "true", "True", "False"]:
                                                            seat_value["minted"] = seat_placeholder["minted"]
                                                            seat_value["tokenID"] = seat_placeholder["tokenID"]
                                                            # seat_value["minted"] = seat_placeholder["tx_receipt"]
                                                            # Append the seat_value that had its seat_value["minted"] updated to the tx_hash value to the mint_pending_seats list
                                                            confirm_minted_seats.append(
                                                                seat_value)
                                                            # st.write(
                                                            #     seat_value)

                                    # Update the unique event .json file now with the updated changes to seat["minted"] = tx_hash after the minting process to store the hashes to lookup on the blockchain later to get a tx_receipt to confirm completion
                                    with open(event_file_path, 'w') as file:
                                        json.dump(event_json_dict,
                                                  file, indent=4)
                                    # Print success and notify admin of updated event .json seat["minted"] tx_hash mint pending value
                                    st.success(
                                        "Confirmation of mint status & status updated. See below for confirmed minted tickets (seats).")
                                    # Print the mint_pending_seats list for the most current batch just currently queued for batch mint
                                    st.write(
                                        "Mint Pending Seats List: ", confirm_minted_seats)

                            except Exception as e:
                                st.write("Error: ", e)

                        except:
                            st.warning(
                                "Batch size must be greater than zero.")

    # for i in range(15):
    #     st.write("")
    # st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'><b>Remix IDE Hyperlink:</b></p>",
    #             unsafe_allow_html=True)
    # st.write("https://remix-beta.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.17+commit.8df45f5f.js")

#########################################################


#########################################################

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
    # print(f"ticketId [key]", ticketId)
    # print(f"info [value]", info)
    for key, value in info.items():
        # print(f'key:', key)
        # print(f'value:', value)
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
    # print(f"ticketId [key]", ticketId)
    # print(f"info [value]", info)
    for key, value in info.items():
        # print(f'key:', key)
        # print(f'value:', value)
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
            int(_timeStamp))  # UNIX timestamp variable inputs here
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
        # background = Image.open("Image_Data/black_background_ticket.png")
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
        # foreground = foreground.resize((200, 200))

        # Overlay the text_info_bottom_left text onto the left bottom corner of the black template background image
        background.alpha_composite(
            text_info_bottom_left, (10, (background.height - text_info_bottom_left.height) - 10))

        # Overlay the artwork image onto the center of the black template background image
        background.alpha_composite(
            artwork, ((background.width-artwork.width)//2, (background.height-artwork.height)//2 - 50))

        #########################################################

        # QR Code Generator

        # text = "testing"

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

        # qr_code = segno.make(text)
        # qr_code.save("test.png", scale=7)
        # print(segno.__version__)

        #########################################################

        # Save as NFT ticket
        background.save(
            f"NFT_Tickets/NFT_ticket_{event_text}_{venue_text}_{selected_seat_text}.png")

#########################################################
