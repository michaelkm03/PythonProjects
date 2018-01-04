import socket
import udpClient

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    print '#############'
    print 'SEVER STARTED'
    print ' '
    while True:
        data, addr = s.recvfrom(1024)
        print 'Message from:  ' + str(addr)
        print udpClient.user_name
        data = data.decode('utf-8')
        data = data.upper()
        #print 'Sending:  ray@iamchachi.com' + data
        s.sendto(data.encode('utf-8'),addr)
    c.close()

if __name__ == '__main__':
    Main()