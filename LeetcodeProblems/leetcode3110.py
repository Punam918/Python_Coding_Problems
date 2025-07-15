class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """

        score = 0
        for i in range(len(s)-1):
            score += abs(ord(s[i]) - ord(s[i+1]))

        return score
        

#Tc = o(n-1) = o(n) and SC = o(1)