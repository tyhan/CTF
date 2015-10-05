#Defcamp CTF Qualification 2015
##No Crypto (Crypto 200)

The folowing plaintext has been encrypted using an unknown key, with AES-128 CBC:
Original: Pass: sup3r31337. Don't loose it!
Encrypted: 4f3a0e1791e8c8e5fefe93f50df4d8061fee884bcc5ea90503b6ac1422bda2b2b7e6a975bfc555f44f7dbcc30aa1fd5e
IV: 19a9d10c3b155b55982a54439cb05dce

How would you modify it so that it now decrypts to: "Pass: notAs3cre7. Don't loose it!" 

This challenge does not have a specific flag format.

####풀이 방법
메시지를 바꾸고 싶다는 문제
Original 메시지와 바꾸려는 메시지의 차이가 첫 블록만 다름
IV + plaintext를 처음 주어진 문제와 같게 맞추면 암호문이 같아짐

IV xor Original = IV' xor NewMsg
IV' = IV xor Original xor NewMsg