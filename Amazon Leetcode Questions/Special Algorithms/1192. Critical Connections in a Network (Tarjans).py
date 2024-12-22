class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Find all critical connections (bridges) in the network using Tarjan's Algorithm.

        Args:
            n (int): Number of nodes in the graph.
            connections (List[List[int]]): List of edges in the graph.

        Returns:
            List[List[int]]: List of critical connections (bridges).
        """
        # Initialize adjacency list for the graph
        adjList = {i: [] for i in range(n)}
        for u, v in connections:
            adjList[u].append(v)
            adjList[v].append(u)
        
        # Initialize variables for Tarjan's Algorithm
        discovery = [-1] * n  # Discovery times of nodes
        low = [-1] * n        # Lowest discovery time reachable
        time = [0]            # Timer for discovery times
        res = []              # List to store critical connections (bridges)
        
        # Helper function for DFS
        def dfs(node, parent):
            # Set discovery and low-link value for the current node
            discovery[node] = low[node] = time[0]
            time[0] += 1
            
            # Explore all neighbors of the current node
            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue  # Skip the parent node
                
                if discovery[neighbor] == -1:  # If the neighbor is unvisited
                    dfs(neighbor, node)  # Recurse on the neighbor
                    
                    # Update low-link value of the current node
                    low[node] = min(low[node], low[neighbor])
                    
                    # If the lowest reachable discovery time from neighbor is greater,
                    # the edge is a critical connection (bridge)
                    if low[neighbor] > discovery[node]:
                        res.append([node, neighbor])
                else:
                    # Update low-link value using back edge
                    low[node] = min(low[node], discovery[neighbor])
        
        # Start DFS from the first node
        dfs(0, -1)
        
        return res
        
# import copy

# class Solution:
#     def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
#         removedAlr = set()
#         uniqueNode = set()
#         adjList = {}
#         res = []
        
#         for edge in connections:
#             serverai = edge[0]
#             serverbi = edge[1]
            
#             if serverai not in adjList:
#                 adjList[serverai] = []
#                 uniqueNode.add(serverai)
#                 adjList[serverai].append(serverbi)
#             else:
#                 adjList[serverai].append(serverbi)
            
#             if serverbi not in adjList:
#                 uniqueNode.add(serverbi)
#                 adjList[serverbi] = []
#                 adjList[serverbi].append(serverai)
#             else:
#                 adjList[serverbi].append(serverai)
        
#         nodes = uniqueNode
#         for node in uniqueNode:
#             # print(f"We are currently at Node {node}")
#             # print(f"this node has edges too {adjList[node]}")
#             for neighbour in adjList[node]:
#                 if (node,neighbour) not in removedAlr and (neighbour,node) not in removedAlr:
#                     # print(f"We are considering {neighbour}")
#                     # print(f"Lets try removing the edge between {node} and {neighbour} and see if we can still traverse the graph")
#                     modifiedGraph = copy.deepcopy(adjList)
#                     # print(f"Here is the Original Graph: {adjList}")
#                     modifiedGraph[node].remove(neighbour)
#                     modifiedGraph[neighbour].remove(node)
#                     # print(f"Here is the modified Graph: {modifiedGraph} lets run a DFS from this node")
#                     seen = set()
#                     if self.dfs(node, modifiedGraph, seen, []) != len(uniqueNode):
#                         res.append([node, neighbour])
#                     else:
#                         print(f"The edge between {node} and {neighbour} not critical!")
#                 removedAlr.add((node,neighbour))
#                 removedAlr.add((neighbour,node))

#         return res
        
#     def dfs(self, node, graph, seen, arr):
#         # print(f"Starting DFS from node {node} on graph: {graph}")
#         stack = [node]

#         while stack:
#             currNode = stack.pop()
#             if currNode in seen:
#                 # print(f"We've been to node {node} before, continuing")
#                 continue
#             else:
#                 for neighbour in graph[currNode]:
#                     # print(f"Adding Neighbout to stack: {neighbour}")
#                     stack.append(neighbour)
#                 seen.add(currNode)

#         return len(seen)