# 1     Write python programs , which accept two inputs and perform the following arithmetic operations
# 	i)    Addition (+)
#         ii)   Subtraction (-)
#         iii)  Multiplication (*)
#         iv)   Division (/)
#         v)    Modulus (%)
#         vi)   Exponentiation (**)
#         vii)  Floor Division (//)  




n1=int(input("enter a number= "))
n2=int(input("enter a number= "))

# 1)Addition
add=n1+n2
print(add)

# substraction
print(n1 - n2 if n1 > n2 else n2 - n1)

#iii) Multiplication
print(n1*n2)

#iv)Division (/)
print(n1/n2)

#v)Modulus (%)
print(n1%n2)

#vi)Exponentiation (**)
print(n1**n2)

#vii)Floor Division (//)  
print(n1//n2)




