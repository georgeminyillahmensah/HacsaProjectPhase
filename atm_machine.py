# Define the ATM machine class
class ATMMachine:
    def __init__(self):
        # Initialize the ATM with a default balance of 0
        self.balance = 0

    def display_menu(self):
        """
        Display the main menu with options for the user.
        """
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")  # Option to check the current balance
        print("2. Deposit Money")  # Option to deposit money
        print("3. Withdraw Money")  # Option to withdraw money
        print("4. Exit")  # Option to exit the program
        print("==============================")

    def check_balance(self):
        """
        Show the user their current account balance.
        """
        print(f"\nYour current balance is: ${self.balance:.2f}")  # Display balance with 2 decimal places

    def deposit_money(self):
        """
        Allow the user to deposit money into their account.
        """
        try:
            # Prompt the user to enter the deposit amount
            amount = float(input("\nEnter the amount to deposit: $"))
            if amount > 0:  # Ensure the deposit amount is positive
                self.balance += amount  # Add the deposit amount to the balance
                print(f"${amount:.2f} deposited successfully.")  # Confirm the deposit
                self.check_balance()  # Show the updated balance
            else:
                print("Amount must be greater than zero.")  # Handle invalid input
        except ValueError:
            # Handle non-numeric input
            print("Invalid input! Please enter a numeric value.")

    def withdraw_money(self):
        """
        Allow the user to withdraw money from their account.
        """
        try:
            # Prompt the user to enter the withdrawal amount
            amount = float(input("\nEnter the amount to withdraw: $"))
            if amount > 0:  # Ensure the withdrawal amount is positive
                if amount <= self.balance:  # Check if there is enough balance
                    self.balance -= amount  # Deduct the withdrawal amount from the balance
                    print(f"${amount:.2f} withdrawn successfully.")  # Confirm the withdrawal
                    self.check_balance()  # Show the updated balance
                else:
                    print("Insufficient balance!")  # Handle insufficient funds
            else:
                print("Amount must be greater than zero.")  # Handle invalid input
        except ValueError:
            # Handle non-numeric input
            print("Invalid input! Please enter a numeric value.")

    def run(self):
        """
        Main function to run the ATM machine, displaying the menu and handling user input.
        """
        while True:
            # Display the menu for the user
            self.display_menu()
            try:
                # Prompt the user to select an option
                choice = int(input("\nSelect an option (1-4): "))
                if choice == 1:
                    self.check_balance()  # Call the function to check balance
                elif choice == 2:
                    self.deposit_money()  # Call the function to deposit money
                elif choice == 3:
                    self.withdraw_money()  # Call the function to withdraw money
                elif choice == 4:
                    # Exit the program
                    print("\nThank you for using the ATM. Goodbye!")
                    break
                else:
                    # Handle invalid menu selection
                    print("Invalid choice! Please select a valid option.")
            except ValueError:
                # Handle non-numeric input
                print("Invalid input! Please enter a number between 1 and 4.")


# Run the ATM machine program
if __name__ == "__main__":
    # Create an instance of the ATMMachine class
    atm = ATMMachine()
    # Start the ATM machine
    atm.run()
