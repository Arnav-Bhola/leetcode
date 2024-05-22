class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        
        tempNumber = x
        reversedNumber = 0
        while tempNumber > 0:
            reversedNumber *= 10
            lastDigit = tempNumber % 10
            reversedNumber += lastDigit
            tempNumber //= 10

        if reversedNumber == x:
            return True
        
