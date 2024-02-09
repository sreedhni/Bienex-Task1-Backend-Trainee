
#  Python program to print the multiplication table of any number (number should be taken as input and user 
#                                                         decides the end limit of the table)

num=int(input("enter the num"))
limit=int(input("enter the limit"))
for i in range(1,limit+1):
    res=i*num
    print(f"{i} * {num} = {res}")