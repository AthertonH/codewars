# Welcome.
#
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#
# If anything in the text isn't a letter, ignore it and don't return it.
#
# "a" = 1, "b" = 2, etc.
#
# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

# def alphabet_position(text):
#     Position = {"1":"a".lower(), "2":"b".lower(), "3":"c".lower(), "4":"d".lower(), "5":"e".lower(), "6":"f".lower(),
#                 "7":"g".lower(), "8":"h".lower(), "9":"i".lower(), "10":"j".lower(), "11":"k".lower(), "12":"l".lower(),
#                 "13":"m".lower(), "14":"n".lower(), "15":"o".lower(), "16":"p".lower(), "17":"q".lower(),
#                 "18":"r".lower(), "19":"s".lower(), "20":"t".lower(), "21":"u".lower(), "22":"v".lower(),
#                 "23":"w".lower(), "24":"y".lower(), "25":"x".lower(), "26":"z".lower()
#                 }

def alphabet_position(text):
    new = ""
    for char in text.lower():
        if ord(char)-96 < 0:
            new += ""
        else:
            new += str(ord(char)-96) + " "
    return new.strip()