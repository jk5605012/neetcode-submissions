class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(' ', '')
        s = s.replace('?', '')
        s = s.replace('.', '')
        s = s.replace(',', '')
        s = s.replace("'", '')
        s = s.replace(":", '')
        print(s)
        s_len = len(s)
        mid = s_len // 2
        
        if not s:
            return True
        if s_len % 2 == 0:
            mid_2 = mid - 1
            if s[mid] != s[mid_2]:
                return False
            for i in range((s_len // 2)-1):
                mid += 1
                mid_2 -= 1
                if s[mid] != s[mid_2]:
                    return False
            return True
        else:
            for i in range(s_len // 2):
                if s[mid+i+1] != s[mid-i-1]:
                    return False
            return True