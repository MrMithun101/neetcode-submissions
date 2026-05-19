class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): #Check if the lengths of the two words match
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)

        if s_count == t_count:
            return True

        else:
            return False

        
        