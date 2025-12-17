def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b != 0:
        return a/b
    else:
        return"cannot divide by zero"

while True:
    print("\n---CALCULATOR---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice(1-5): ")

    if choice == "5":
        print("calculator closed.")
        break

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if choice == "1":
        print("Result =", add(a,b))
    elif choice == "2":
        print("Result =", sub(a,b))
    elif choice == "3":
        print("Result =", mul(a,b))
    elif choice == "4":
        print("Result =", div(a,b))
    else:
        print("Invalid choice.")




