# def div42by(divideBy):
#     try:
#         print '<-- there is the answer'
#         return 42 / divideBy
#     except:
#         print ('Error -- ')
# print (div42by(2))
# print (div42by(12))
# print (div42by(0))
# print div42by(1)
#
# numCats = raw_input('How many cats do you have?  ')
# #print type(numCats)
# try:
#     if numCats >=4:
#         print 'That is a lot of cats'
#     else:
#         print 'That is not that many cats'
# except ValueError:
#     response = 'This is not a number'
#     print response

# words = ['hello','123','things']
# user_question = raw_input('Enter your word here:  ')
#
# print words.index(user_question)

#
# glist = ['eggs', 'bread','milk','pasta']
# add = raw_input('Which items would you like to ADD:  ')
# if add in glist:
#     print add,'is already in your list'
# else:
#     glist.append(add)
# rm = raw_input('Which items would you like to REMOVE:  ')
# if rm in glist:
#     glist.remove(rm)
#     print 'You have removed',rm
# else:
#     print rm, 'is already in your list'
#     glist.remove(rm)
#
# print '--------------- YOUR LIST ---------------'
# print ''
# print ', '.join(glist)
#
# def triangle_area(base,height):
#     area = (1.0/2)*base*height
#     return area
#
# a1 = triangle_area(3,8)
# a2 = triangle_area(10,23)
# #print a1,' - ',a2
#
# # converts Fahrenheit to Celsius
# def fahrenheit2celsius(fahrenheit):
#     celsius = (5.0/9 * (fahrenheit-32))
#     return  celsius
#
# # test it
# c1 = fahrenheit2celsius(32)
# c2 = fahrenheit2celsius(212)
# print c1
# print c2
#
# # convert Fahrenheit to Kelvin
# def Fahrenheit2Kelvin(fahrenheit):
#     celsius = fahrenheit2celsius(fahrenheit)
#     kelvin = celsius + 273.15
#     return kelvin
#
# #test
#
# k1 = Fahrenheit2Kelvin(32)
# k2 = Fahrenheit2Kelvin(212)
# print k1
# print k2

#Write a function that prints all of the numbers between 1 and 10,000 that are either divisible by 7 or 33 but not both.
#
# def main():
#     for i in range(1,10001):
#         if i % 7 == 0 or i % 33 == 0:
#             if i % 7 == 0 and i % 33 ==0:
#                 break
#             else:
#                 print i
#
# main()



PROPERTIES_FILE = 'Reporter.properties'
REPORTER_FILE = 'Reporter.jar'

CMD = 'java -jar',REPORTER_FILE,'p='+PROPERTIES_FILE,'a=117736615'
print CMD