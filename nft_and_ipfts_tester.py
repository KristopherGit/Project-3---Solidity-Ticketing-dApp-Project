# nftgen & ipfsgen function tester

# Import segno library (QR Code Generator)
import segno
import qrcode

# Import PIL Image Editor
from PIL import Image, ImageFont, ImageDraw, ImageOps

# Import datetime for UNIX data conversions
import datetime

# Import JSON Request Library
import requests

import pinata
from pinata_api_keys import PINATA_API_KEY, PINATA_SECRET_API_KEY, PINATA_ACCESS_TOKEN
import requests
import json
import plotly.graph_objs as go

# **** Import classes
# def nft_generator(traces, ticket_id, event_select, venue_select, selected_seat):
from nftgen import nft_generator
from ipfsgen import ipfs_gen  # def ipfs_gen(nft_filepath):


# Traces file partial
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


ticket_id = 2
event_select = "Gorillaz"
venue_select = "Massey Hall"
selected_seat = "Seat 57"

# nft_generator(traces, ticket_id, event_select, venue_select, selected_seat)
nft_url = nft_generator(traces, ticket_id, event_select,
                        venue_select, selected_seat)

# ipfs_generator()
ipfsHash_img = ipfs_gen(nft_url, event_select, venue_select, selected_seat)

print(ipfsHash_img)
