# 2 Python Program to replicate bank transaction: min balance 500, ask user to the amount to withdraw,print the balance amount after
#  withdrawal, if user enters an amount greater than balance: print:: insufficient balance. if balance is below 500 print an alert 
# message : your account balance is "available_balance", Please  keep your account balance above Rs.500 to avoid unwanted charges.


def bank_transaction(balance):
    if balance > 500:
        withdrawal_amount = int(input("Enter the withdrawlamount"))
        if withdrawal_amount > balance:
            print("Insufficient balance.")
        else:
            balance -= withdrawal_amount
            print(f"Balance amount after withdrawal: Rs. {balance}")
            if balance < 500:
                print(f"Your account balance is Rs. {balance}. Please keep your account balance above Rs. 500 to avoid unwanted charges.")
    else:
        print(f"Your account balance is Rs. {balance}. Please keep your account balance above Rs. 500 to avoid unwanted charges.")


bank_transaction(2000)
