class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:


        res = []
        
        for i in trust:
            res.append(i[1])
            del i[1]
            
        for i in range(1, n+1):
            if [i] not in trust and res.count(i) == n-1:
                return i
            
        return -1


# ===============


