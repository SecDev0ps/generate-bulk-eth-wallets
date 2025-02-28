from eth_account import Account
import json
import os

def generate_wallet():
    account = Account.create()
    return {
        "address": account.address,
        "privateKey": account.key.hex()
    }

def save_wallets_to_file(filename, num_wallets):
    wallets = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                wallets = json.load(file)
            except json.JSONDecodeError:
                pass  # Ignore if file is empty or invalid JSON
    
    new_wallets = [generate_wallet() for _ in range(num_wallets)]
    wallets.extend(new_wallets)
    
    with open(filename, "w") as file:
        json.dump(wallets, file, indent=4)
    
    print(f"{num_wallets} wallets generated and saved to {filename}")

if __name__ == "__main__":
    num_wallets = int(input("Enter the number of wallets to generate: "))
    if num_wallets <= 0:
        print("Please enter a valid number greater than 0.")
    else:
        save_wallets_to_file("wallets.json", num_wallets)
