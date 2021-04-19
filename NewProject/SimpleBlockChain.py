import hashlib
import json
from time import time
from datetime import date


class Blockchain(object):
    def __init__(self):
        self.chain = []

        #todo: when users send our coins to each other, their transactions will sit in this array until we approve & add them to a new block.
        self.pending_transactions = [] 

        #todo: add each block to the chain
        self.new_block(previous_hash="The Times {0} our Genesis block was born.".format(date.today()), proof=100) 

# Create a new block listing key/value pairs of block information in a JSON object. Reset the list of pending transactions & append the newest block to the chain.

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block

#Todo: Search the blockchain for the most recent block.

    @property
    def last_block(self):
 
        return self.chain[-1]

#Todo: Add a transaction with relevant info to the 'blockpool' - list of pending tx's. 

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'From (sender)': sender,
            'To (recipient)': recipient,
            'Value (amount)': amount
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

#Todo: receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

#Example 
blockchain = Blockchain()
tran1 = blockchain.new_transaction("Satoshii", "Mikee", '5 BTC')
tran2 = blockchain.new_transaction("Mikee", "Satoshii", '1 BTC')
tran3 = blockchain.new_transaction("Satoshii", "Hal Finney", '5 BTC')
blockchain.new_block(200)

tran4 = blockchain.new_transaction("Mikee", "Alice", '1 BTC')
tran5 = blockchain.new_transaction("Alice", "Bob", '0.5 BTC')
tran6 = blockchain.new_transaction("Bob", "Mikee", '0.5 BTC')
blockchain.new_block(300)

print("BlockChain: ",blockchain.chain)

for i in range(len(blockchain.chain)):
    print("block: "+ str(i), blockchain.chain[i])

