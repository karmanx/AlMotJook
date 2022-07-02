## 11장 해시 테이블
# 27 보석과 돌

*해시 테이블을 이용하지 않았음..

### code
def numJewelsInStones(self, jewels: str, stones: str) -> int:
    jw = list(jewels)
    st = list(stones)
    answer = 0
    for i in jw:
        answer += st.count(i)

    return answer
