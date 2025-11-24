class Solution:
    def bfs(self,node,isConnected,vis):
        q=deque([node])
        while q:
            x=q.popleft()
            for nei in range(len(isConnected)):
                if isConnected[x][nei]==1 and nei not in vis:
                    vis.add(nei)
                    q.append(nei)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        p=0
        vis=set()
        n=len(isConnected)
        for start in range(n):
            if start not in vis:
                p+=1
                vis.add(start)
                self.bfs(start,isConnected,vis)
                
        
        return p


        
