## 6장 문자열 조작
# 04 가장 흔한 단어

### code
import string # string.punctuation 사용하기위함

def most_commonWord(par, ban):
    par_c = []
    par = par.lower().translate(str.maketrans('','',string.punctuation)).split()
    for i in par:
        if i in ban: # ban 목록에 있는건 빼고 append 
            continue
        par_c.append(i)

    return max(par_c, key = par_c.count) # key를 이용해서 par_c에서 가장 많이 count된 값을 return

### test code 
paragraph = "Bob hit a ball. the hit BALL flew far affer it was hit."
banned = ["hit"]
most_commonWord(paragraph,banned)
