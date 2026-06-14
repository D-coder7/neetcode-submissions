class Solution:
    def isPalindrome(self, s: str) -> bool:
        charlist = []
        for c in s:
            if c.isalnum():
                charlist.append(c.lower())

        return charlist == charlist[::-1]