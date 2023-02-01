pragma solidity ^0.5.0; 

//import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/ERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract TickETHolder is ERC721 {
        address public contractOwner;
        // Instantiate instance of the maximum total number of concert tickets to be minted (public viewable call variable)
        uint256 public MAX_TICKETS;
        // Instantiate instance of the ticketCount variable
        uint256 public ticketCount;
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
    mapping(uint256 => SoldData) public soldData;

    // Create constructor
    constructor() public {
        // set owner of the contract as the one that deploys the contract 
        contractOwner = msg.sender;
        ticketCount=0;
    }

    // Create mint function to produce all tickets for the event at once (modify if advance ticket sale required)
    function mint(
        address _owner,
        string memory _ownerFirstName,
        string memory _ownerLastName,
        string memory _eventName,
        uint _concertDate,
        uint _price, 
        string memory _venueName,
        uint _seatNumber,
        string memory _seatColor
    ) public {
    // Make requirement that the number of tickets minted is not over the MAX_TICKETS value indicated above
    require(ticketCount < MAX_TICKETS, "Max tickets for venue has been reached."); 
    // Increment total ticket count as mint function iterates through all tickets being minted
    ticketCount++;

    // Mint ticket with specific metadata
    ticketData[ticketCount].owner = _owner;
    ticketData[ticketCount].ownerFirstName = _ownerFirstName;
    ticketData[ticketCount].ownerLastName = _ownerLastName;
    ticketData[ticketCount].eventName = _eventName;
    ticketData[ticketCount].concertDate = _concertDate; 
    ticketData[ticketCount].price = _price;
    ticketData[ticketCount].venueName = _venueName;
    ticketData[ticketCount].seatNumber = _seatNumber; 
    ticketData[ticketCount].seatColor = _seatColor;
    }

    function setMAX_TICKETS (uint _maxNumberOfTickets) private {
        require(msg.sender == contractOwner);
        MAX_TICKETS = _maxNumberOfTickets;
    }
}
