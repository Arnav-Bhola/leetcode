class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        number = 0
        for i in nums:
            number = number ^ i
        return number
