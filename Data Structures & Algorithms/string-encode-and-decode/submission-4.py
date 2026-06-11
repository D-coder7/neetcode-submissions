class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = [] #editing as list then converting to str to save space
        for s in strs:
            ans.extend([str(len(s)), "#", s]) 
            #always decodable, no matter what the strings are used
            # "#" is needed to signify end of strlen ex. "14#"
        print("".join(ans))
        return "".join(ans)
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            strlen = int(s[i:j])
            ans.append(s[j+1 : j+1+strlen])
            i = j + 1 + strlen
        return ans
