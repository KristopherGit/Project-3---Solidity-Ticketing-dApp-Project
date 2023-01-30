pragma solidity ^0.5.0; 

contract CustomerAccount {

address payable owner = 0x0c0669Cd5e60a6F4b8ce437E4a4A007093D368Cb; 
bool isNewAccount; 
uint public accountBalance;
string customerName; 
string customerLastName;
address payable authorizedRecepient = 0x7A1f3dFAa0a4a19844B606CD6e91d693083B12c0; 

function getInfo() view public returns (address, bool, address payable, uint, string memory, string memory) {

    return(owner, isNewAccount, authorizedRecepient, accountBalance, customerName, customerLastName);

}

function sendRemittance(uint amount, address payable recepient) public {
    require(recepient==owner || recepient==authorizedRecepient, "This address is not authorized!");
    recepient.transfer(amount);
    accountBalance = address (this).balance; 
}

 function setInfo(address payable newOwner, bool newAccountStatus, uint newAccountBalance, string memory newCustomerName, string memory newCustomerLastName) public {
        owner = newOwner;
        isNewAccount = newAccountStatus;
        accountBalance = newAccountBalance;
        customerName = newCustomerName;
        customerLastName = newCustomerLastName;
    }


function deposit() public payable {

    accountBalance = address(this).balance;
}

function() external payable {
    accountBalance = address(this).balance;
}

}