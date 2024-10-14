# Step 1: Import necessary libraries
import networkx as nx

# Step 2: Create a directed graph representing the web pages and links
G = nx.DiGraph()

# Step 3: Add edges (links between pages)
# Example: A -> B means there is a link from page A to page B
G.add_edges_from([('A', 'B'), ('A', 'C'),
                  ('B', 'C'), ('C', 'A'),
                  ('C', 'D'), ('D', 'C')])

# Step 4: Compute PageRank
pagerank = nx.pagerank(G, alpha=0.85)

# Step 5: Display the PageRank values for each node
print("PageRank Values:")
for node, value in pagerank.items():
    print(f"{node}: {value:.4f}")
