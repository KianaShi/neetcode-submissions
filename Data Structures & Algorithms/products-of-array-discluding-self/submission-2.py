class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        left = 1
        right = 1
        for i in range(1, len(nums)):
            left = left * nums[i - 1]
            result[i] = left

        for j in range(len(nums) - 1, -1, -1):
            result[j] = result[j] * right
            right = right * nums[j]
        
        return result
        
