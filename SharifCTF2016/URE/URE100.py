from Crypto.Util.number import *
from Crypto.Cipher import AES

#Note: You require neither g nor h to solve this challenge!

p = 0x8000048d1d71b57838b7d90ebc63b8c853f3af1af87ce2db5593f3386ae5139d040d3844e31db723d39cdd7717c8cffc26f6f877b5c85ca8e595ca687c07c773

a = 0x21068b690f5438360063bb80799a95af7bbb83fa399376af9ad21e0cef3d5233aa313fe1960ccfd87e8a4b1dba0e053d89bfebd4bc57170147462fafef44c9c7
b = 0x436c161645052a76c1f7c976da63f61987f5f9bf7cb810a0e6fb1ea593aa9397c7b7cb0488f0f14cf93c79eef967a4b2a39388da1a357077d30a6f8b2a2c97e7
c = 0x7dd53b07c05ea2aca88bcbdd58601fa344918848107431ae7710542ea625abb335c27352c1bd2ef01359adb19b1bee77edc07ab0b41b9766392fc154f7891268
d = 0x1a50308011b409460d504cc7cddd61cdff1bda0774d1329b59606df274bce81a7e4b15830ddd4e684e3f2422d36bd52220134881db560be0a34c76a9c5bbb6be


con = 2
con_p = inverse(con, p)

#print con
#print con_p

print hex((a * a) % p)
print hex((b * b) % p)
print hex((c * a) % p)
print hex((d * b) % p)


#SharifCTF{546ba7b2e279d3f36d262347ad220396}