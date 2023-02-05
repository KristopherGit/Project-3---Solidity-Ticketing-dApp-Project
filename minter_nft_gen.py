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
col1, col2 = st.columns([1, 1], gap="medium")

# Sidebar Main Logo Image
# Main Logo Addition Function


@st.cache
def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo


st.sidebar.image(
    add_logo(logo_path="tickETHolder_logo.png", width=500, height=500))
st.sidebar.write("NFT Image Data Input")

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

#########################################################

# Minter Program

# Show minter_layout header

with col1:
    st.header("Minter & NFT Gen Admin Console")
    st.write("Event Contract Generator Form:")
    st.write("File: ticketholder.sol -> contract.functions.mint")
    st.write("")
    st.write("")
    _ownerFirstName = st.text_input(
        "Enter string memory _ownerFirstName", "First Name")
    _ownerLastName = st.text_input(
        "Enter string memory _ownerLastName", "Last Name")
    _eventName = st.text_input("Enter string memory _eventName", "Event Name")
    _concertDate = st.number_input(
        "Enter uint _concertDate [UNIX Format]", 1660176000)
    _price = st.number_input("Enter uint _price (ETH)", 0.071)
    _venueName = st.text_input("Enter uint _price", "Venue Name")

with col2:
    st.header("Links")
    st.write("col2 test")

    # contract.functions.mint(_owner)

    # //address payable contractOwner,
    # string memory _ownerFirstName,
    # string memory _ownerLastName,
    # string memory _eventName,
    # uint _concertDate,
    # uint _price,
    # string memory _venueName,
    # string memory _seatColor,
    # uint batchSize

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
        event_ticket_holders = "Gorillaz"
        venue_ticket_holders = "Massey Hall"

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
