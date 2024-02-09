#  Find the factorial of a number taken as input using while loop
num=int(input("enter a number"))
fact=1
while(num>=1):
        fact=fact*num
        num-=1
print(fact) 