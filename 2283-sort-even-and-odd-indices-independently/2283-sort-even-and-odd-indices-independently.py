class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_indices = sorted(nums[0::2])
        odd_indices = sorted(nums[1::2], reverse=True)

        result = []
        even_ptr, odd_ptr = 0, 0

        for i in range(len(nums)):
            if i%2 == 0:
                result.append(even_indices[even_ptr])
                even_ptr += 1
            else:
                result.append(odd_indices[odd_ptr])
                odd_ptr += 1
        
        return result