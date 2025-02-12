class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        res = ""
        for i in range(len(s)):
            d[indices[i]] = s[i]
        indices.sort()
        for i in indices:
            res+=d[i]      
        return res