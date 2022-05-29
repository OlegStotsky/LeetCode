from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        i = 0
        result = []
        while i < len(nums) and nums[i] <= 0:
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums[i], i, nums, result)
            i += 1
        return result
                
    def twoSum(self, cur, i, nums, result):
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[l] + nums[r] + cur
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                result.append([cur, nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
