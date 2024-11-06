class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.__account_holder = account_holder  # Private variable
        self.__balance = initial_balance        # Private variable

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited: ",amount)
            print("New Balance: ",self.__balance)
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print("Withdrew: ",amount)
                print("New Balance: ",self.__balance)
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    # Private method to display the account holder's information
    def __display_account_info(self):
           print("Account Holder: ", self.__account_holder) 
           print("Balance: ",self.__balance)

        #return "Balance: ",self.__balance

    # Public method to access the private method
    def show_account_info(self):
        print(self.__display_account_info())

# Create a BankAccount object
account = BankAccount("Ranjana", 1000)

# Perform some operations
account.deposit(500)
account.withdraw(300)
account.show_account_info()

