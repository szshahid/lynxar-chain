from blockchain import LynxarChain

class LynxarToken:
    def __init__(self, blockchain: LynxarChain):
        self.blockchain = blockchain
        self.name = "Lynxar Chain"
        self.symbol = "LYNX"
        self.decimals = 18
        self.total_supply = 10_000_000_000 * (10 ** self.decimals)  # 10 Billion

    def transfer(self, sender: str, recipient: str, amount: int) -> bool:
        if amount <= 0:
            return False
            
        self.blockchain.add_transaction(sender, recipient, amount)
        return True

    def balance_of(self, address: str) -> float:
        return self.blockchain.get_balance(address)
