## 6장 문자열 조작
# 01 유효한 팰린드롬

### code
def palindrome_check(lst): #palindrome인지 확인하는 함수 정의
  lst1 = lst.lower().replace(" ", "") #입력한 list의 대소문자를 소문자로 통일하고 띄어쓰기를 제거한 문자열을 다른 리스트에 저장한다
  lst2 = lst1[::-1] #처음부터 끝까지 -1칸 간격으로 #즉, 역순으로 읽은 문자열을 또 다른 리스트에 저장한다
  if lst1 == lst2: #앞에서 비교를 위해 만든 리스트들이 동일한지 확인한다 #일치하면
    print(True) #palindrome 이다
  else: #일치하지 않으면 palindrome이 아니다
    print(Fasle)

### test code
List = "Race a car"
palindrome_check(List)
