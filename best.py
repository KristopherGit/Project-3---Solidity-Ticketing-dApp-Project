# Works DO NOT ALTER THIS IS THE BEST TRIAL VERSION YET (SEE TEXT BELOW FOR INTERACTION WITH ETHEREUM SMART CONTRACT)

import streamlit as st
import plotly.graph_objs as go

# Create a dictionary that holds the attributes of each seat but first reference it with session_state seats already coded

"st.session_state object:", st.session_state

seats = {
    'A0': {'name': 'A0', 'price': 10, 'bought': False, 'color': 'black'},
    'A1': {'name': 'A1', 'price': 10, 'bought': False, 'color': 'red'},
    'A2': {'name': 'A2', 'price': 10, 'bought': False, 'color': 'red'},
    'A3': {'name': 'A3', 'price': 10, 'bought': False, 'color': 'red'},
    'A4': {'name': 'A4', 'price': 10, 'bought': False, 'color': 'red'},
    'A5': {'name': 'A5', 'price': 10, 'bought': False, 'color': 'red'},
    'A6': {'name': 'A6', 'price': 10, 'bought': False, 'color': 'red'},
    'A7': {'name': 'A7', 'price': 10, 'bought': False, 'color': 'red'}
    # ... Add more seats
}


# Use session state
# for seat_name in st.session_state.keys():
#    for seat in seats.keys():
#        if (seat_name == seat):
#            seats[seat]['color'] = 'green'

if st.session_state:
    for seat_name in st.session_state.keys():
        for seat in seats.keys():
            if (seat_name == seat):
                seats[seat]['color'] = 'green'

else:
    st.write("Session state is empty.")


# Create a function that generates a grid of seats


def create_seat_grid():
    seat_traces = []
    for seat_name, seat_attributes in seats.items():
        seat_trace = go.Scatter(
            x=[seat_attributes['name'][0]],
            y=[seat_attributes['name'][1]],
            mode='markers',
            marker=dict(
                size=10,
                color=seat_attributes['color']
            ),
            text=seat_name,
            hoverinfo='text'
        )
        seat_traces.append(seat_trace)
    return seat_traces


# Create a selectbox to select a seat
selected_seat = st.selectbox('Select a seat', list(seats.keys()))

# Create a button to change the color of the selected seat
if st.button('Change seat color'):
    # Here you would call the smart contract function to change the color of the seat
    # and update the value of the seat in the dictionary
    seats[selected_seat]['color'] = 'green'
    # Here you would save the updated dictionary to a JSON file

    if selected_seat not in st.session_state:
        st.session_state[selected_seat] = seats[selected_seat]['color'] = 'green'

# Add session state to track 'session_state' of seats[selected_seat]['color'] = 'green' color

# key: value pairing
# "st.session_state object:", st.session_state ---> Moved to top
# if selected_seat not in st.session_state:
#    st.session_state[selected_seat] = seats[selected_seat]['color'] = 'green'


# Create a graph that shows the grid of seats
st.plotly_chart(go.Figure(data=create_seat_grid()))


print("Difference between 'seats.items()' & 'seats'")
print("seats.items()")
print(seats.items())
print()
print()
print()
print("seats:")
print(seats)


"""I'm glad you found it helpful. The next step would be to integrate the application with the Ethereum smart contract. This can be done using a library like web3.py which allows you to interact with Ethereum nodes using JSON-RPC.

Here's an example of how you can use web3.py to interact with a smart contract:

python
Copy code
from web3 import Web3

# Connect to the Ethereum node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# The address of the smart contract
contract_address = '0x742d35Cc6634C0532925a3b844Bc454e4438f44e'

# The ABI (Application Binary Interface) of the smart contract
contract_abi = [...]

# Create a contract object
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Call a function of the smart contract
result = contract.functions.get().call()

# Send a transaction to the smart contract
tx_hash = contract.functions.set(1234).transact()
You can use this code to call functions of the smart contract, and to send transactions to the smart contract.

You can also use the eth-abi library to encode and decode the function calls and the transaction data.

Please let me know if you have any questions or need any more help."""
