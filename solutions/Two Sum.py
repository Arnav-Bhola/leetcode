class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = 0
        while True:
            newNums = nums[1:]
            otherNum = target - nums[0]
            if otherNum in newNums:
                secondIndex = newNums.index(otherNum) + 1 + index
                return [index, secondIndex]
            nums.pop(0)
            index += 1
