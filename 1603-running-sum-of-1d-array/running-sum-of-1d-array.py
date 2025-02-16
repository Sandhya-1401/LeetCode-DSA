class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = []
        current_sum = 0
        for num in nums:
            current_sum += num
            running_sum.append(current_sum)
        return running_sum

# Example usage:
a = Solution()
print(a.runningSum([1, 2, 3, 4])) 