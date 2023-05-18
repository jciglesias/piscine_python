import random

def check_option(op) -> bool:
    if op == None:
        return False
    elif type(op) is str:
        if op == "shuffle" or op == "unique" or op == "ordered":
            return False
    return True

def generator(text: str, sep: str = " ", option: str = None):
    """Splits the text according to sep value and yield the substrings. option precise if a action is performed to the substrings before it is yielded."""
    if (type(text) is not str) or check_option(option):
        print("ERROR")
        return 
    s = text.split(sep)
    if option:
        if option == "ordered":
            s.sort()
        elif option == "unique":
            tmp = []
            [tmp.append(x) for x in s if x not in tmp]
            s = tmp
        elif option == "shuffle":
            for i in range(len(s)):
                j = random.randint(0, len(s) - 1)
                s[i], s[j] = s[j], s[i]
    for i in s:
        yield i
    
if __name__=="__main__":
    text =  "Le Lorem Ipsum est simplement du faux texte."
    for i in generator(text):
        print(i)