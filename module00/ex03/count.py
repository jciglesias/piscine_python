def text_analyzer(arg: str = None):
    '''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''
    if arg == None:
        arg = input("What is the text to analyze?\n");
    if isinstance(arg, str): #type(arg) is str:
        count = [0, 0, 0, 0, 0];
        for element in arg:
            if element.isupper():
                count[0] += 1;
            elif element.islower():
                count[1] += 1;
            elif element == ' ':
                count[2] += 1;
            elif element in ".,!?():;'-[]": #https://punctuationmarks.org/
                count[3] += 1;
            count[4] += 1;
        print(f"The text contains {count[4]} character(s):\n- {count[0]} upper letter(s)\n- {count[1]} lower letter(s)\n- {count[3]} punctuation mark(s)\n- {count[2]} space(s)")
    else:
        print("Error: Argunment is not a string");

import sys

if __name__=="__main__":
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1]);
    elif len(sys.argv) == 1:
        text_analyzer();
    else:
        print("Error: more than one argument provided")