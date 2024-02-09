#  Find the sum of all even numbers between the range given by user

lower_limit=int(input("enter a lower limit"))
upper_limit=int(input("enter a upper limit"))
# for i in range(lower_limit,upper_limit+1):
#     if i%2==0:
#         print(i,end=" ")
even=([i for i in range(lower_limit,upper_limit+1) if i%2==0])
print("even number list",even)
