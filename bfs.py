from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
                
def bfsModified(graph_fst, start_fst, graph_snd, start_snd):
    alignment_cost = 0
    visited_fst = set()
    queue_fst = deque([start_fst])
    visited_fst.add(start_fst)
    
    visited_snd = set()
    queue_snd = deque([start_snd])
    visited_snd.add(start_snd)

    while queue_fst or queue_snd:
        if len(queue_fst) == 0:
            alignment_cost += len(queue_snd)
            break
        if len(queue_snd) == 0:
            alignment_cost += len(queue_fst)
            break
            
        current_node_fst = queue_fst.popleft()
        
        current_node_snd = queue_snd.popleft()
        
        if current_node_fst != current_node_snd:
            alignment_cost += 1
            print("------------ \nFirst graph: " + current_node_fst + "\nSecond graph: " + current_node_snd)

        for neighbor_fst in graph_fst[current_node_fst]:
            if neighbor_fst not in visited_fst:
                queue_fst.append(neighbor_fst)
                visited_fst.add(neighbor_fst)
        
        for neighbor_snd in graph_snd[current_node_snd]:
            if neighbor_snd not in visited_snd:
                queue_snd.append(neighbor_snd)
                visited_snd.add(neighbor_snd)
        
    print("------------ \nAligment cost: ", alignment_cost)


if __name__ == "__main__":
    #adjacency list
    graph_fst = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C'],
        'G': ['C']
    }
    
    graph_snd = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'M'],
        'C': ['A', 'F', 'H'],
        'D': ['B'],
        'M': ['B'],
        'F': ['C'],
        'H': ['C']
    }

    bfsModified(graph_fst, 'A', graph_snd, 'A')


G = nx.DiGraph(graph_fst)

# Draw the graph using networkx and matplotlib
''' pos = nx.spring_layout(G, seed=42) 
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
plt.show() '''
