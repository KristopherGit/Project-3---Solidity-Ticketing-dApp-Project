// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0; 

//import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/ERC721.sol";
//import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
// not found import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/ERC721Full.sol";


//import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
//import "@openzeppelin/contracts/utils/Counters.sol";
//import "./node_modules/@openzeppelin/contracts/token/ERC721/ERC721.sol";        

contract TickETHolder is ERC721 {
        address payable public contractOwner;
        // Instantiate instance of the maximum total number of concert tickets to be minted (public viewable call variable)
        uint256 public MAX_TICKETS;
        // Instantiate instance of the ticketCount variable
        uint256 public ticketCount;
        // Instantiate _seatsMintedSoFar as a global variable to keep track of while minting
        // Set initially to 0, once contract is deployed it will update
        uint256 public _seatsMintedSoFar = 0; 
    // Structure of the TickETHholder TicketData obj 
    struct TicketData {
        // Owner Info
        address owner;
        string ownerFirstName;
        string ownerLastName;
        // Specific Event Info (Band/Event Info)
        string eventName; 
        uint concertDate; // use UNIX data format (use a convert site i.e. UNIX -> https://www.unixtimestamp.com/
        uint price; 
        // Venue Info
        string venueName;
        uint seatNumber;
        // GUI streamlit / plotly reference variable (ties to session_state reference & enables GUI seat map update realtime)
        string seatColor;
    }
    // Structure of the TickETHolder SoldData obj
    struct SoldData {
        uint seatNumber; 
        uint seatColor;
    }

    // i.) Mapping tokenID -> ticket metadata for each individual ticket (tokenID -> ticketData[i])
    // Note: ticketData is *private* 
    mapping(uint256 => TicketData) private ticketData; 
    // ii.) Mapping tokenID -> 
    //mapping(uint256 => SoldData) public soldData;

    // Create constructor
    constructor() ERC721("TickETHolder", "TETH") {
        // set owner of the contract as the one that deploys the contract 
        contractOwner =  payable(msg.sender);
        //contactOwner = msg.sender;
        ticketCount=0;
    }

    // Create mint function to produce all tickets for the event at once (modify if advance ticket sale required)
    function mint(
            //address payable contractOwner,
            string memory _ownerFirstName,
            string memory _ownerLastName,
            string memory _eventName,
            uint _concertDate,
            uint _price, 
            string memory _venueName,
            //uint _seatNumber,
            string memory _seatColor, 
            uint batchSize
        ) public {
        require(msg.sender == contractOwner, "Only the contract owner[deployer] can mint tickets.");

        uint remaining = MAX_TICKETS - _seatsMintedSoFar;
        uint numToMint = remaining > batchSize ? batchSize : remaining;
        for (uint i = _seatsMintedSoFar; i < _seatsMintedSoFar + numToMint; i++) {
                // Mint a ticket with seat number `i`

                // Make requirement that the number of tickets minted is not over the MAX_TICKETS value indicated above
                require(ticketCount < MAX_TICKETS, "Max tickets for venue has been reached."); 
                // Increment total ticket count as mint function iterates through all tickets being minted
                ticketCount++;

                // Mint ticket with specific metadata
                ticketData[ticketCount].owner = contractOwner;
                ticketData[ticketCount].ownerFirstName = _ownerFirstName;
                ticketData[ticketCount].ownerLastName = _ownerLastName;
                ticketData[ticketCount].eventName = _eventName;
                ticketData[ticketCount].concertDate = _concertDate; 
                ticketData[ticketCount].price = _price;
                ticketData[ticketCount].venueName = _venueName;
                //ticketData[ticketCount].seatNumber = _seatsMintedSoFar; 
                ticketData[ticketCount].seatNumber = i; 
                ticketData[ticketCount].seatColor = _seatColor;
            }
            _seatsMintedSoFar += numToMint;
        }

    function setMAX_TICKETS (uint _maxNumberOfTickets) public {
        require(msg.sender == contractOwner);
        MAX_TICKETS = _maxNumberOfTickets;
    }

    function getSeatsMintedSoFar() public view returns (uint) {
        return _seatsMintedSoFar;
    }

    event TicketPurchased(uint ticketId, address buyer, uint price);

    function buyTicket(uint ticketId) public payable {
        // Make sure to purchase the ticket the ticket is available (i.e. set to the contractOwner, so it's still in unsold stasis/pool of minted tickets
        require(ticketData[ticketId].owner == contractOwner, "Ticket isn't available for sale. Already sold. Sorry. Try to purchase a different seat, please.");

        // Make sure the buyer has enough money to buy the ticket
        require(msg.value >= ticketData[ticketId].price, "Insufficent funds.");

        // Send required funds from buyer -> contractOwner (owner)
        contractOwner.transfer(msg.value);

        // Reset the status of the ticketData attribute for the buyer's address to be the new owner ('address owner')
        ticketData[ticketId].owner = msg.sender;

        // Broadcast sale has been made & transfer of ticket to msg.sender (buyer) has been completed
        emit TicketPurchased(ticketId, msg.sender, ticketData[ticketId].price);
    }

    function getTicketDetails(uint256 tokenId) public view returns (
        address owner,
        string memory ownerFirstName,
        string memory ownerLastName,
        string memory eventName,
        uint concertDate,
        uint price,
        string memory venueName,
        uint seatNumber,
        string memory seatColor
) {
        owner = ticketData[tokenId].owner;
        ownerFirstName = ticketData[tokenId].ownerFirstName;
        ownerLastName = ticketData[tokenId].ownerLastName;
        eventName = ticketData[tokenId].eventName;
        concertDate = ticketData[tokenId].concertDate;
        price = ticketData[tokenId].price;
        venueName = ticketData[tokenId].venueName;
        seatNumber = ticketData[tokenId].seatNumber;
        seatColor = ticketData[tokenId].seatColor;
}

}
