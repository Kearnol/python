num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initilize float(i.e. decimals)
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list?
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary?
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuple? 
print(type(fruit)) # print the datatype of "fruit"
print(pizza_toppings[1]) # print "Pepporoni" >> the index of pizza_toppings at [0]
pizza_toppings.append('Mushrooms') # add Mushrroms?
print(person['name']) #prints "John"
person['name'] = 'George' #change person's name to "George"
person['eye_color'] = 'blue' #change person's eye color to "blue"
print(fruit[2]) # print fruit at index 2 == strawberry? 

if num1 > 45: #conditional if
    print("It's greater") # essentially console.log in JS
else:   #conditional else
    print("It's lower") 

if len(string) < 5: #conditional if, function call, string
    print("It's a short word!")
elif len(string) > 15: # else if?
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # print 0 - 4
    print(x)
for x in range(2,5): # print range of 2 - 4
    print(x)
for x in range(2,10,3): # print range 2 - 9 in multiples of 3
    print(x)
x = 0
while(x < 5): #while loop that prints 0-4
    print(x)
    x += 1


pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, array of strings
pizza_toppings.pop() # remove last index of pizza_toppings array
print(pizza_toppings) 
pizza_toppings.pop(1)# remove index1 of pizza_toppings array
print(pizza_toppings)

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
print(person)
person.pop('eye_color') #key error - no key of 'eye_color'
print(person)

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, array of strings
for topping in pizza_toppings: # for loop with an if statement in it
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): #function decleration 
    for num in range(10): #for loop 0-9
        print('Hello') # console.log hello

print_hello_ten_times() #function call

def print_hello_x_times(x): #parameter
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #argument decleration

def print_hello_x_or_ten_times(x = 10): # declare a function, declare a variable in the parameter
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4) # pass the argument x = 4 into the parameter of this function


"""
Bonus section
"""

print(num3) #name error
num3 = 72 #define a variable, numbers
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, tuple?
fruit[0] = 'cranberry' # Tuple error
print(person['favorite_team']) #KeyError: 'favorite_team'
print(pizza_toppings[7])# IndexError: list index out of range
  print(boolean) # indent error
fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'
