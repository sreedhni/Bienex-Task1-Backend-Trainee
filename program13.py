	    #     *
        #    * *
        #   * * *
        #  * * * *

def print_pattern(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "* " * i
        print(spaces + stars)

print_pattern(4)  
print()

# (b)	o
# 		1 2
# 		3 4 5
# 		6 7 8 9

def print_pattern(rows):
    number = 0
    for i in range(1, rows + 1):
        for j in range(i):
            print(number, end=" ")
            number += 1
        print()

print_pattern(4) 

print()
#    	o
# 		1 1
# 		2 2 2
# 		3 3 3 3


def print_pattern(rows):
    for i in range(0, rows):
        for j in range(i+1):
            print(i, end=" ")
        print()
print_pattern(4)
print()


# (d)	*
# 		* *
# 		* * *
# 		* * * *

def print_pattern(rows):
    for i in range(1, rows + 1):
        stars = "* " * i
        print(stars)
print_pattern(4) 
