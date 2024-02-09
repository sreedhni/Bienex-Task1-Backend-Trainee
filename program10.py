#  Find the sum of all even numbers between the range given by user

lower_limit=int(input("enter a lower limit"))
upper_limit=int(input("enter a upper limit"))
sum=0
while(lower_limit<upper_limit+1):
    if(lower_limit%2==0):
        sum+=lower_limit
    lower_limit+=1
print("sum of the even number between the range is",sum)
