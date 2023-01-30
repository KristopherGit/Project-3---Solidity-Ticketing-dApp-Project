pragma solidity ^0.5.0; 

contract LatestTrade {

    string coin = "BTC"; 
    uint price; 
    bool isBuyOrder; 

// setter function
    function updateTrade(string memory newCoin, uint newPrice, bool isBuy) public {

        coin = newCoin; 
        price = newPrice; 
        isBuyOrder = isBuy; 
        
    }

}