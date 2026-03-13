def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except TypeError:
        print('Inputs must be numbers')
    else:
        print(f'Result: {result}')
    finally:
        print('Operation complete.')
        
divide(10, 2)
divide(10, 0)