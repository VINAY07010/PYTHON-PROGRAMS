# ADDING TWO NUMBERS

num1 = float(input("Enter the First Number for Addition: "))
num2 = float(input("Enter the Second Number for Addition: "))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")

# DIVIDING TWO NUMBERS

num3 = float(input("Enter Dividend for Division: "))
num4 = float(input("Enter Divisor for Division: "))
if num4 == 0:
    print("Error: Division by zero is not allowed")
else:
    div_result = num3 / num4
    print(f"Division: {num3} / {num4} = {div_result}")