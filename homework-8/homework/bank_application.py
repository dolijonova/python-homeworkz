import json

class Account:
    def __init__(self, account_number,name,balance):
        self.account_number=account_number
        self.name=name
        self.balance=balance
    def to_dic(self):
        return {
            self.account_number,
            self.name,
            self.balance
        }
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited ${amount:.2f}.New Balance: ${self.balance:;.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdrawn(self,amount):
        if amount>0:
            if self.balance>=amount:
                self.balance-=amount
                print(f"WIthdrew ${amount:.2f}. New Balance: $ {self.balance:.2f}")
            else:
                print("Funds are not sufficient")
        else:
            print("withdrawn must be positive")

    
class Bank:
    def __init__(self):
        self.accounts={}

    def create_account(self,name,initial_deposit):
        if initial_deposit<0:
            print("Initial deposit must be non-negative")
            return
        account_number=len(self.accounts)+1
        new_account=Account(account_number,name,initial_deposit)
        self.accounts[account_number]=new_account
        print(f"Account created successfully. Acsount number: {account_number}")

    def view_account(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"Account Number: {account.account_number}")
            print(f"Name: {account.name}")
            print(f"Balance: ${account.balance:.2f}")
        else:
            print("Account not found!")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
        else:
            print("Account not found!")

    def withdrawn(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdrawn(amount)
        else:
            print("Account not found!")

    def save_to_file(self, filename="bank_data.json"):
        accounts_data = {acc_num: account.to_dict() for acc_num, account in self.accounts.items()}
        with open(filename, "w") as file:
            json.dump(accounts_data, file)
        print(f"Accounts saved to {filename}.")

    def load_from_file(self, filename="bank_data.json"):
        try:
            with open(filename, "r") as file:
                accounts_data = json.load(file)
                self.accounts = {
                    int(acc_num): Account(data["account_number"], data["name"], data["balance"])
                    for acc_num, data in accounts_data.items()
                }
            print(f"Accounts loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty bank.")


# Command-line interface
def main():
    bank = Bank()
    bank.load_from_file()  # Load existing accounts from file

    while True:
        print("\nBanking Application")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, initial_deposit)

        elif choice == "2":
            account_number = int(input("Enter account number: "))
            bank.view_account(account_number)

        elif choice == "3":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_number, amount)

        elif choice == "4":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(account_number, amount)

        elif choice == "5":
            bank.save_to_file()
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    

