# Print the greatest of the 3 numbers taken as input, print equal if all three numbers are the same
n1=int(input("enter the 1st number"))
n2=int(input("enter the 2nd number"))
n3=int(input("enter the 3rd number"))

if(n1==n2 and n2==n3):
    print("All three numbers are the same")
elif (n1>n2 and n1>n3):
    print(n1,"is greatest")

elif (n2>n3):
    print(n2,"is greatest")
else:
    print(n3,"is greatest")

