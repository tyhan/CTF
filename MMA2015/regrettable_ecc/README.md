# MMA 2015
## regrettable ecc

#### 암호화
```python
def encrypt(H, m):
    r = getRandomRange(1, p)
    M = r * G
    S = e * M
    T = e * r * H - M
    #print "encrypt: M = %s" % M
    cipher = AES.new(long_to_bytes(M.x, 32), mode = AES.MODE_CBC, IV = DEM_IV)
    dem_c = bytes_to_long(cipher.encrypt(pad(m)))
    return (S, T, dem_c)
```

#### 복호화
```python
def decrypt(k, c):
    (S, T, dem_c) = c
    M = k * S - T
    #print "decrypt: M = %s" % M
    cipher = AES.new(long_to_bytes(M.x, 32), mode = AES.MODE_CBC, IV = DEM_IV)
    return unpad(cipher.decrypt(long_to_bytes(dem_c, AES.block_size)))
```

#### 풀이방법 
 * 목표: 메시지(M)을 복원하면 되는 문제
  - M = e^(-1) * e * M
  - M = e^(-1) * S
 
 * e의 역원을 찾음 ( e * e' = 1 MOD order(E))
  1. EC의 order를 구함
   - [order.sage](order.sage) ([sage](http://www.sagemath.org/)를 이용)
   - order = 5690927557662961033685528428582965261457195061979359507803867989619629786150
  2. inverse_mod( e, order)
   - [order.sage](order.sage)
   - inverse of e = 115792089210356248762697446949407573529996955224135760342422259061068512044369

 * M = e * S
  - M = ECP(56415482737989966166823194075124309191579838995662974007326170304203076762730, 66321143813061108250373685568872431883243259928989166706358343494697055267644)

 * M을 AES복호화를 한다.
  - [dec.py](dec.py)