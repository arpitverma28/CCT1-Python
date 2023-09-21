#CALCULATOR


print("Select an Operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1": # PERFORM ADDITION
    num1 = input("Enter The First Number: ")
    num2 = input("Enter The Second Number: ")
    print("The Sum is" + str(int(num1) + int(num2)))
elif operation =="2": # PERFORM SUBTRACTION
    num1 = input("Enter The First Number: ")
    num2 = input("Enter The Second Number: ")
    print("The Difference is" + str(int(num1) - int(num2)))
elif operation =="3": # PERFORM MULTIPLICATION
    num1 = input("Enter The First Number: ")
    num2 = input("Enter The Second Number: ")
    print("The Product is" + str(int(num1) * int(num2)))
elif operation =="4": # PERFORM DIVISION
    num1 = input("Enter The First Number: ")
    num2 = input("Enter The Second Number: ")
    print("The Result is" + str(int(num1) / int(num2)))
else:
    print("invalid Entry")