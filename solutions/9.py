class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False  # Negative integers can never be palindromes.
        
        tempNumber = xa
        reversedNumber = 0
        while tempNumber > 0:
            reversedNumber *= 10
            lastDigit = tempNumber % 10
            reversedNumber += lastDigit
            tempNumber //= 10

        if reversedNumber == x:
            return True
        
