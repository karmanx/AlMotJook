## 11장 해시 테이블
# 27 보석과 돌

*해시 테이블을 이용하지 않았음..

### code
def numJewelsInStones(jewels, stones):
    answer = 0
    for i in jewels:
        answer += stones.count(i)

    return answer


### test
J = "aA"
S = "aAAbbbb"

numJewelsInStones(J, S) # 3
