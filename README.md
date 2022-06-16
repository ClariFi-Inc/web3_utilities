# ClariFi, Inc - Web3 Utility Methods/Helpers
Various tutorials, utilities,  and helper methods for working with Web3, primarily utilizing Python.

## Code / Project Purpose
This code is provided to help people new to blockchain/Web3 programming understand how to interact 
with the blockchain.  Some of the examples we'll be providing include:

- Retrieving a transaction's detailed information
- Getting the latest price of AVAX in $USD
- How to interact with a project's smart contract and call a read function
- How to interact with a project's smart contract and call a 'write' function
- How to get price of a transaction's token at the time of a transaction, when swapped through a decentralized exchange
- Ensuring proper handling of private keys when interacting with a Web3 smart contract through scripts

There will be additional tutorials for the Avalanche blockchain, including:

- Setting up an Avalanche Subnet
- Creating NFT's on Avalanche


These examples will hopefully help people quickly get up-to-speed on 
understanding how to interact with Web3 ecosystems.

> **Note**: If you have a specific example/tutorial you'd like to see sooner than later, send us a message at 
info@clarifi.xyz and we'll see what we can make happen!


### Donations
If you find any of the code/examples in this repo we would greatly appreciate donations. You may send donations to the following Wallet Address:

**0x3143c205FB04812d8Cd27C9EE901050dDD6996dc**

We prefer AVAX, as we are collecting AVAX to create an Avalanche validator node, however, 
any and all donations are appreciated!


## PyEnv and Poetry
This project utilizes the pyenv and poetry modules for Python.

## .env_example
This project utilizes python-decouple.  The example .env_example file should be copied to the 
project's root directory as **.env** and updated as appropriate.

## Example Scripts
The Makefile contains shortcuts to a few of the example code in the project to make it 
easier for someone new to run the example code.  You can run:

```$ make help```

To see the entire list of make targets available.  Some of the available targets are:

```shell

Avalanche Network: 
    make avax_gas_fee_watcher              outputs the current avax network gas fee every 3 seconds 

```


## This code is provided as-is under the MIT Open Source License
