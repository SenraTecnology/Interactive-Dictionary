import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
  word = word.lower()
  if word in data:
    return data[word]
  elif word.title() in data:
    return data[word.title()]
  elif word.upper() in data:
    return data[word.upper()]
  elif len(get_close_matches(word, data.keys())) > 0:
    yn = input("Did you mean %s instad? Yes or No" % get_close_matches(word, data.keys())[0])
    if yn == "Y" or yn == "y":
      return data[get_close_matches(word, data.keys())[0]]
    elif yn == "N" or yn == "n":
      return "Word not found, try again."
    else: 
      return "Input not available"
  else:
    return "Word not found, try again."

word = input("Type word: ")
output = (translate(word))

if type(output) == list:
   for item in output:
     print(item)
else: 
  print(output)
