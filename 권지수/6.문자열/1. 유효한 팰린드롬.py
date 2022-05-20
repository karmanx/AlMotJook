# https://leetcode.com/problems/valid-palindrome/
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.



class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper() # 대소문자를 구분하지 않음
        s = re.sub('[^a-zA-Z0-9]', '', s) # 정규식으로 특수기호 없애기
        
        r = s[::-1] # 인덱싱으로 역순배열, str이므로 s.reverse 안됨!
        
        return s == r


# 이전에 과제로 [::-1] 인덱싱을 사용한 적 있어서 기억을 더듬어가며 풀었다.
# 다만 정규식을 외울 수 없어서.. 다른 방법으로도 풀어봤다.



class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.upper()
        strs = []
        
        for char in s:
            if char.isalnum(): # 특수기호 판별해서 append
                strs.append(char)
        
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        
        return True


# .isalnum() 문자열이 알파벳([a-zA-Z])과 숫자([0-9])로만 구성되었는지 확인하는 파이썬 문자열 메소드
# 이런 메소드도 있었구나..
