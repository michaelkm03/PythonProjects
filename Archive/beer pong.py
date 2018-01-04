from random import randint

print'--- PLAYER ONE ---'
player1 = raw_input('ENTER YOUR NAME:  ')
print'--- PLAYER TWO ---'
player2 = raw_input('ENTER YOUR NAME:  ')

player2cups = 10
player1cups = 10

def P1Shot():
    print player1,'its your turn...SHOOT!'
    print''
    global player2cups
    if player2cups > 0:
        shot = randint(0,100)
        if 0 <= shot <= 50:
            player2cups = player2cups - 1
            print 'MADE! ',player2,'has',player2cups,'left'
        else:
            print 'MISS,',player2,'has',player2cups,'left'
    else:
        print '################# YOU LOSE,', player2, 'WINS!!! #################'


def P2Shot():
    print player2, 'its your turn...SHOOT!'
    print''
    global player1cups
    if player1cups > 0:
        shot = randint(0, 100)
        if 51 <= shot <= 100:
            player1cups = player1cups - 1
            print 'MADE! ', player1, 'has', player1cups, 'left'
        else:
            print 'MISS,', player1, 'has', player1cups, 'left'
    else:
        print '################# YOU LOSE,',player1,'WINS!!! #################'

while player1cups!=0 or player2cups!=0:
    P1Shot()
    P2Shot()