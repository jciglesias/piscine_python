kata = (19, 42, 21)
# kata = (19, 42, 21, 3, 0, 55)
# kata = ()

if __name__=='__main__':
    size = len(kata)
    print(f"The {size} numbers are:", end = " " if size else '\n')
    for i in range(size):
        print(kata[i], end = "\n" if i == (size - 1) else ", ")