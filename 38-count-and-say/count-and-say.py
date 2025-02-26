class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)  # Get the previous term
        result = ""
        count = 1

        for i in range(1, len(prev)):
            if prev[i] == prev[i - 1]:
                count += 1
            else:
                result += str(count) + prev[i - 1]  # Append count and digit
                count = 1  # Reset count for new digit

        result += str(count) + prev[-1]  # Append the last counted sequence
        return result
