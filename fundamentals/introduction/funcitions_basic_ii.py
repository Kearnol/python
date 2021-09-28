# countdown
def countdown(start):
    list  = []
    for x in range(start, -1, -1):
        list.append(x)
    return list
print(countdown(5))

# print and return
def printAndReturn(printVar="0", returnVar="sloppy work"):
    print(printVar)
    return returnVar
print(printAndReturn(1, 2))
print(printAndReturn())

#first plus length
def fpl(list):
    sum = list[0] + len(list)
    return sum
print(fpl([1,2,3,4,5]))

#values greater than second
def valuesGreater(list):
    newList = []
    if len(list) < 2:
        return False
    else:
        for x in range(0, len(list)):
            if list[x] > list[1]:
                newList.append(list[x])
    print(f"newList length = {len(newList)}")
    return newList

print(valuesGreater([5,2,3,2,1,4]))
print(valuesGreater([3]))

#this length, that value
def this_length_that_value(size, value):
    newList =[]
    for x in range(0, size):
        newList.append(value)
    return newList

print(this_length_that_value(4,7))
print(this_length_that_value(6,2))
