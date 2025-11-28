# https://leetcode.com/problems/3sum/

# brutforce O(n3)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        target = 0
        result_set = set()
        
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == target:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        result_set.add(tuple(triplet))
        return [list(t) for t in result_set]