class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grpmaps = [] #{hashmap:index}
        sol = []
        for s in strs:
            ind = -1
            newmap = dict(Counter(s))
            for i, mapi in enumerate(grpmaps):
                if newmap == mapi:
                    sol[i].append(s)
                    break
            else:
                sol.append([s,])
                grpmaps.append(newmap)
        return sol
