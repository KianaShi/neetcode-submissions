class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            left = nums[i]
            right = target - left
            if right in nums[i+1:]:
                return [i, nums.index(right, i + 1)]