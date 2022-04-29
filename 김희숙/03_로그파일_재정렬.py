## 6장 문자열 조작
# 03 로그파일 재정렬

### code
def log_re_arrange(lst):
    digit = [] # 숫자 그릇
    letter = [] # 문자 그릇
    for i in lst:
        keep = i.split(' ') # space 구분자로 쪼개기
        if (keep[1].isnumeric() == True): # 숫자이면
            digit.append(i) # 숫자 그릇에 넣고
        else: # 문자이면
            letter.append(i) # 문자 그릇에 
    
    letter.sort(key = lambda let: (let.split(' ')[1:], let.split(' ')[0])) # sort의 key 매개변수를 이용해서 정렬 
    # 정렬의 기준은 space로 쪼갠 뒤 index 1번부터~문자 순, 만약 같으면 식별자([0]) 순서로 정렬
    return (letter + digit)

### test code
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
log_re_arrange(logs)
