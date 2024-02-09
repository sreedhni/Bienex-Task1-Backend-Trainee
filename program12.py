# 12   Print first 10 fibonacci numbers using 'for' and 'while' loops
# Using for loop
fibonacci_sequence = [0, 1]
for i in range(2, 10):
    fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

print("First 10 Fibonacci numbers using for loop:")
for num in fibonacci_sequence:
    print(num, end=" ")
    
print(" ")


# Using while loop
fibonacci_sequence = [0, 1]
count = 2
while count < 10:
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)
    count += 1

print("Fibonacci numbers using 'while' loop:")
for num in fibonacci_sequence:
    print(num, end=" ")
