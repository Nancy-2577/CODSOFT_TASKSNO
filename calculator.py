import math


print("*" * 45)
print("Welcome to the Calculator!")
print("*" * 45)

print("-" * 45)
print("INSTRUCTIONS:")

print("\nSelect operation:")
print("1. Addition (+)")    
print("2. Subtraction (-)")
print("3. Multiplication (*)")  
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Exponentiation (**)")
print("7. sqrt (√)")
print("8. Trigonometry (sin, cos, tan)")

print("-" * 45)

num1 = int(input("Enter the first number: "))
operation = int(input("choose the operation (1-8): "))
num2 = int(input("Enter the second number: "))

if operation == 1:
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")


elif operation == 2:
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")

elif operation == 3:
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")



elif operation == 4:  
    
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")

elif operation == 5:
    if num2 == 0:
        print("Error: Modulus by zero is not allowed.")
    else:
        result = num1 % num2
        print(f"The result of {num1} % {num2} is: {result}")

elif operation == 6:
    result = num1 ** num2
    print(f"The result of {num1} ** {num2} is: {result}")


elif operation == 7:
    if num1 < 0:
        print("Error: Square root of a negative number is not allowed.")
    else:
        result = math.sqrt(num1)
        print(f"The square root of {num1} is: {result}")


elif operation == 8:
    trig_function = input("Enter the trigonometric function (sin, cos, tan): ").lower()
    angle = float(input("Enter the angle in degrees: "))
    radians = math.radians(angle)

    if trig_function == "sin":
        result = math.sin(radians)
        print(f"The sine of {angle} degrees is: {result}")

    elif trig_function == "cos":
        result = math.cos(radians)
        print(f"The cosine of {angle} degrees is: {result}")

    elif trig_function == "tan":
        result = math.tan(radians)
        print(f"The tangent of {angle} degrees is: {result}")

    else:
        print("Error: Invalid trigonometric function. Please choose sin, cos, or tan.")