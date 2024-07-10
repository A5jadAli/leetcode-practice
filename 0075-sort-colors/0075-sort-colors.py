class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, one, n = 0, 0, len(nums)

        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                one += 1
        
        for i in range(0, zeros):
            nums[i] = 0
        for i in range(zeros, zeros + one):
            nums[i] = 1
        for i in range(zeros + one, n):
            nums[i] = 2