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


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        center = None
        
        for i in edges[0]:
            if center == None:
                for j in edges:
                    if i in j:
                        center = i
                    else:
                        center = None
                        break
            else:
                break
        
        return center

      # Alt solution:

      if edges[0][0] in edges[1]:
        return edges[0][0]
      return edges[0][1]


# ===============


