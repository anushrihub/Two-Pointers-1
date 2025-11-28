# https://leetcode.com/problems/sort-colors/

# brutforce Tc- O(n log n) Sc- (1)
# class Solution:
#     def sortColors(self,nums: list[int]) -> list[int]:
#         nums.sort()
#         return nums

# brutforce Tc- (n2) Sc-(1)
class Solution:
    def sortColors(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

