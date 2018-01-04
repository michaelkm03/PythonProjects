month = str(raw_input('Enter the month you were born: '))
day = str(raw_input('Enter the day you were born: '))
year = int(raw_input('Enter the year you were born: '))
today = int(raw_input('What year is it: '))
salary = float(raw_input('How much do you make a year: '))
future_year = float(raw_input('Enter the year you expect to be a millionaire: '))
age = int(2016) - year

def birthday():
        return month + " " + day + ", " + str(year)

print "Your birthday is " + birthday()

year_int = float(year)

need_to_save = (salary - (1000000.00/(future_year - today))) 

per_paycheck = need_to_save/24

print "You need to save " + "$" + str(need_to_save) + " per year"
print "That's " + "$" + str(per_paycheck) + "per paycheck"
