def add(x,y):
    print(x + y)

def sub(x,y):
    print(x - y)

def div(x,y):
    print(x / y)

def mult(x,y):
    print(x * y)

while True:
    x = float(input("insert num1: "))
    y = float(input("insert num2: "))
    op = input("insert an operator: ")

    if op == "+":
        add(x, y)
    elif op == "-":
        sub(x, y)
    elif op == "/":
        div(x, y)
    elif op == "*":
        mult(x, y)
    else:
        print("invalid!")