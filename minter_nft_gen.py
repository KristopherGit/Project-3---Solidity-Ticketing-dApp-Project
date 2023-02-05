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
from PIL import Image, ImageFont, ImageDraw

# Import datetime for UNIX data conversions
import datetime

# Import JSON Request Library
import requests


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


#########################################################

#########################################################

# Minter Program

#########################################################


#########################################################

# NFT Image Gen Program

#########################################################

# * have it pull json data from JSONbin (all currently sold seats waiting for NFT gen) and convert json data to text
# i.e. Venue: Massey Hall, Performer: Gorillaz, Date: 1035901350 (UNIX -> MM/DD/YYYY format), Seat Number: 07

text = "testing"
qr_code = segno.make(text)
qr_code.save("test.png", scale=7)
print(segno.__version__)

# Create Event/Venue Info Text Box
white_blank = Image.open("Image_Data/white_blank_square.png")
black_blank = Image.open("Image_Data/black_blank_square.png")
font = ImageFont.truetype('/Library/Fonts/Arial Black.ttf', 12)
font_time_small = ImageFont.truetype('/Library/Fonts/Arial Black.ttf', 12)

draw = ImageDraw.Draw(black_blank)

# Create 'event_text' & 'venue_text' text variables to be added for event & venue info
event_text = "Gorillaz"
venue_text = "Massey Hall"

# Fetch UNIX event date stamp from Solidity and convert to formatted_date_time format ('%m/%d/%Y %H:%M:%S')
date_time = datetime.datetime.fromtimestamp(
    1660176000)  # UNIX timestamp variable inputs here
formatted_date_time = date_time.strftime('%m/%d/%Y %H:%M:%S')

# Create aisle, row & seat text variables
aisle_text = "Aisle 0"
row_text = "Row 2"
selected_seat_text = "Seat 2"

# Create info box ticket component

draw.text((0, 20), event_text, (255, 255, 255), font=font)
draw.text((0, 50), venue_text, (255, 255, 255), font=font)
draw.text((0, 80), formatted_date_time, (255, 255, 255), font=font_time_small)
draw.text((0, 110), aisle_text, (255, 255, 255), font=font)
draw.text((0, 140), row_text, (255, 255, 255), font=font)
draw.text((0, 170), selected_seat_text, (255, 255, 255), font=font)

# Draw image to 'draw' canvas and save as .png
black_blank.save("Image_Data/text_box.png")


#img = qrcode.make("test")
# img.save("test.png")
# print("test")
