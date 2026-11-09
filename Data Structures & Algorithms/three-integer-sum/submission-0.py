class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    if nums[left] == nums[left - 1] and left > i + 1:
                        left += 1
                    elif right + 1 < len(nums) and nums[right] == nums[right + 1]:
                        right -= 1
                    else:
                        cur = [nums[i], nums[left], nums[right]]
                        result.append(cur)
                        left += 1
                        right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return result