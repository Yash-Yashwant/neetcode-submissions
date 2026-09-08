class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDic = {}
        tDic = {}

        for i in s:
            if i in sDic:
                sDic[i]+=1 
            else:
                sDic[i] = 1

        for j in t:
            if j in tDic:
                tDic[j]+=1 
            else:
                tDic[j] = 1

        return sDic == tDic