import hashlib
import json

from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

class Blockchain(object):

    def __init__(self):
        self.blockchain = [];
        # self.name = 'Michaels Blockchain'
        self.blockchain_transactions = [];

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
            Create a new Block in the Blockchain

        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional, req in genesis) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self.blockchain) + 1,
            'timestamp': time(),
            'transactions': self.blockchain_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.blockchain[-1]),
        }

        # Reset the current list of transactions
        self.blockchain_transactions = []

        self.blockchain_transactions.append(block)
        return block

    @staticmethod
    def hash(block):
        """
            Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str> hash
        """

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.blockchain[-1]

    def new_transaction(self, sender, recipient, amount):
        '''

            Creates new transaction to be added to next mined Block

        :param sender: <int> User ID of sender
        :param recipient: <int> User ID of recipient
        :param amount: <int> Amount
        :return: last Block in Blockchain to reserve for this transaction
        '''
        self.blockchain_transactions.append(
            {
                'Sender': sender,
                'Recipient': recipient,
                'Amount': amount
            }
        )

        return self.last_block['index'] + 1

    def proof_of_work(self, last_proof):
        '''
            Proof of Work Algorithm
            - Find a value, such that hash(p0 * p1) contains 4 leading zeros
            - p0:  previous proof value
            - p1:  current proof value

        :param last_proof:
        :return:
        '''

        proof = 0
        while self.is_valid_proof(last_proof, proof) is False:
            proof+=1

        return proof

    @staticmethod
    def is_valid_proof(last_proof, proof):
        '''

            Validates the Proof: Does hash(last_proof * proof) contain 4 leading zeroes?

        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> is valid proof?
        '''

        guess = f'{last_proof}{proof}'.encode()
        guess_hashed = hashlib.sha256(guess).hexdigest()
        return guess_hashed[-4] == '0000'

# Instantiate our Node and create globally unique identifier
app = Flask(__name__)
node_identifier = str(uuid4()).replace('-','')

# Instatiate new Blockchain
montys_chain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof...
    last_block = montys_chain.last_block
    last_proof = last_block['proof']
    proof = montys_chain.proof_of_work(last_proof)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    montys_chain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # Forge the new Block by adding it to the chain
    previous_hash = montys_chain.hash(last_block)
    block = montys_chain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transaction/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amount']
    if not all(keys in values for keys in required):
        return 'Missing values', 400

    # Create a new Transaction
    index = montys_chain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/blockchain', methods=['GET'])
def full_blockchain():
    response = {
        'blockchain': montys_chain.blockchain,
        'size': len(montys_chain.blockchain),
    }

    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)