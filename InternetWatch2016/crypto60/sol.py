from Crypto.PublicKey import RSA

'''
Oh Bob!
(crypto60, solved by 79)


Description: Alice wants to send Bob a confidential message. They both remember the crypto lecture about RSA. So Bob uses openssl to create key pairs. Finally, Alice encrypts the message with Bob's public keys and sends it to Bob. Clever Eve was able to intercept it. Can you help Eve to decrypt the message?
Attachment: crypto60.zip
'''

##################################################################
# https://gist.github.com/tylerl/1239116
# Part of find_inverse below
# See: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def eea(a,b):
	if b==0:return (1,0)
	(q,r) = (a//b,a%b)
	(s,t) = eea(b,r)
	return (t, s-(q*t) )

# Find the multiplicative inverse of x (mod y)
# see: http://en.wikipedia.org/wiki/Modular_multiplicative_inverse
def find_inverse(x,y):
	inv = eea(x,y)[0]
	if inv < 1: inv += y #we only want positive values
	return inv
######################################################################


f = open("bob.pub")
f.readline()
bob = f.readline().strip()
bob += f.readline()
f.close()
bobDER = bob.decode("base64")
keyPub = RSA.importKey(bobDER)
#17963604736595708916714953362445519 * 20016431322579245244930631426505729
p = 17963604736595708916714953362445519
q = 20016431322579245244930631426505729
if keyPub.key.n is (p * q):
    print "n = "+ keyPub.key.n
d = find_inverse(keyPub.key.e, (q-1) *(p-1))
key = RSA.construct((keyPub.key.n,keyPub.key.e, d ,p, q))


f = open("bob2.pub")
f.readline()
bob2 = f.readline().strip()
bob2 += f.readline()
f.close()
bob2DER = bob2.decode("base64")
key2Pub = RSA.importKey(bob2DER)
#16514150337068782027309734859141427 * 16549930833331357120312254608496323
q2 = 16514150337068782027309734859141427
p2 = 16549930833331357120312254608496323
if key2Pub.key.n is (p2 * q2):
    print "n2 = "+ key2Pub.key.n
d2 = find_inverse(key2Pub.key.e, (q2-1) *(p2-1))
key2 = RSA.construct((key2Pub.key.n,key2Pub.key.e, d2 ,p2, q2))

f = open("bob3.pub")
f.readline()
bob3 = f.readline().strip()
bob3 += f.readline()
f.close()
bob3DER = bob3.decode("base64")
key3Pub = RSA.importKey(bob3DER)
#17357677172158834256725194757225793 * 19193025210159847056853811703017693
p3 = 17357677172158834256725194757225793
q3 = 19193025210159847056853811703017693
if key3Pub.key.n is (p3 * q3):
    print "n3 = "+ key3Pub.key.n
d3 = find_inverse(keyPub.key.e, (q3-1) *(p3-1))
key3 = RSA.construct((key3Pub.key.n,key3Pub.key.e, d3 ,p3, q3))


f = open("secret.enc")
enc = f.readline().strip()
f.readline()
enc2 = f.readline().strip()
f.readline()
enc3 = f.readline().strip()
f.close()


#enc = "DK9dt2MTybMqRz/N2RUMq2qauvqFIOnQ89mLjXY="
#enc2 = "AK/WPYsK5ECFsupuW98bCFKYUApgrQ6LTcm3KxY="
#enc3 = "CiLSeTUCCKkyNf8NVnifGKKS2FJ7VnWKnEdygXY="

flag = key.decrypt(enc.decode("base64"))
flag += key2.decrypt(enc3.decode("base64"))
flag += key3.decrypt(enc2.decode("base64"))

#print flag.encode("hex")
#print flag

f = open("flag",'w')
f.write(flag)
f.close()

#strings flag