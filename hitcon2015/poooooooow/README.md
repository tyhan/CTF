#HITCON 2015 Qualification 2015
##poooooooow (Crypto 200)
Description
Get the flag.
nc 52.69.244.164 9003

pow-0ba8661a3fb7764ad3380a5b29117b7f.rb

### Solution

1. BF를 막기 위하여 많은 연산이 필요한 문제를 넣어놓았음
  - BF를 하여 찾음 (가끔 답찾는데 오래 걸려서 timeout에 걸렸음)


2. 본 문제는 숫자(x)를 입력하면 x^flag mod p의 값을 출력함
  - DLP 문제임
  - p의 order는 p-1임
  - x의 값을 2^q (q = p-1의 약수)로 입력하여 x의 order를 2 x 3^336으로 만듬
  - sage를 이용하여 DLP를 풀어 flag값을 얻음

3. 결론
  - x읙 값을 수정하여 order가 적은 subgroup을 만둘수 있기 때문에 p를 선택할때에는 safe prime을 사용 해야함
