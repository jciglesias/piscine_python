import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc > 1:
        if argc == 2:
            try:
                n = int(sys.argv[1])
                if n == 0:
                    print("I'm Zero.")
                elif n % 2:
                    print("I'm Odd.")
                else:
                    print("I'm Even.")
            except ValueError as ve:
                print(f"Error: you entered {sys.argv[1]} wich is not a number")
        else:
            print("Error: more than one argument are provide")
    else:
        print("Usage: python3 whois.py <arg>")