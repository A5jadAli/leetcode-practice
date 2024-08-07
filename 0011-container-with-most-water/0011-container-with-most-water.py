class Solution:
    def maxArea(self, height: List[int]) -> int:
        curr = 0
        maxx = 0
        l, r = 0, len(height) - 1
        while l < r:
            curr = min(height[l], height[r]) * (r - l)
            maxx = max(curr, maxx)
            if height[l] < height[r]:
                l+= 1
            else:
                r -= 1
        
        return maxx

        '''
        time complexity = O(n)
        space complexity = constant or O(1)
        '''
