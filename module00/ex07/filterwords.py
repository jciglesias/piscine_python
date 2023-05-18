import sys
import string

if __name__=="__main__":
    argc = len(sys.argv)
    if argc == 3 and sys.argv[2].isdigit():
        arr: str = ""
        for n in sys.argv[1]:
            arr = arr + n.strip(string.punctuation)
        arr = arr.split()
        size = int(sys.argv[2])
        arr = [n for n in arr if len(n) > size]
        print(arr)
    else:
        print("ERROR")