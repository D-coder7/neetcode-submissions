class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {s[0]: [0, 1]} # char: [index, streak, gap, streak, gap...]

        for i in range(1, len(s)):
            if s[i] in mp:
                if i - mp[s[i]][0] > 1:
                    mp[s[i]].append(i-mp[s[i]][0]-1)
                    mp[s[i]].append(1)
                    mp[s[i]][0] = i
                else:
                    mp[s[i]][-1] += 1
                    mp[s[i]][0] = i
            else:
                mp[s[i]] = [i, 0, i, 1]
        
        maxl = 0
        for c,v in mp.items():
            l,r = 1,1 #streak start
            length = 0
            remaining = k
            while r<len(v):
                length += v[r]
                maxl = max(maxl, length + remaining)
                if r == len(v)-1:
                    break
                while l <= r and v[r+1] > remaining:
                    length -= v[l] + v[l+1]
                    remaining += v[l+1]
                    l += 2
                length += v[r+1]
                remaining -= v[r+1]
                r += 2
        
        return min(maxl, len(s))


