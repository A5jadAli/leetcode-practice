class Solution():
    def myAtoi(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0

        sign = 1
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        num = 0
        for char in s:
            if not char.isdigit():
                break
            num = num*10 + int(char) # whenever you want to convert str to int, this formula will be used

        num *= sign
        num = max(min(num, 2**31-1), -2**31)
        return num
