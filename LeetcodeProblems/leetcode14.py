#Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        prefix = strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(prefix)!=0:
                prefix = prefix[0:len(prefix)-1]
                if prefix == "":
                    return ""
        return prefix
print(longestCommonPrefix((strs = ["flower", "flow", "flight"])))
''' TC = o(s)  s is the sum of all charactes in all strings and sc = o(1)'''