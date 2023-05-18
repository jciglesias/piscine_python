kata = "The right format"
# kata = "123456789012345678901234567890123456789012"
# kata = ""

if __name__=="__main__":
    for i in range(42 - len(kata)):
        print('-', end = "")
    print(kata, end = "")