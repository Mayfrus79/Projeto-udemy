while True: 
    number_1 = input("Enter the first number: ")
    operator = input("Enter the operator (+, -, *, /): ")
    number_2 = input("Enter the second number: ")

    try:
        num_1_float = (float(number_1))
        num_2_float = (float(number_2))
        numbers_valid = True    
    except ValueError:
        numbers_valid = None
    
    if numbers_valid is None:
        print("One or both numbers of the entered numbers are invalid.")
        continue

    allowed_operators = "+-*/"

    if operator not in allowed_operators:
        print('Invalid Operator')
        continue

    if operator == "+":
        result = num_1_float + num_2_float 
    
    elif operator == "-":
        result = num_1_float - num_2_float
    
    elif operator == "*":
        result = num_1_float * num_2_float
    
    elif operator == "/":
        if num_1_float and num_2_float == 0:
            print("ERROR: Division by 0 is not allowed.")
        result = num_1_float / num_2_float
    
    print(f"The result of {number_1} {operator} {number_2} is: {result}")
    
    exit_choice = input("Do you want to exit? [Y]es or [N]o:").lower().startswith('y')
    if exit_choice:
        print('Exiting the calculator. GoodBye!')
        continue
            


