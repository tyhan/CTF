import hashlib
import itertools
import string
import myhash
'''
Hashdesigner
(crypto70, solved by 28)


Description: There was this student hash design contest. All submissions were crap, but had promised to use the winning algorithm for our important school safe. We hashed our password and got '00006800007d'. Brute force isn't effective anymore and the hash algorithm had to be collision-resistant, so we're good to go, aren't we?

Attachment: crypto70.zip

Service: 188.166.133.53:10009
'''
def find_sha1(prefix):
    chars = string.lowercase + string.digits
    strings = itertools.product(chars, repeat=7)
    for a in strings:
        result = prefix + reduce(lambda x, y: x+y, list(a))
        myhash = hashlib.sha1(result).hexdigest()
        if myhash[36:] == "0000":
            return result

print find_sha1("91905744")


def find_hash(h):
    chars = string.lowercase + string.digits
    strings = itertools.product(chars, repeat=18)
    for a in strings:
        result = reduce(lambda x, y: x+y, list(a))
        my = myhash.myhash(result)
        if my == h:
            return result
            
print find_hash("00006800007d")

"""
nc  188.166.133.53 10009
You need to provide your proof of work: A sha1 hash with the last two bytes set to 0. It has 91905744 as the prefix. It should match ^[0-9a-z]{15}$
Enter work:91905744aaaaw0n
Thank you. Please continue with the login process...
Password: aaaaaaaaaaaaaacn6c
Logged in!
IW{FUCK_YOU_HASH_MY_ASS}
"""