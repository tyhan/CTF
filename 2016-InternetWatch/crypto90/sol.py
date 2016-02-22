from pwn import *
import re
'''
Bank
(crypto90, solved by 39)

Description: Everyone knows that banks are insecure. This one super secure and only allows only 20 transactions per session. I always wanted a million on my account.
Attachment: crypto90.zip
Service: 188.166.133.53:10061
'''

def convert(data):
    result = data.decode("hex")[:12]
    post = data.decode("hex")[12:]
    #" 5000"
    #"99999"    
    pos = chr(ord(post[0]) ^ ord(" ") ^ ord("9"))
    pos += chr(ord(post[1]) ^ ord("5") ^ ord("9"))
    pos += chr(ord(post[2]) ^ ord("0") ^ ord("9"))
    pos += chr(ord(post[3]) ^ ord("0") ^ ord("9"))
    pos += chr(ord(post[4]) ^ ord("0") ^ ord("9"))
    result += pos
    return result.encode("hex")

r = remote ("188.166.133.53",10061)
#logo
r.recvuntil("Command:")

for x in range(0,20):
    r.sendline("create 5000")
    text = r.recvuntil("Command:", timeout = 2)
    print text
    text = re.search("[0-9a-f]{34}", text).group(0)
    text = convert(text)
    r.sendline("complete %d %s" % (x,text))
    print r.recvuntil("Command:", timeout = 2)

print r.recvall()