#Sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False 
        return sorted(s) == sorted(t)

# Tc = 0(nlogn + mlogm)
# SC  = o(1) or o(n+m)

#Hash Map 
class Solution:
    def isAnaagram(self,s:str,t:str) -> bool:
        if len(s) != len(t):
            return False 
        
        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 +countT.get(t[i],0)
        return countS == countT

''' Tc = o(n+m) and SC = 0(1) where n is the length of string  s and m is the length of string t'''

