class Solution(object): 
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num  
        return result

nums = [2, 2, 1]
sol = Solution()
print(sol.singleNumber(nums))  
