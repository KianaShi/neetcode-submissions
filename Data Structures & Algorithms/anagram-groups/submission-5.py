class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        same_words = {}
        for word in strs:
            char_count = Counter(word)
            char_tuple = tuple(sorted(char_count.items()))
            if char_tuple in same_words:
                same_words[char_tuple].append(word)
            else:
                same_words[char_tuple] = [word]
        result = []
        for words in same_words:
            result.append(same_words[words])
        return result