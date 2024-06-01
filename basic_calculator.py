# functions that take simple arithmetic
def add(a, b):
    answer = a + b
    print(a, "+", b, "=", answer, "\n")

def sub(a, b):
    answer = a - b
    print(a, "-", b, "=", answer, "\n")

def mul(a, b):
    answer = a * b
    print(a, "*", b, "=", answer, "\n")

def div(a, b):
    answer = a / b
    print(a, "/", b, "=", answer, "\n")

# run function over again until false...
while True:
    # output of choice
    print("pick any basic mathematical sign for your problem set")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Quit")

# user choice
    choice = input("put in your choice: ")
#
    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        add(a, b)

    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sub(a, b)

    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        mul(a, b)

    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        div(a, b)

    elif choice == "e" or choice == "E":
        print("program ended")
        quit()
