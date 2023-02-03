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

#img = qrcode.make("test")
# img.save("test.png")
# print("test")
