'''
No Crypto (Crypto 200)
The folowing plaintext has been encrypted using an unknown key, with AES-128 CBC:
Original: Pass: sup3r31337. Don't loose it!
Encrypted: 4f3a0e1791e8c8e5fefe93f50df4d8061fee884bcc5ea90503b6ac1422bda2b2b7e6a975bfc555f44f7dbcc30aa1fd5e
IV: 19a9d10c3b155b55982a54439cb05dce

How would you modify it so that it now decrypts to: "Pass: notAs3cre7. Don't loose it!" 

This challenge does not have a specific flag format.
'''

from Crypto.Cipher import AES

problem  = "Pass: notAs3cre7. Don't loose it!"
original = "Pass: sup3r31337. Don't loose it!"
encrypted = "4f3a0e1791e8c8e5fefe93f50df4d8061fee884bcc5ea90503b6ac1422bda2b2b7e6a975bfc555f44f7dbcc30aa1fd5e".decode("hex")
iv = "19a9d10c3b155b55982a54439cb05dce".decode("hex")


def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

print xor_strings(problem, original).encode("hex")
diff = xor_strings(problem[:16], original[:16])
print diff.encode("hex")
new_iv = xor_strings(iv,diff)

print new_iv.encode("hex")


#aes = AES.new(key, AES.MODE_CBC, iv).encrypt(original)