import pinata
from pinata_api_keys import PINATA_API_KEY, PINATA_SECRET_API_KEY, PINATA_ACCESS_TOKEN
import requests
import json

# Create an instance of the Pinata API using your API key and secret API key
#pinata_api = pinata.Pinata(api_key=PINATA_API_KEY, secret_api_key=PINATA_SECRET_API_KEY)


def ipfs_gen(nft_filepath):
    pinata_api = pinata.Pinata(
        api_key=PINATA_API_KEY, secret_key=PINATA_SECRET_API_KEY, access_token=PINATA_ACCESS_TOKEN)

    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    payload = {'pinataOptions': '{"cidVersion": 1}',
               'pinataMetadata': '{"name": "NFT Ticket", "keyvalues": {"company": "Pinata"}}'}
    files = [
        ('file', (f'{nft_filepath}', open(
            f'/Users/chris/Desktop/Git/Project-3---Solidity-Ticketing-dApp-Project/{nft_filepath}', 'rb'), 'application/octet-stream'))
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

    ipfsHash_img = 'https://gateway.pinata.cloud/ipfs/' + \
        response.json()['IpfsHash']

    return ipfsHash_img
