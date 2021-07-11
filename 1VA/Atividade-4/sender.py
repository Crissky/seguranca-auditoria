import socket


def send_message(string_message):    
    # Set up IP and PORT we1re connecting to
    RHOST = '127.0.0.1'
    RPORT = 31337

    # Create a TCP connection (socket)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST, RPORT))

    # Send the happy little message down the socket
    s.send(string_message)

    # Print out what we sent
    print 'Sent: {}'.format(string_message)

    # Recive same data from the socket
    data = s.recv(1024)

    # Print out what we received
    print f'Received: {}'.format(data)
