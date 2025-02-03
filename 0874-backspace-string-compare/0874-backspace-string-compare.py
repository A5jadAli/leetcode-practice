class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        for char in s:
            if char == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(char)
        
        # Process the second string
        stack_t = []
        for char in t:
            if char == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(char)
        
        # Compare the two stacks
        return stack_s == stack_t