#Import segno library (QR Code Generator)
import segno
import qrcode

# Import PIL Image Editor
from PIL import Image, ImageFont, ImageDraw, ImageOps

# Import datetime for UNIX data conversions
import datetime

# Import JSON Request Library
import requests

# Import urllib.parse to fix filepaths (to remove spaces that affect url hyperlinks)
import urllib.parse

# def nft_generator(traces, ticket_id, event_select, venue_select, selected_seat):
def nft_generator(nft_artwork_file_path, event_select, venue_select, date, time, selected_seat):

    # Access the row & aisle values from each trace (seat) that corresponds to each tokenId/seat number
#aisle = traces[ticket_id - 1]['x'][0]
#row = traces[ticket_id - 1]['y'][0]
    
#     aisle = selected_seat["sec"]
#     row = selected_seat["row"]

#     event_ticket_holders = event_select
#     venue_ticket_holders = venue_select

#     aisle_ticket_holders = selected_seat["sec"]
#     row_ticket_holders = selected_seat["row"]
#     seat_ticket_holders = selected_seat["name"]

    # Create Background Template to Overlay Foreground Images
    img = Image.new('RGB', (1000, 600), color='black')
    img.save('Image_Data/black_background_ticket.png')

    # Create Event/Venue Info Text Box
    white_blank = Image.open("Image_Data/white_blank_square.png")
    black_blank = Image.open("Image_Data/black_blank_square.png")
    font = ImageFont.truetype('/Library/Fonts/Arial Black.ttf', 13)
    font_time_small = ImageFont.truetype(
                '/Library/Fonts/Arial Black.ttf', 13)

    # Get Black Blank as Canvas Template
    draw = ImageDraw.Draw(black_blank)

    # Create 'event_text' & 'venue_text' text variables to be added for event & venue info
#     event_text = event_ticket_holders
#     venue_text = venue_ticket_holders
    event_text = event_select
    venue_text = venue_select

    # Fetch UNIX event date stamp from Solidity and convert to formatted_date_time format ('%m/%d/%Y %H:%M:%S')
#     date_time = datetime.datetime.fromtimestamp(
#             1660176000)  # UNIX timestamp variable inputs here
#     formatted_date_time = date_time.strftime('%m/%d/%Y %H:%M:%S')
#     date_time = datetime.datetime.fromtimestamp(
#             1660176000)  # UNIX timestamp variable inputs here
    formatted_date_time_text = str(date + " " + time)

    # Create aisle, row & seat text variables
#     aisle_text = "Aisle " + str(aisle_ticket_holders)
#     row_text = "Row " + str(row_ticket_holders)
    selected_seat_text = selected_seat["name"]

    # Create info box ticket component

#     draw.text((15, 20), event_text, (255, 255, 255), font=font)
#     draw.text((15, 50), venue_text, (255, 255, 255), font=font)
#     draw.text((15, 80), formatted_date_time,
#                   (255, 255, 255), font=font_time_small)
#     draw.text((15, 110), aisle_text, (255, 255, 255), font=font)
#     draw.text((15, 140), row_text, (255, 255, 255), font=font)
#     draw.text((15, 170), selected_seat_text, (255, 255, 255), font=font)
    
    draw.text((15, 80), event_text, (255, 255, 255), font=font)
    draw.text((15, 110), venue_text, (255, 255, 255), font=font)
    draw.text((15, 140), formatted_date_time_text,
                  (255, 255, 255), font=font_time_small)
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
    f"event_venue_library/nft_artwork/{nft_artwork_file_path}").convert('RGBA')

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
                    formatted_date_time_text + "," + "\n" +
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
    background.save(f"NFT_Tickets/NFT_ticket_{event_text}_{venue_text}_{selected_seat_text}.png") #-> change 02/13/2023 to fix hyperlinks for NFT Tickets in main app.py when 'retrieve tickets' is activated
    
    #file_name = f"NFT_Tickets/NFT_ticket_{event_text}_{venue_text}_{selected_seat_text}.png"
    
    #encoded_file_name = urllib.parse.quote(file_name)
    
    #background.save(encoded_file_name)
    
    # Save string to variable to return from function
    
    url = f"NFT_Tickets/NFT_ticket_{event_text}_{venue_text}_{selected_seat_text}.png"
    
    #url = encoded_file_name
    
    return url

    #########################################################