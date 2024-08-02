import json
from difflib import get_close_matches
data  =  json.load(open("124 data.json"))
def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) >  0:
        print("Did you mean %s instead" %get_close_matches(word,data.keys())[0])
        decide  = input("press y for yes , or n for no:")
        if decide == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == "n":
            return ("I cannot find that word")
        else:
            return ("Yoy have entered wrong input , please just enter just y or n")
    else :
        print("I cannot find what word")
word = input("Enter the word you want to search : ")
output =  translate(word)
if type(output) == list:
    for line in output:
        print(line)
else:
    print(output)