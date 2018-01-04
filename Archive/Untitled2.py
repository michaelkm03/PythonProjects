##import urllib
##import re
##
##urls = ["http://google.com","http://nytimes.com","http://CNN.com"]
##
##i = 0
##regex = '<title>(.+?)</title>'
##pattern = re.compile(regex)
##while i < len (urls):
##        htmlfile = urllib.urlopen(urls[i])
##        htmltext = htmlfile.read()
##        titles = re.findall(pattern,htmltext)
##        print titles
##        i+=1
##
##def computepay(h,r):
##    return 42.37
##computepay(10,20)


##intTestValueOne = 1
##if not type (intTestValueOne) == type(1.0):
####        print "Variable is not type('float')"
##
##smallest = None
##print 'Before'
##for value in [3,41,'hello',12,943,74]:
##        if smallest is None:
##                smallest = value
##        elif value < smallest:
##                smallest = value
##        print smallest, value
##
##print 'After',smallest

##tot = 0 
##for i in [5, 4, 3, 2, 1] :
##    tot = tot + 1
##print tot
##
##largest = None
##smallest = None
##
##while True:
##    try:
##        num_as_string = raw_input("Enter a number: ")
##        num_value = int(num_as_string)
##
##        if largest is None or num_value > largest:
##            largest = num_value
##
##        if smallest is None or num_value < smallest:
##            smallest = num_value
##
##    except:
##        if num_as_string == "done":
##            break
##        else:
##            print "Invalid input"
##            continue
##
##print "Maximum is", largest
##print "Minimum is", smallest
##
##def birthday(bmonth,bday,byear):
##        user_birthday = bmonth + bday + byear
##        bmonth = str(raw_input('Enter the month you were born: '))
##        bday = str(raw_input('Enter the day you were born: '))
##        byear = str(raw_input('Enter the year you were born: '))
##
##        return birthday
##
##x = birthday
##
##print x


##
##fruit = 'banana'
##index = 0
##while index < len(fruit):
##    letter = fruit [index]
##    print index,letter
##    index = index +1
##
##name = 'montgomery'
##for letter in name:
##    print letter

##for letter in 'banana':
##    print letter
##
##s = 'Monty Python'
##print s[0:6]
##print s[:]

##
##fruit = 'banana'
##'n' in fruit

##greet = 'Hello Bob'
##zap = greet.lower()
##print zap

##fruit = 'banana'
##pos = fruit.find('na')
##print pos
##
##
##data = 'From michael.m@getvictorious.com Sat Jan 5'
##atpos = data.find('@')
##print atpos
##
##sppos = data.find(' ',atpos)
##print sppos
##
##host = data[atpos+1:sppos]
##print '@' + host


