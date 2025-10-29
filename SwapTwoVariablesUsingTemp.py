# INPUT TWO VARIABLES

a = input("Enter the value of first variable (a): ")
b = input("Enter the value of second variable (b): ")

# DISPLAY THE ORIGINAL VALUES

print(f"Original values: a = {a}, b = {b}")

# SWAP THE VALUES USING TEMPORARY VARIABLE

temp = a
a = b
b = temp

# DISPLAY THE SWAPPED VALUES

print(f"Swapped values: a = {a}, b = {b}")