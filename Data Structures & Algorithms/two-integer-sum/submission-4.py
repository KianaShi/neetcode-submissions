class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}
        for i in range(len(nums)):
            needs[target - nums[i]] = i
        
        for n in range(len(nums)):
            if nums[n] in needs:
                if n != needs[nums[n]]:
                    return[min(n, needs[nums[n]]), max(n, needs[nums[n]])]