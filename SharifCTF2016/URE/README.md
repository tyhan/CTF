## URE

### Problem

* Let p be a prime, and g be an element of ℤp of prime order q.
* Let x ∈ ℤq be the private key, and h = gx (mod p) be the public key.
* To encrypt a message m ∈ ℤ*p, pick two random values r, s ∈ ℤq, and compute the ciphertext as follows:
 - (a, b, c, d) = (g^r, h^r, g^s, mh^s).

* Download a valid ciphertext σ = (a, b, c, d) below, and compute another valid ciphertext σ' = (a', b', c', d') such that:
 - σ and σ' decrypt to the same message;
 - a ≠ a' and b ≠ b' and c ≠ c' and d ≠ d'.

``` 
p = 0x8000048d1d71b57838b7d90ebc63b8c853f3af1af87ce2db5593f3386ae5139d040d3844e31db723d39cdd7717c8cffc26f6f877b5c85ca8e595ca687c07c773

a = 0x21068b690f5438360063bb80799a95af7bbb83fa399376af9ad21e0cef3d5233aa313fe1960ccfd87e8a4b1dba0e053d89bfebd4bc57170147462fafef44c9c7
b = 0x436c161645052a76c1f7c976da63f61987f5f9bf7cb810a0e6fb1ea593aa9397c7b7cb0488f0f14cf93c79eef967a4b2a39388da1a357077d30a6f8b2a2c97e7
c = 0x7dd53b07c05ea2aca88bcbdd58601fa344918848107431ae7710542ea625abb335c27352c1bd2ef01359adb19b1bee77edc07ab0b41b9766392fc154f7891268
d = 0x1a50308011b409460d504cc7cddd61cdff1bda0774d1329b59606df274bce81a7e4b15830ddd4e684e3f2422d36bd52220134881db560be0a34c76a9c5bbb6be
```

### Solustion
* 새로운 r, s를 만들어야 함
 - (g^r, h^r, g^s, mh^s)
 
* r' = 2r, s' = r + s 
 - (a, b, c, d)
 - (g^r', h^r', g^s', mh^s')
 - (g^2r, h^2r, g^(r+s), mh^(r+s))
 - (g^2r, h^2r, g^(r+s), mh^(r+s))
 - (g^r * g^r, h^r * h^r, g^r * g^s, m * h^r * h^s)
 - (a * a, b * b, c * a, d * b)
 