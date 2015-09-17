from Crypto.Util.number import *
from Crypto.Cipher import AES
import key

class ECP:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y
    
    def isinf(self):
        return self.x is None
    
    def __add__(self, Q):
        P = self
        if P.isinf(): (P, Q) = (Q, P)
        if Q.isinf(): return P
        if P == Q:
            l = (3 * P.x * P.x + A) * inverse(2 * P.y, p) % p
        elif P.x == Q.x:
            return None
        else:
            l = (Q.y - P.y) * inverse(Q.x - P.x, p) % p
        nx = (l * l - P.x - Q.x) % p
        ny = (l * (P.x - nx) - P.y) % p
        return ECP(nx, ny)
    
    def __sub__(self, Q):
        return self + (-Q)
    
    def __neg__(self):
        if self.x is None:
            return ECP()
        else:
            return ECP(self.x, -self.y % p)
    
    def __mul__(self, n):
        return pow(self, n)

    def __rmul__(self, n):
        return pow(self, n)
    
    def __pow__(self, n):
        P = self
        R = ECP()
        if n < 0:
            n = -n
            P = -P
        while n != 0:
            if n & 1 == 1:
                R += P
            P += P
            n >>= 1
        return R
        
    def __repr__(self):
        if self.x is None:
            return "ECP()"
        else:
            return "ECP(%d, %d)" % (self.x, self.y)

p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
A = -3
B = 41058363725152142129326129780047268409114441015993725554835256314039467401291
G = ECP(48439561293906451759052585252797914202762949526041747995844080717082404635286,
        36134250956749795798585127919587881956611106672985015071877198253568414405109)
e = 65537
DEM_IV = "\xAA"*16

def pad(m):
    l = AES.block_size - len(m) % AES.block_size
    return m + chr(l) * l

def unpad(m):
    return m[:-ord(m[-1])]

# public key: H = kG
def encrypt(H, m):
    r = getRandomRange(1, p)
    M = r * G
    S = e * M
    T = e * r * H - M
    #print "encrypt: M = %s" % M
    cipher = AES.new(long_to_bytes(M.x, 32), mode = AES.MODE_CBC, IV = DEM_IV)
    dem_c = bytes_to_long(cipher.encrypt(pad(m)))
    return (S, T, dem_c)

# secret key: k
def decrypt(k, c):
    (S, T, dem_c) = c
    M = k * S - T
    #print "decrypt: M = %s" % M
    cipher = AES.new(long_to_bytes(M.x, 32), mode = AES.MODE_CBC, IV = DEM_IV)
    return unpad(cipher.decrypt(long_to_bytes(dem_c, AES.block_size)))

#H = key.k * G
H = ECP(109751108484562349164127530101305240692682402677631328958397290100273187096405,
        90096893579313178361630896633528547111519814104799360692628427547223501810820)

if __name__ == "__main__":
    c = encrypt(H, key.flag)
    print c
    #print decrypt(key.k, c)
