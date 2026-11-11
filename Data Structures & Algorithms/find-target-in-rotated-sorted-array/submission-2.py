class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
                break
            elif nums[l] <= nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return -1