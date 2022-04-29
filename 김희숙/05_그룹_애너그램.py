## 6장 문자열 조작
# 05 그룹 애너그램

### code
def group_anagrams(lst):
    result = {}

    for str in strs:
        s = ''.join(sorted(str)) # 알파벳 단위로 쪼개서 sort후 다시 연결
        result[s] = result.get(s,[]) + [str] # 위에서 연결한 건 key로 
    return(list(result.values()))


### test code 
strs = ["eat","tea","tan","ate","nat","bat"]
group_anagrams(strs)


##### 실~패 #####
temp_d = dict()
temp = []
a = []
a.append([])
for i in strs:
    for p in str(i):
        print(i)
        temp.append(p)
    temp.sort()
    temp_d[i] = temp
    temp = []

#for i in temp_d.values():
#    if value ==    
# 이제 value값이 같은 key들끼리 묶어서 출력하고싶어~
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
##### 실~패 #####  
