#!/bin/python3
import sys #system functions and paramenters
import os
from datetime import datetime as dt #import with alias
print(dt.now())

print(sys.version)

#sys.exit - exists the script clearnly

my_name = "Alistair"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence"
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)


quote = "he said, \"give me all your money\""
print(quote)


too_much_space = "               hello                 "
print(too_much_space.strip())

print("a" in "Apple")
letter = "A"
word = "APPLE"
print(letter.lower() in word.lower()) #improved

movie = "The hangover"
print("my fav movie is {}".format(movie))


#Dictonaries - key/value pairs {}

drinks = {"white russian": 7, "old fashion": 10, "lemon drop":100} #drink is key, price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Teddy", "bob"], "HR": ["jimmy", "mort"]}
print(employees)

employees["legal"] = ["Mr. Frond"] #add new key value pair
print(employees)

employees.update({"Sales": ["BOB", "tina"]})
print(employees)

drinks["white russian"] = 99
print(drinks)

print(drinks.get("white russian"))
