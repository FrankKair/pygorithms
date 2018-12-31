class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index, x in enumerate(nums):
            complement = target - x
            if complement in seen:
                return [seen[complement], index]
            seen[x] = index
        return []
