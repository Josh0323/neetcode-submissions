class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for src, dest in tickets:
            adj[src].append(dest)
        
        result = ["JFK"]
        def dfs(src):
            if len(result) == len(tickets) + 1:
                return True
            
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, n in enumerate(temp):
                adj[src].pop(i)
                result.append(n)

                if dfs(n):
                    return True
                adj[src].insert(i, n)
                result.pop()
            
            return False
        
        dfs("JFK")
        return result