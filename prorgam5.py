# 5    Python program to check the score from a student ,print grades as A+ if score >= 90,A if 80 or above, 
# B+ if 70 or above and so on... print failed if the score is below 50, if score > 100 print invalid
score = int(input("Enter the student's score: "))
if score > 100:
    print("Invalid")
elif score >= 90:
    print("A+")
elif score >= 80:
    print("A")
elif score >= 70:
    print("B+")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C+")
elif(score<50):
    print("Failed")
