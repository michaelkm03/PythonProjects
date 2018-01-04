inp = raw_input('How many hours did you work this year?')
int_inp= int(inp)
rate = 15.75
payout = int_inp*rate
if payout < 40000:
    print str('Employee owed: $'), payout
else:
    print str('Employee owed: $40,000')
    bonus = payout*0.04
    print str('But you will get a bonus of '),bonus
x = int(98.6)
print x

