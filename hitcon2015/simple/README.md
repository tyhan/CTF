#HITCON 2015 Qualification 2015
## simple (Crpyto 100)
Description
Become admin!
http://52.69.244.164:51913

simple-01018f60e497b8180d6c92237e2b3a67.rb

### Solution

1. Cookie의 auth에 json값이 암호화 되어 넘어감
  - 정상적인 동작에서는 username, password, db 세개의 키워드가 있음
  - 그러나 사용하는것은 "admin" 필드뿐임

2. CFB모드는 평문을 알면 키를 모르더라도 암호문을 생성해 낼수 있음
  - string1을 변조하여 string2로 대체할것임
  - string1 = {"username":"a","password":"a","db":"hitcon-ctf"}
  - string2 = {"username":"a","password":"a","admin":true}
  
3. 암호문 분석
  - 첫번째 블럭은 IV
  - 두번째 블럭은 {"username":"a",
  - 세번째 블럭은 "password":"a","
  - 네번째 블럭은 db":"hitcon-ctf"  =>  admin":true}
  - 다섯번째 블럭은 }  =>  버림
  
4. 암호문이 qkfkxkflwnrlakxukanfkduxkandkflrkuvnqkcjalkjalkjv 로 오게되면,
  - 1,2,3블럭은 그대로 사용, a = '123940dkvnzkdkfwqkfkxkflwnrlakxukanfkduxkandkflr'
  - 네번째 블럭 'kuvnqkcjalkjalkj' 부분은 b = 'db":"hitcon-ctf"' xor 'admin":true}' xor 'kuvnqkcjalkjalkj'

5. 변조한 암호문을 cookie의 auth값에 넣어주면 인증이 된다.
  - You're admin! The flag is hitcon{!!!!!!!!!!!!!!!!!!!!!!!!}