# Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

# Return the power of the string.

class Solution:
    def maxPower(self, s: str) -> int:

        map = dict()
        
        for i in range(len(s)):
            letter = s[i]
            if letter not in map:
                map[letter] = 0
            else:
                map[letter]+=1

        print(map)

sl = Solution()
sl.maxPower( "hello world")