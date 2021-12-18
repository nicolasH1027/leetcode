class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        def generate(words):
            for word in words:
                for c in word:
                    yield c
            yield None
        
        for a, b in zip(generate(word1), generate(word2)):
            if a != b:
                return False
        
        return True