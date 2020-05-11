# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:53:39 2020

Gives the meaning of the word.
data is loaded from data.json file
@author: SowjanyaG
"""
import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) >0:
        yn =input("Did you mean '{}' instead? Enter Y if Yes, or N if No.".format(get_close_matches(w, data.keys())[0]))
        if yn =='Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn =='N':
            return "The Word doesn't exist. Please double check it."
        else:
            return "We didn't understand your Query"
    else:
        return "The Word doesn't exist. Please double check it."

word = input("Enter a word:")
result = translate(word)

if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)