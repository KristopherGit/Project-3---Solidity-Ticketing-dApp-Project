pragma solidity ^0.5.0; // defining which compiler version of Solidiy to implement

contract BankAccount {


    function withdrawal(uint amount, address payable recepient) public {

    return recepient.transfer(amount); 

    }

    function deposit() public payable {

    }

    function () external payable {
        
    }


}