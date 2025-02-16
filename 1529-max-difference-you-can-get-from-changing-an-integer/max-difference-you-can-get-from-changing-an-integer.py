class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """

        num_str = str(num)

        # Case 1: Maximize the number (Replace first non-9 digit with 9)
        for digit in num_str:
            if digit != '9':  # Find first non-9 digit
                max_num = num_str.replace(digit, '9')
                break
        else:
            max_num = num_str  # If all are 9, no change

        # Case 2: Minimize the number (Replace first digit or any non-0 digit accordingly)
        if num_str[0] != '1':  
            # If first digit is not 1, replace it with 1
            min_num = num_str.replace(num_str[0], '1')
        else:
            # Otherwise, replace the first non-1 digit (not first digit) with 0
            for digit in num_str[1:]:
                if digit not in ['0', '1']:  
                    min_num = num_str.replace(digit, '0')
                    break
            else:
                min_num = num_str  # If all are 1 or 0, no change

        return int(max_num) - int(min_num)

# Example usage:
solution = Solution()
print(solution.maxDiff(555)) 
 
        