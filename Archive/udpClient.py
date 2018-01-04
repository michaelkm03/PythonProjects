import socket

def Main():
    host = '127.0.0.1'
    port = 5001

    server = ('127.0.0.1',5000)

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind((host,port))

    user_name = raw_input('What is your username?  ')
    message = raw_input('~> ')
    while message !='q':
        s.sendto(user_name.encode('utf-8'),server)
        s.sendto(message.encode('utf-8'),server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        #print "Received from server:  "
        message = raw_input('~> ')
    s.close()

if __name__ == '__main__':
    Main()