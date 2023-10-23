def calculate(*args, operator):
 
    if operator not in ['+', '-', '*', '/']:
        raise ValueError("Invalid operator. Operator must be '+', '-', '*', or '/'")

    if operator == '+':
        return sum(args)
    elif operator == '-':
        if len(args) > 1:
            return args[0] - sum(args[1:])
        else:
            return -args[0]
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
        return result
    elif operator == '/':
        if len(args) > 1:
            result = args[0]
            for num in args[1:]:
                if num == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                result /= num
            return result
        else:
            raise ValueError("At least two arguments are required for division")
        
#how to use the calculator 
print(calculate(5, 3, operator='+')) 
print(calculate(5, 3, operator='-')) 
print(calculate(5, 3, operator='*')) 
print(calculate(5, 3, operator='/'))
print(calculate(5, operator='-'))