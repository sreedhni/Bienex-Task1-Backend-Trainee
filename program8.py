# Find the factorial of a number taken as input using for loop

num=int(input("enter a number"))
fact=1
for i in range(1,num+1):
        fact=fact*i
print(f"factorial of {num} is {fact}") 