import sys

MORSE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', ' ': '/'}

def translate_code(line:str = None):
    if line != None:
        l = "";
        for n in line:
            code = MORSE_DICT.get(n.capitalize());
            if code == None:
                raise ValueError(f"ERROR: {n} is not convertible to morse code");
            l += code;
        print(l);

if __name__=="__main__":
    argc = len(sys.argv);
    if argc > 1:
        st = sys.argv[1];
        if argc > 2:
            for i in sys.argv:
                if i != 'sos.py' and i != sys.argv[1]:
                    st += (' ' + i);
        try:
            translate_code(st);
        except ValueError as ve:
            print(ve);
    else:
        print("Usage: python3 sos.py <arg> ...");