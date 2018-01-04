
'''

a = [2, 4, 5, 6, 12, 44, 76, 90, 201]

def binarySearch(list, item):
    first = 0
    last = len(a) - 1
    found =  False

    while(first <= last):
        midpoint = (last + first)/2
        if(list[midpoint] == item):
            print 'found it at index %s' % midpoint
            found = True
            return midpoint
        elif(item < list[midpoint]):
            last = midpoint - 1
        else:
            first = midpoint + 1

binarySearch(a,5)

'''
'''
def fibo(n):
    if(n == 0): return 0
    elif(n == 1): return 1
    else:
        return fibo(n - 1) + fibo(n -2)

print fibo(10)
'''
'''
def isPalindrome(string):
    first = 0
    last = len(string) - 1
    for i in string:
        if string[first] != string[last]:
            return False
        else:
            first+=1
            last-=1
    return True

print isPalindrome('test')
'''
'''
def firstNonRepeat(string):
    current = 0
    next = current + 1
    for i in string:
        if not(string[current] == string[next]):
            return string[current]
        else:
            current+=1

print firstNonRepeat('jjjjjjjjjjjjduuu')
'''
'''
list = ['apples', 'oranges', 'apple', 'michael', 'oranges', 'oranges', 'michael',
        'apples', 'oranges', 'apple', 'michael', 'oranges', 'oranges', 'michael',
        'apples', 'oranges', 'apple', 'michael', 'oranges', 'oranges', 'michael','apples', 'oranges', 'apple', 'michael', 'oranges', 'oranges', 'michael',
        'apples', 'oranges', 'apple', 'michael', 'oranges', 'oranges', 'michael',
        'apples', 'oranges', 'apple', 'michael', 'oranges', 'oranges', 'michael']
def findOccurances(list):
    map = {}
    for i in list:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    print map

findOccurances(list)
'''
'''
string = 'About Fire Calls for Service'
if string.startswith('About '):
    string = string[6:]
    string = string.replace(' ', '-')
    print string

'''
