pragma solidity ^0.5.0; 

contract LatestTrade {

    string coin ="XRP"; 
    uint price; 
    bool is_buy_order; 

    function updateTrade(string memory new_coin, uint new_price, bool is_buy) public { // setter function

        coin = new_coin; 
        price = new_price; 
        is_buy_order = is_buy; 

    }

    function getTrade() public view returns (string memory, uint, bool) {

        return (coin, price, is_buy_order); 

    }


}