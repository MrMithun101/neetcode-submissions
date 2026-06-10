class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the separator '#'
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # The actual word starts after '#'
            word_start = j + 1
            word_end = word_start + length

            result.append(s[word_start:word_end])

            # Move to the next encoded word
            i = word_end

        return result
