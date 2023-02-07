# Import streamlit as GUI interface
import streamlit as st

# Import libraries to run Solidity smart contract & interact with json/files
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv

# Import segno library (QR Code Generator)
import segno
import qrcode

# Import PIL Image Editor
from PIL import Image, ImageFont, ImageDraw, ImageOps

# Import datetime for UNIX data conversions
import datetime

# Import JSON Request Library
import requests


#########################################################
# Setup Admin / Minter / NFT Gen Streamlit Web Interface
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


# Implement the contract helper function
# a.) Loads the contract only once using the streamlit cache feature
# b.) Connects to the contract once using the contract address & ABI

#########################################################

st.sidebar.markdown("<p style='color: white; font-size: 28px; margin-top: 0px;'><b><u>Admin Dashboard</u></b></p>",
                    unsafe_allow_html=True)
st.sidebar.image(
    add_logo(logo_path="tickETHolder_logo.png", width=500, height=500))

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

if st.sidebar.button("Update Contract Address"):
    with open(".env", "w") as env_file:
        env_file.write(
            "WEB3_PROVIDER_URI=http://127.0.0.1:7545\n"
            f"SMART_CONTRACT_ADDRESS={current_smart_contract_address}")
        st.success("New contract address has been updated successfully.")
    os.environ.update(dict(line.strip().split('=') for line in open('.env')))

# Load the contract ABI
# @st.cache(allow_output_mutation=True)
# def load_contract():
#    with open(Path('./contracts/compiled/ticketholder_abi.json')) as f:
#        ticketholder_abi = json.load(f)
#        contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
#        contract = w3.eth.contract(
#            address=contract_address,
#            abi=ticketholder_abi
#        )
#
#    return contract

with open(Path('./contracts/compiled/ticketholder_abi.json')) as f:
    # with open(Path(f'./contracts/compiled/{abi_contract_file_name}')) as f:
    ticketholder_abi = json.load(f)
    #abi = json.load(f)

    # Set the contract address (Ethereum address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=ticketholder_abi
        # abi=abi

    )

#########################################################


#contract = load_contract()

if contract is None:
    st.sidebar.write("Unable to connect to the deployed contract.")
    st.sidebar.markdown("<p style='color: red; font-size: 16px; margin-top: 0px;'><b>Unable to Connect to ETH Test Network.</b></p>",
                        unsafe_allow_html=True)
else:
    st.sidebar.markdown("<p style='color: green; font-size: 16px; margin-top: 0px;'><b>Successfully connected to the deployed contract at address:.</b></p>",
                        unsafe_allow_html=True)
    st.sidebar.write(contract.address)
#########################################################

abi_contract_file = st.sidebar.file_uploader(
    "Upload the ABI contract (.json) file", type=["json"])

# Add 'Deploy Contract' button to deploy the contract to the Ethereum network
if st.sidebar.button("Connect to ABI"):
    if abi_contract_file is not None:
        st.write("Filename: ", abi_contract_file.name)
        abi_contract_file_name = abi_contract_file.name
        contract = load_contract(abi_contract_file_name)
    # if contract is not None:
    #    st.sidebar.write(
    #        "Successfully connected to the deployed contract at address:", contract.address)
    # else:
    #    st.sidebar.write("Unable to connect to the deployed contract.")
# Admin Dashboard


# getTicketDetails)
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

    # getSeatsMintedSoFar
st.sidebar.markdown("<p style='color: white; font-size: 20px; margin-top: 0px;'><b><u>getSeatsMintedSoFar</u></b></p>",
                    unsafe_allow_html=True)
if st.sidebar.button("Seats Minted (So Far)"):
    seats_minted_so_far = contract.functions.getSeatsMintedSoFar().call()
    st.sidebar.write("Total Seats Minted (So Far): ", seats_minted_so_far)

    # getSeatsMintedSoFar
st.sidebar.markdown("<p style='color: white; font-size: 20px; margin-top: 0px;'><b><u>MAX_TICKETS</u></b></p>",
                    unsafe_allow_html=True)
if st.sidebar.button("Get Max Tickets"):
    max_tix = contract.functions.MAX_TICKETS().call()
    st.sidebar.write("Maximum number of tickets : ", max_tix)


# Show minter_layout header

with col1:
    with st.container():
        #st.header("Minter Admin Console")

        # Set Maximum Tickets to Batch/Sell
        st.write("Set Maximum Tickets Available for Mint/Purchase:")
        # for trial purposes set to max Massey Hall gallery size
        _maxNumberOfTickets = st.number_input("Enter max tickets", 1217)
        if st.button("Set Max Tickets"):
            set_max_tickets = contract.functions.setMAX_TICKETS(
                _maxNumberOfTickets).transact({"from": selected_address})
            tx_receipt = w3.eth.waitForTransactionReceipt(set_max_tickets)
            st.write("Transaction receipt:", tx_receipt)

        st.markdown("<p style='color: white; font-size: 28px; margin-top: 0px;'><u><b>Minter Admin Console:</b></u></p>",
                    unsafe_allow_html=True)
        st.write("Event Contract Generator Form:")
        st.write("File: ticketholder.sol -> contract.functions.mint")
        st.write("")
        st.write("")
        _ownerFirstName = st.text_input(
            "Enter string memory _ownerFirstName", "First Name")
        _ownerLastName = st.text_input(
            "Enter string memory _ownerLastName", "Last Name")
        _eventName = st.text_input(
            "Enter string memory _eventName", "Event Name")
        _concertDate = st.number_input(
            "Enter uint _concertDate [UNIX Format]", 1660176000)
        gwei_price = st.number_input("Enter uint _price (in Gwei)", 71000000)
        _venueName = st.text_input(
            "Enter string memory _venueName", "Venue Name")
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
    st.markdown("<p style='color: white; font-size: 28px; margin-top: 0px;'><u><b>NFT Image Constructor:</b></u></p>",
                unsafe_allow_html=True)
    for i in range(10):
        st.write("")
    st.markdown("<p style='color: white; font-size: 16px; margin-top: 0px;'><b>Remix IDE Hyperlink:</b></p>",
                unsafe_allow_html=True)
    st.write("https://remix-beta.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.17+commit.8df45f5f.js")


# Run main sidebar program


# Load the ticketholder Ethereum contract
#contract = load_contract()

#########################################################

#########################################################

# Minter Program


# Load Minter Admin Wallet & Additional Wallet Options
# Setup access to user Ethereum eth.accounts (MetaMask)
# Drop down for eth wallet addresses ('selected_address') from customer


# Declare contract variable to hold contract that can be held when load_contract() function is invoked later from file_uploader & Deploy
#contract = None
#########################################################
# Solidity Contract Load
# Implement the @st.cache to cache the contract object


# @st.cache(allow_output_mutation=True)
# def load_contract(solidity_contract_file, abi_contract_file_path):
#    if solidity_contract_file is not None:
#        with open(abi_contract_file_path, 'r') as abi_file:
#            abi = json.load(abi_file)

#        bytecode = solidity_contract_file.read()
#        contract_filename = solidity_contract_file.name
#        contract_instance = w3.eth.contract(
#            abi=abi,
#            bytecode=bytecode
#        )

# deploy contract to ETH network
#        selected_address = w3.eth.accounts[0]
#        tx_hash = contract_instance.constructor().transact(
#            {"from": selected_address})
#        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#        st.write(
#            f"ETH Solidity contract: '{contract_filename}'. Deployed at ETH address:", tx_receipt["contractAddress"])
#        return contract_instance
#    else:
#        st.write(
#            "Unable to load. No contract file (.sol) selected.")
#        return None
#########################################################


# Main Sidebar App
# def main_sidebar():

#########################################################


# Create & Call 'update_seat_colors' function that pulls updated seat colors from JSONbin based on sold seats

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

print(ticket_holders)

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

        #print("values[i]:", value[0], value[1], value[2], value[3], value[4], value[5])


#########################################################


#########################################################

# NFT Image Gen Program

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

#########################################################

# Minter Program

#########################################################
