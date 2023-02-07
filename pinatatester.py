import pinata
from pinata_api_keys import PINATA_API_KEY, PINATA_SECRET_API_KEY, PINATA_ACCESS_TOKEN
import requests
import json

# Create an instance of the Pinata API using your API key and secret API key
#pinata_api = pinata.Pinata(api_key=PINATA_API_KEY, secret_api_key=PINATA_SECRET_API_KEY)
pinata_api = pinata.Pinata(
    api_key=PINATA_API_KEY, secret_key=PINATA_SECRET_API_KEY, access_token=PINATA_ACCESS_TOKEN)

url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

payload = {'pinataOptions': '{"cidVersion": 1}',
           'pinataMetadata': '{"name": "NFT Gorillaz Massey Hall Seat 46", "keyvalues": {"company": "Pinata"}}'}
files = [
    ('file', ('NFT_ticket_Gorillaz_Massey_Hall_Seat_2.png', open(
        '/Users/chris/Desktop/Git/Project-3---Solidity-Ticketing-dApp-Project/NFT_Tickets/NFT_ticket_Gorillaz_Massey Hall_Seat 46.png', 'rb'), 'application/octet-stream'))
]
headers = {
    # 'Authorization': Bearer 'PINATA_ACCESS_TOKEN'
    'pinata_api_key': PINATA_API_KEY,
    'pinata_secret_api_key': PINATA_SECRET_API_KEY
}

response = requests.request(
    "POST", url, headers=headers, data=payload, files=files)

# Print the IPFS hash
print("The JSON response is:", response.json())
print("The ipfsHash is: ", response.json()['IpfsHash'])
print("The NFT viewable link: ", 'https://gateway.pinata.cloud/ipfs/' +
      response.json()['IpfsHash'])

ipfsHash = 'https://gateway.pinata.cloud/ipfs/' + response.json()['IpfsHash']
