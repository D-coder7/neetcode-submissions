class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = []
        for s in strs:
            encodedStr.extend([s, "..."])
        print("".join(encodedStr))
        return "".join(encodedStr)
    def decode(self, s: str) -> List[str]:
        print(s.split("..."))
        return s.split("...")[:-1] if s else []