from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = defaultdict(set)
        for idx, x in enumerate(nums):
            s = seen[x]
            s.add(idx)
        
        n = len(nums)
        ans = set()
        for i in range(0, n):
            for j in range(i+1, n):
                s = nums[i] + nums[j]
                missing = -s
                if missing in seen:
                    seen_set = seen[missing]
                    seen_set_len = len(seen_set)
                    if i in seen_set:
                        seen_set_len -= 1
                    if j in seen_set:
                        seen_set_len -= 1
                    if seen_set_len > 0:
                        ans.add(tuple(sorted(([nums[i], nums[j], missing]))))
        
        result = []
        for x in ans:
            result.append(list(x))
        return result
