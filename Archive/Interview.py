# Given 2 integer arrays, determine of the 2nd array is a rotated version of the 1st array

array_01 = [1,2,3,4,5]
array_02 = [5,4,3,2,1]

print 'EXERCISE #1:  ',
if array_01[::-1] == array_02:
    print 'Is inverse'
else:
    print 'Is not inverse'

# Find the most frequent integer in an array
with open('random_numbers.txt') as f:
    nums = [num.strip('\n') for num in f]

num_counter = {}
for i in nums:
    if i in num_counter:
         num_counter[i] +=1
    else:
        num_counter[i] = 1
print 'EXERCISE #2:  ', num_counter

# Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)
print 'EXCERCISE #3:  '
d = {}
for num in nums:
    if num in d:
        d[num] +=1
    else:
        d[num] = 1
for int1 in d:
    for int2 in d:
        if int(int1) + int(int2) == 10:
            print int1,'+',int2,'= 10'
        else:
            continue

# Write fibbonaci recursively
print 'EXCERCISE #4:  '
x = int(raw_input('What is the max range for the sequence?  '))

def Fibo(n):
    if n == 0: return 0
    elif n ==1: return 1
    else: return Fibo(n-1) + Fibo(n-2)

for i in range(1,x+1):
    print 'Position',i,':  ',(Fibo(i))


# Check if a String is composed of all unique characters
s = str(raw_input('Enter word here:  '))
d = {}
duplicates = []

for i in s:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1
for i in d:
    if d[i] > 1:
        duplicates.append(i)
    else:
        continue

if not duplicates:
    print 'All characters are unique'
else:
    print 'Contains duplicate characters, see below:  '
    print duplicates

# Reverse a String iteratively and recursively

s = str(raw_input('Enter word here:  '))
print s[::-1]
