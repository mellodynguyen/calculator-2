"""CLI application for a prefix-notation calculator."""

from arithmetic import add, subtract, multiply, divide, square, cube, power, mod

while True: #can change this true to something else if we want later
    user_input = input("What is your equation > ")
    tokens = user_input.split(" ")
    
    if "q" in tokens or "quit" in tokens:
        print("You will quit.")
        break  

    elif len(tokens) < 2:
        print("Not enough inputs.")
        continue

    operator = tokens[0]
    num1 = tokens[1]
    
    #method from calculator1 lab
        
    # adjusting the intake for the arguments based on the user's choice of operator
    # cubes+ = c[0] u[1] etc 
    # + = +[0]
    # ** = *[0]*[1]

    if operator == "+":
        num2 = tokens[2]
        result = add(float(num1), float(num2))

    elif operator == "-":
        num2 = tokens[2]
        result = subtract(float(num1), float(num2))
    
    elif operator == "*":
        num2 = tokens[2]
        result = multiply(float(num1), float(num2))
    
    elif operator == "/":
        num2 = tokens[2]
        result = divide(float(num1), float(num2))

    # if len(tokens[0]) >= 2:
    elif operator == "**":
        result = square(float(num1)) 

    elif operator == "cube": 
        # print(operator)
        # cubes is num1 ** 3 
        result = cube(float(num1))

    print(result)