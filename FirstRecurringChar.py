## Google interview question : First recurring char in given string
class Solution:
    def first_recurring_char(self,str):
        counts = {}
        for char in str:
            if char in counts:
                return char
            else:
                counts[char] = 1
        return None


sl = Solution()
str = "BCDAEFD"
print(sl.first_recurring_char(str))
