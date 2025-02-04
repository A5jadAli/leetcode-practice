class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        else:
            return [-1, -1]

        start = m
        while start - 1 >= 0 and nums[start - 1] == target:
            start -= 1
        end = m
        while end + 1 < len(nums) and nums[end + 1] == target:
            end += 1

        return [start, end] 