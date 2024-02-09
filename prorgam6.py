# 6    Python program to print all even/odd numbers in the range given by user
lower=int(input("enter a lower limit"))
upper=int(input("enter a uper limit"))
even=[]
odd=[]
for i in range(lower,upper+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even",even)
print("odd",odd)