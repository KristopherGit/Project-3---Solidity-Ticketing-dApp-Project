# Concert Seat Selection Program GUI

# import tkinter library for GUI interface for geometry (tk as alias)
import tkinter as tk
from tkinter import *

# import streamlit library
# import streamlit as st

# create window with tkinter constructor
root = tk.Tk()

# set geometry ("X x Y pixels") & title
root.geometry("1280x720")
root.title("Meridian Seating Layout")

# main body labels, additional layout & textbox instantiation
label1 = tk.Label(root, text="Stage", font=('Arial', 16))
label1.pack(padx=10, pady=10)
label2 = tk.Label(root, text="Orchestra: 730 seats and 5 wheelchair locations",
                  font=('Arial', 14))
label2.pack(padx=10, pady=10)

#textbox = tk.Text(root, height=5, font=('Arial', 14))
# textbox.pack(padx=5)

# frame enables a container for button objects
# * (Tk [window container] (root) -> Frame [frame container] (buttonframe) -> Button.grid)
buttonframe = tk.Frame(root)
# (column #, weight= X)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 14))
# sticky enables anchoring to E corner
btn1.grid(row=0, column=0, sticky=tk.E)

# set the Button (btn1) inside of the Frame (buttonframe)
buttonframe.pack(fill='x')

# action button genesis & layout

button = tk.Button(root, text="Buy Ticket", font=('Arial', 12))
button.pack(padx=8, pady=8)

# Define Streamlit action button to open Tkinter window

# runs GUI window in streamlit
# st.pyplot(root.mainloop)

root.mainloop()


# def open_tk():
# subprocess.Popen([<interpreter>, <filepath>])
# os.system(<filepath>)
# os.system("seating.py")

@st.cache(allow_output_mutation=True)
def launch_tk():

    try:
        subprocess.run(["python", "seating.py"])
    except Exception as e:
        print(str(e))


st.sidebar.button("Massey Hall", launch_tk)

# Massey Hall Header
st.write("Massey Hall")

"""
# First Row of Concert Seats
st.radio(label='Mezzanine Level Seats', options=[
    'None', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10'])
st.write(
    '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
# Second Row of Concert Seats
st.radio(label="none", options=[
    'None', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10'], label_visibility="collapsed")
st.write(
    '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
# Third Row of Concert Seats
st.radio(label="none", options=[
    'None', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10'], label_visibility="collapsed")
st.write(
    '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
# First Row of Concert Seats
st.radio(label="none", options=[
    'None', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10'], label_visibility="collapsed")
st.write(
    '<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
"""

"""
# Create Concert Structure As A List of Seats

# Entire Gallery
gallery = []

# Row of Seats
row_1 = []

# Define each individual seat that can be customizable in terms of color (representing available (blue) or occupied (grey))

# Front Row Seating
seat_A0 = (10, 10)
seat_A1 = (12, 10)
seat_A2 = (14, 10)
seat_A3 = (16, 10)
seat_A4 = (18, 10)

# Set all seats into row_1 of gallery
row_1 = (seat_A0, seat_A1, seat_A2, seat_A3, seat_A4)

# Set concert_layout (scatter plot trace) of all the seats (points)
concert_layout = px.

# Show concert venue in 2-D
concert_layout.show()
"""
