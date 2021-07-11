from sender import send_message

# Build a happy little message folloewd by a newline
buf = 'A'*3000
buf += 'Python Script'
buf += '\n'

send_message(buf)