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

    #method from calculator1 lab
    operator = tokens[0]
    num1 = tokens[1]
    
    # if the length if user input is greater than 3, sub num2 for 0
    # ex cubes+ and pow (power) only takes one number 
    if len(tokens) < 3:
        num2 = "0"
    
    else:
        num2 = tokens[2]
    
    if len(tokens) > 3:
        num3 = tokens[3]
    

    if operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))

    elif operator == "*":
        result = multiply(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), float(num2))


    elif operator == "**":
        result = square(float(num1)) 

    elif operator == "cubes+": 
        # cubes is num1 ** 3 
        result = cube(float(num1)) 
    elif operator == pow:
        reslt = power(float(num1, num2))

    print(result)