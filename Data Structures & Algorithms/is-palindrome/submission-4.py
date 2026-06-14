class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                print(s[l], "is not alnum")
                l += 1
            while l < r and not s[r].isalnum():
                print(s[r], "is not alnum")
                r -= 1
            
            if s[l].lower() != s[r].lower():
                print(s[l], "!=", s[r])
                return False
            l += 1
            r -= 1
        return True