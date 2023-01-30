pragma solidity ^0.5.0; 

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";

contract ArcadeToken{

    using SafeMath for uint; 

    address payable owner = msg.sender; // represents entity currently sending a message. i.e. whoever initially assigns this 
    // it only occurs once and never again (contract address is set to the owner only)

    string public symbol = "ARCD";

    uint public exchange_rate = 100; 

    mapping(address => uint) balances; 

    function balance() public view returns (uint){
        return balances[msg.sender];
    }

    function transfer(address recipient, uint value) public{
        balances[msg.sender] = balances[msg.sender].sub(value);
        balances[recipient] = balances[recipient].add(value);
    }

    function purchase() public payable{
        uint amount = msg.value * exchange_rate;
        balances[msg.sender] +=amount;
        owner.transfer(msg.value);
    }

    function mint(address recepient, uint value) public{
        require(msg.sender == owner, "You can't mint tokens as you are not the owner!"); 
        balances[recepient]+=value;
    }
    /*
    function exchangeWeiForTokens(uint256 _wei) public payable {
        require(_wei >= 50); // Ensure minimum wei value is accepted
        uint256 tokens = _wei.div(50); // 1 token per 50 wei
        require (tokens > 0); // Handle division by zero errors 
        msg.sender.transfer(tokens); // Transfer the tokens to the sender
    } */






}