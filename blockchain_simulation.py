from flask import Flask, jsonify, request
import hashlib
import json
import time

app = Flask(__name__)

class Block:
    def __init__(self, index, previous_hash, transactions, proof):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "proof": self.proof
        }
        block_string = json.dumps(block_data, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_block(proof=1, previous_hash='0')
    
    def create_block(self, proof, previous_hash):
        block = Block(index=len(self.chain),
                      previous_hash=previous_hash,
                      transactions=self.pending_transactions.copy(),
                      proof=proof)
        self.pending_transactions = []
        self.chain.append(block)
        return block
    
    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)
    
    def get_last_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, last_proof):
        proof = 0
        while not self.valid_proof(last_proof, proof):
            proof += 1
        return proof
    
    def valid_proof(self, last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
            if not self.valid_proof(previous.proof, current.proof):
                return False
        return True
    
    def mine_block(self):
        if not self.pending_transactions:
            return None
        last_block = self.get_last_block()
        last_proof = last_block.proof
        proof = self.proof_of_work(last_proof)
        new_block = self.create_block(proof, last_block.hash)
        return new_block

# API endpoint to get the blockchain data
@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    return jsonify([{
        "index": block.index,
        "transactions": block.transactions,
        "previous_hash": block.previous_hash,
        "proof": block.proof,
        "hash": block.hash
    } for block in blockchain.chain])

# Initialize blockchain
blockchain = Blockchain()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
