class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

# Example usage
sol = Solution()
n = 11
print(sol.hammingWeight(n))  # Output: 3
