class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max_words = 0
        for b in sentences:
            word_count = len(b.split())
            max_words = max(max_words, word_count)
        return max_words

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
a=Solution()
print(a.mostWordsFound(sentences))