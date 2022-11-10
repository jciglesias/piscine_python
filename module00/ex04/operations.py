import sys

if __name__=='__main__':
    argc = len(sys.argv);
    if argc == 3:
        try:
            a = int(sys.argv[1]);
            b = int(sys.argv[2]);
            print(f"Sum:        {a + b}");
            print(f"Difference: {a - b}");
            print(f"Product:    {a * b}");
            if b != 0:
                print(f"Quotient:   {a / b}");
                print("Remainder: ", a % b);
            else:
                print("Quotient:   ERROR (division by zero)");
                print("Remainder:  ", "ERROR (modulo by zero)");
        except ValueError as ve:
            print("Error: only integers");
    elif argc > 3:
        print("Error: too many arguments");
    else:
        print("Usage: python3 operations.py <number1> <number2>");
        print("Example: \n\tpython3 operations.py 10 3")