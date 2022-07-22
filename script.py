#!/bin/python3

#variables and methods
quote = "I like big butts and I cannot lie"
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case

print(len(quote)) #length of quote

name = "Ali" #string
age = 19 #int int(30)
gpa = 5.17 #float float(5.17)

print(int(age))
print(int(30.1)) #drop after the .

print("My name is " + name + " and I am " + str(age) + " years old.")

age +=1
print(age)

birthday = 1
age += birthday
print(age)


print('\n')
#Functions
print("Here is an example of a function:" )

def who_am_i(): #this is a function
	name = "Alis"
	age = 30
	print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

#adding parameters
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)


#multiple parameters
def add(x,y):
	print(x + y)

add(7,7)



def multiply(x,y):
	return x * y

print(multiply(50,3))

def nl():
	print('\n')

nl()

#Relational and Boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7>=7

test_and = 7 > 5 and (5 < 7) #TRUE
test_and2 = (7 > 5) and (5 < 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_not = not True #false




nl()
#conditioanl statements
def drink(money):
	if money >=2:
		return "youve got yourself a drink"
	else:
		return "no drink for you"
print(drink(1))
print(drink(2))
print(drink(3))


def alcohol(age,money):
	if (age>=21) and (money >= 5):
		return "drink time"
	elif (age>=21) and (money <5):
		return "more money"
	elif (age < 21) and (money >=5):
		return "nice try kid"
	else:
		return "too young and too poor"

print(alcohol(21,5))
print(alcohol(20,100))
print(alcohol(1,2))
print(alcohol(21,2))

nl()

#lists - have brackets []
movies = ["Top Gun", "Love Simon", "Stranger Things", "Perks of Being a Wallflower"]

print(movies[0]) #first item in list
print(movies[1:4]) #return items from 1 till 4
print(movies[1:]) #return items from 1
print(movies[:2]) #return items upto index 2
print(movies[-1]) #last item in list

print(len(movies))
movies.append("JAWS")
print(movies)

movies.pop() #delete last item of list
print(movies)
movies.pop(0) #remove first item

nl()
#TUPLES - like lists but unmutable (un changeable)
grades = ("a", "b", "c", "d", "f")
print(grades[1])




nl()
#looping

#Foor loops - start to finish of an iterate
vegetables = ["carrot", "beans", "apples"]
for x in vegetables:
	print(x)



#While Loops
i = 1
while i < 10:
	print(i)
	i +=1
