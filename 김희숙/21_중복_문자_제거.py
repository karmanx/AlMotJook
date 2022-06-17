## 9장 스택, 큐
# 21 중복 문자 제거

### code
def del_dupLetter(s):
    keep = []
    for i in str(s):
        if i not in keep:
            keep.append(i)
    return ''.join(s for s in sorted(keep))
 

### test code
s = "bcabc"
del_dupLetter(s) #abc

s = "cbacdcbc"
del_dupLetter(s) #abcd



### stack, que
def removeDuplicateLetters(self, s: str) -> str:
	# counter 숫자 세기; seen 처리한 문자 확인; stack 스택 쌓기 용도
	counter, seen, stack = collections.Counter(s), set(), []

	for char in s:
		counter[char] -= 1
		
		# 이미 처리된 문자라면 스킵
		if char in seen:
			continue
		
		# 만약 현재 문자 char가 스택에 쌓여 있는 문자(이전 문자보다 앞선 문자)이고
		# 뒤에 다시 붙일 수 있는 문자가 남아있다면(카운터가 0 이상이라면)
		while stack and char < stack[-1] and counter[stack[-1]] > 0 :
			seen.remove(stack.pop()) # 즉, 뒤에 붙일 문자가 남아 있다면 스택에서 제거
      
		# 스택은 앞에서부터 차례대로 쌓아 나간다.
		stack.append(char)
		seen.add(char)

return ''.join(stack)
