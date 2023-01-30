# Project 3
# tickETHolder dApp - Interactive Decentralized Token & Ticketing Service
## <i> Proposal </i>


<p align= "left" width="50">
<img width= "15%" src="tickETHolder_logo.png">
</p>

---
## <i>Overview of the Project</i>
---

## <b>Project Purpose:</b>

The purpose of this project is to develop a decentralized concert/event dApp. The project purports to have the following functionality & compartmentalization: 
<ol> i.) <b> Front End </b> - The front end of this project will be coded in python utilizing libraries including PIL, Streamlit, and Plotly. Within Streamlit, the user will be able to select from a venue's gallery seating selection and choose the recommended number / location of seats and interact with a visual GUI of the unique venue. The Streamlit dApp will contain form input fields, st.buttons/st.selectbox widgets in order to provide user info, ETH account interaction (expanded further upon in Back End), user account data (potentially), & submission. The user will then be presented with confirmed log data, transaction hashes that their seat has been purchased and the user takes an ERC020 token representing the ticket is deposited into their ETH account wallet. 
<br>
<br> ii.) <b> Back End </b> - The back end of this project will include the programming for the ticket token objects/account addresses via Solidity. There would be some consideration made over the precise architecture of the code's attributes and how to handle the minting, selling and transferring of these tickets, but may replicate or have similarities to a crowd-sale type architecture.
<br>
<br> iii.) <b> Testing </b> - Testing would be required in order to make sure all transactions go through, seats are accounted for and serialized & hashed with unique identifiers, etc. The debate would be to what would be handled in a separate - if required database - or what can be handled on-chain. Simple unique hashing could be handled on chain and not consume substantial resources, most likely.
<br>
<br> iv.) <b> Security </b> - This may expand past the scope of the capabilities of this project, but security auditing would be an ideal addition to the project in order to handle any vulnerabilities to customer information or mishandling of duplicate seats, etc. being sold or generated. 
<br>
<br> v.) <b> NFT Expanded Capabilities </b> - Ideally, it would be beneficial for this project to also include NFT capabilities such as .png type info contained on the ticket NFT that could be examined/experimented with for potential lucrative promotional, collectible or marketable undertakings.




---

