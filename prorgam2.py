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
