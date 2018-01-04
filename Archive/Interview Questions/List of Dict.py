'''

Lists and Dictionaries

'''

# Take user input to generate list 'x' size
size = input('How many elements are there?  ')
num_multiply = input('What do I multiply by?  ')

l = []
for i in range((size - 1)):
    l.append(i*num_multiply)
print l[1:]

index = input('Find at index:  ')
[i for i, x in enumerate(l) if x ==  index]:
    print x