# 4    Python program to check the number taken as an input is even or odd,print invalide input if user enters 
# anything other than integers

def even_odd():
    try:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(number," is even.")
        else:
            print(number," is odd.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

even_odd()

