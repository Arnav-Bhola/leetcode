class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        while len(nums) >= 1:
            referenceNum = nums[0]
            otherNums = nums[1:]
            if referenceNum not in otherNums:
                return referenceNum
            nums.remove(referenceNum)
            nums.remove(referenceNum)
        return nums[0]
