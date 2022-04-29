## 6장 문자열 조작
# 06 가장 긴 펠린드롬

### code
def longest_pelind(s):
    s = s.lower()
    result = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] and str(s[i:j]) == str(s[i:j])[::-1]: #앞 뒤가 같은 녀석 찾기
                result.append(s[i:j])

    # 이제 result 중에서 가장 알파벳 수가 많은 걸 리턴
    result.sort(key=len)
    result_max = len(result[-1])

    answer = []
    for i in range(len(result)):
        if len(result[i]) >= result_max:
            answer.append(result[i])
    return answer


### test code 
testString = "babad"
longest_pelind(testString) # ['bab', 'aba']

testString2 = "cbbd"
longest_pelind(testString2) # ['bb']
