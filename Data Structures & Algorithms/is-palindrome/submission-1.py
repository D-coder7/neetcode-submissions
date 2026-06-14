class Solution:
    def isPalindrome(self, s: str) -> bool:
        charlist = []
        for c in s:
            if c.isalnum():
                charlist.append(c.lower())

        for i in range(len(charlist)):
            if charlist[i] != charlist[len(charlist)-1-i]:
                return False
        return True