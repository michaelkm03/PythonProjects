import random


def substring(string):
    list = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            list.append(string[i:j + 1])
    list.sort()
    return list[-1]

def generateArray(size):
    items = []
    for num in range(size):
        items.append(random.randint(1, 101))
    return items

def bubbleSort(items):
    for i in range(0,len(items)):
        if items[i] > items[i+1]:
            temp = items[i]
            items[i] = items[i+1]
            items[i+1] = temp
    return items

if __name__ == '__main__':
    substring('uvuyvu izzzwenoppokk')
    list = generateArray(100)
    bubbleSort(list)