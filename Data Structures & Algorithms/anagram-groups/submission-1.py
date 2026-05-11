class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped_anagrams = defaultdict(list)

        for words in strs:
            count = [0] * 26

            for letter in words:
                count[ord(letter) - ord("a")] += 1

            grouped_anagrams[tuple(count)].append(words)

        return list(grouped_anagrams.values())




        