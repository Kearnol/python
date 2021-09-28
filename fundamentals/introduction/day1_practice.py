heroes = ["Iron Man", "Hulk", "Wonder Woman", "Thor"]
villians = ["Thanos", "Joker", "Ultron", ["Marvel", "DC"]]
empty = []

# add heroes to villians
villians.extend(heroes)

print(villians)

#finding "Marvel" within villians list
print(villians[3][0])

# add values to list "empty" (same as .push() in JS)
heroes.append("Spider-man")
print(heroes)

# replace ("mutate") an index within a list: 
heroes[1] = "Old Man Captain America"
print(heroes)

#get the index of spider-man
print(heroes.index("Spider-man"))

#insert "New-Guy" to the heroes list before index 4
heroes.insert(4, "New-Guy")
print(heroes)

#pop index 4 from heroes. FYI this returns the value which can be stored as s variable (such as "what")
what = heroes.pop(4)
print(what)

#dictionary values are accessed via their key. 
ironman = {
    "name": "Tony Stark",
    "birthday": "5/29/1970",
    "powers": {
        "power1": "rich",
        "power2": "genius",
    },
    "gear": "ironman suit"
}

# access a dictionary within a dictionary
print(ironman["powers"]["power1"])

#you can loop through strings
for i in "Loop through this string":
    print(i)

#tuple experiments
# dog = ("pug", 135, "small bark")
# dog = dog + ("domestic")
# print(dog)

#loop through a dictionary, print the key and value
for i in ironman:
    print(i, ironman[i])

#loop through a dictionary within a dictionary, print the key and the value of the embedded dictionary
for i in ironman["powers"]:
    print(i, ironman["powers"][i])

#while loops
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1

print("Happy New Year!")

#functions 
#define with "def"
def add(a,b):
        x = a+b
        return x # must return the function

add_val = add(2,5) #returns to where the function is called
print(add_val)

#set up default values
def add2(a=1,b=2):
    x = a+b
    return x

add_val = add2(2) # this makes a=2 (it was passed), and b defaults back to it's defualt value of 2.
print(add_val)# this makes the solution 4

def say_hi(list):
    for i in list:
        print(f"Hi {i}")

say_hi(heroes)

def multiply(num_list, num):
    print(num_list, num)
    for x in num_list:
        print(x)
        x *= num
        print(num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)

