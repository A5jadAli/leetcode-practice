class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for i in range(len(s)):
            dict[s[i]] = 1 + dict.get(s[i], 0)
        for index, no in enumerate(s):
            if dict[no] == 1:
                return index
        return -1

        