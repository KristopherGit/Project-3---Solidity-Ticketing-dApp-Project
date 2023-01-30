pragma solidity ^0.5.17; 

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";

contract XP_Token {

    using SafeMath for uint; 

    address payable owner = msg.sender;
    string public symbol = "XPT"; 
    uint public exchange_rate = 100; 

    mapping(address => uint) balances; 

    function balance() public view returns(uint) {
        returns balances[msg.sender]; 
    } // getter function

    function transfer(address recepient, uint value) public {
        balances[msg.sender] = balances[msg.sender].sub(value); 
        balances[recipient] = balances[recepient].add(value);
    }

    function purchase() public payable {
        uint amount = msg.value.mul(exchange_rate); 
        balances[msg.sender] = balances[msg.sender].add(amount)
    }


}