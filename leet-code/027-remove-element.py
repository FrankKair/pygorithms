class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        count = sum(1 for num in nums if num == val)
        for i in range(count):
            nums.remove(val)

        return len(nums)
