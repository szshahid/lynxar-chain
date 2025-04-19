from blockchain import LynxarChain
from token import LynxarToken
import argparse

def main():
    # ব্লকচেইন এবং টোকেন ইনিশিয়ালাইজ করুন
    blockchain = LynxarChain()
    lynx_token = LynxarToken(blockchain)

    # কমান্ড লাইন আর্গুমেন্ট পার্স করুন
    parser = argparse.ArgumentParser(description='Lynxar Chain CLI')
    parser.add_argument('--port', type=int, default=5000, help='Network port')
    args = parser.parse_args()

    print(f"""
    ██╗     ██╗   ██╗███╗   ██╗██╗  ██╗ █████╗ ██████╗ 
    ██║     ╚██╗ ██╔╝████╗  ██║╚██╗██╔╝██╔══██╗██╔══██╗
    ██║      ╚████╔╝ ██╔██╗ ██║ ╚███╔╝ ███████║██████╔╝
    ██║       ╚██╔╝  ██║╚██╗██║ ██╔██╗ ██╔══██║██╔══██╗
    ███████╗   ██║   ██║ ╚████║██╔╝ ██╗██║  ██║██║  ██║
    ╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
    
    Welcome to Lynxar Chain (LYNX) CLI
    Initial Supply: 10,000,000,000 LYNX
    Your Wallet: {blockchain.wallet_address}
    """)

    while True:
        print("\nMenu:")
        print("1. Send LYNX Tokens")
        print("2. Mine Pending Transactions")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            recipient = input("Recipient Address: ")
            amount = float(input("Amount: "))
            lynx_token.transfer(blockchain.wallet_address, recipient, amount)
            print(f"Transfer initiated! Mining required to confirm.")
            
        elif choice == "2":
            print("Mining...")
            blockchain.mine_pending_transactions()
            print(f"Mining reward: {blockchain.mining_reward} LYNX")
            
        elif choice == "3":
            balance = lynx_token.balance_of(blockchain.wallet_address)
            print(f"Your Balance: {balance} LYNX")
            
        elif choice == "4":
            print("Exiting Lynxar Chain CLI")
            break
            
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
