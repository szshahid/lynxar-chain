import hashlib
import json
from time import time
from typing import List, Dict

class Block:
    def __init__(self, index: int, transactions: List[Dict], timestamp: float, previous_hash: str):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty: int):
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

class LynxarChain:
    def __init__(self):
        self.chain: List[Block] = [self.create_genesis_block()]
        self.pending_transactions: List[Dict] = []
        self.difficulty = 4
        self.mining_reward = 100
        self.wallet_address = "0x42Ef69ad0BD86f0C4a4144d4B295174E737C031c"

    def create_genesis_block(self) -> Block:
        return Block(0, [], time(), "0")

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def add_transaction(self, sender: str, recipient: str, amount: float) -> None:
        self.pending_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

    def mine_pending_transactions(self) -> None:
        block = Block(
            len(self.chain),
            self.pending_transactions,
            time(),
            self.get_latest_block().hash
        )
        block.mine_block(self.difficulty)
        self.chain.append(block)
        
        # মাইনারকে রিওয়ার্ড দিন
        self.pending_transactions = [{
            'sender': "network",
            'recipient': self.wallet_address,
            'amount': self.mining_reward
        }]
        print("Block mined successfully!")

    def get_balance(self, address: str) -> float:
        balance = 0.0
        for block in self.chain:
            for trans in block.transactions:
                if trans['sender'] == address:
                    balance -= trans['amount']
                if trans['recipient'] == address:
                    balance += trans['amount']
        return balance

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True
