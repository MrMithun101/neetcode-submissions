class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped_anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26 #make a count array for each word (a-z)

            for letter in word: #loop through each letter in and increase its count
                count[ord(letter) - ord('a')] += 1


            grouped_anagrams[tuple(count)].append(word)

        return list(grouped_anagrams.values())

            