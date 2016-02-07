##High-speed RSA Keygen

### Problem
RSA

n=A4E20DDB854955794E7ABF4AE40051C0FC30488C82AB93B7DD046C1CC094A54334C97E84B523BD3F79331EBEAF5249200D729A483D5B8D944D58DF18D2CA9401B1A1A6CDA8A3AC5C234A501794B76886C426FAC35AD9615ADAB5C94B58C03CCFFA891CE0156CBC14255F019617E40DE9124FBBE70D64CD823DCA870FF76B649320927628250D47DB8DFA9BBCE9964CB3FE3D1B69845BD6FA2E6938DDA1F109E5F4E4170C845B976BBD5121107642FC00606208F9BC83322532739BCFEAF706FB2AF985EBD9769C7FBD50ECBF55566BD44FB241F9FD2DE25069AA8C744F0558514F1E9C8E4297A4D4B25D9F2B7494B466C2E6E2834BA68C5C824215018368B4FB
e=10001

### Solustion

* 문제에서 prime을 빠르게 구하기 위해서 p, q 선정 방법을 특이하게 구현하였음
 - pi = 3 * ... * 433
 - kp, kq = randrange(1, 2^12) + 2^12 + 2^13 + 2^14 + 	2^15 + 2^16 + 2^17 + 2^18 + 2^19
 - tq, tq = randrange(1, 2**399), pi와 서로소

* p, q
 - p = kp * pi * 2^400 + tp
 - q = kq * pi * 2^400 + tq

* pi * 2^400 를 X로 치환
 - p = kp * X + tp
 - q = kq * X + tq

* n = p*q
 - (kp * X + tp) * (kq * X + tq)
 - (kp * kq)*X^2 +(kp * tq + kq * tp) * X + tp * tq
 - a * X^2 + b * X + c

* 계수를 따로 쓰면 
 - a = kp * kq
 - b = kp * tq + kq * tp
 - c = tp * tq

* a를 인수분해
 - factor(1094695521128)
 - 2^3 * 11 * 17 * 2797 * 261619

* kp가 될수 있는것은 2^20보다 작은 수이여야 하기 때문에
 - 261619, 2 * 261619 or 2 * 2 * 261619

* sage를 이용하여 다항식을 해결
 - sage: solve([eq1,eq2,eq3,kp == 261619],kp,kq,tp,tq)
 - sage: solve([eq1,eq2,eq3,kp == 261619*2],kp,kq,tp,tq)
 - sage: solve([eq1,eq2,eq3,kp == 261619*4],kp,kq,tp,tq)
 - 세 명령여의 결과 중에 나누기가 없는 결과를 선택

* kp, kq, tp, tq를 구하였음 (즉, p, q를 구함)
 - kp = 1046476
 - kq = 1046078
 - tp = 1043948703640430782418404568397379785573236195992474448505791212189061002365437316289912568373152734060191290086628880727
 - tq = 661210345469456402100489805444522037620875173669321847796588356919712449396916319769138366893562527225063254775914077949

 - q = kq * pi * 2**400 + tq
 - p = kp * pi * 2**400 + tp

* 인수분해 하였으므로 복호화
 - d = e^(-1) mod (p-1(q-1)
 - message = c ^ d mod n
