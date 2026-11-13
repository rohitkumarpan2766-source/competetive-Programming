def count_reachable_leaves(n, edges, is_dark, m):
   
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, parent, dark_count):
        
        if is_dark[node - 1]: 
            dark_count += 1
        else:
            dark_count = 0

       
        if dark_count > m:
            return 0

        is_leaf = True
        total_leaves = 0

        
        for neighbor in graph[node]:
            if neighbor != parent:
                is_leaf = False
                total_leaves += dfs(neighbor, node, dark_count)

        if is_leaf:
            return 1
            
        return total_leaves
    return dfs(1, 0, 0)