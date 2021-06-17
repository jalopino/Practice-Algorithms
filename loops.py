'''
def difference (a, b):
    z = a - b
    return z
numberOfEntries = int(input())
entryPass = 0
while True:
    if (entryPass == numberOfEntries):
        break
    secondEntrypass = 0
    while True:
        Entry = int(input())
        secondEntrypass = secondEntrypass + 1
        if(secondEntrypass == 2):
            b = Entry
            print (difference(a, b))
            break
        a = Entry
    entryPass = entryPass + 1


def negate(a):
    z = int(a) * -1
    return z

def add(a, b):
    z = int(a) + int(b)
    return z

def maximum(a, b, c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    elif (c > a and c > b):
        return c
    else:
        return a


while True:
    inputString = input()
    if(inputString == 'stop'):
        break
    a = 0
    b = 0
    c = 0
    if (inputString == 'negate'):
        a = input()
        print(negate(a))
    elif (inputString == 'add'):
        a = input()
        b = input()
        print(add(a, b))
    elif (inputString == 'maximum'):
        a = input()
        b = input()
        c = input()
        print(maximum(a, b, c))

'''
