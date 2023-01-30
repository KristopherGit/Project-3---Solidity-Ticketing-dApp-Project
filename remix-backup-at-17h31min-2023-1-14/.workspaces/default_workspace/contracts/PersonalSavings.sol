pragma solidity ^0.5.0; 


contract PersonalSavings {

address payable public public_savings=0x1B96e6710EF91E8642903f0348815654A27b2388; 
address payable private private_savings=0x9B8683f4Cff5369CB7da166B85d6B8EDD95abCE3;
string account_holder="Evil Dave";

function withdrawal(uint amount, address payable recepient) public {

    return recepient.transfer(amount); 

}

function deposit() public payable {

}

function () external payable {
    
}

}