class Solution:
    def firstUniqChar(self, s):
        # Step 1: Count frequency of each character
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Step 2: Find the first character with frequency 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        return -1
