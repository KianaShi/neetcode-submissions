class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}
        for i in range(len(nums)):
            if nums[i] in needs:
                return [needs[nums[i]], i]
            else:
                needs[target - nums[i]] = i