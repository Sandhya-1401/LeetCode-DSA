class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if low % 2 == 0:
            low += 1
        
        if high % 2 == 0:
            high -= 1
    
        if low > high:
            return 0
        return (high - low) // 2 + 1

low=3
high=7

a=Solution()
print(a.countOdds(low,high))