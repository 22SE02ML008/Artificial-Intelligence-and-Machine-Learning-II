class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child):
        self.children.append(child)
def dfs(node):
    print(node.value, end=' ')

    for child in node.children:
        dfs(child)

if __name__ == "__main__":
    root = TreeNode('A')
    node_b = TreeNode('B')
    node_c = TreeNode('C')
    node_d = TreeNode('D')
    node_e = TreeNode('E')
    node_f = TreeNode('F')

    root.add_child(node_b)
    root.add_child(node_c)
    node_b.add_child(node_d)
    node_b.add_child(node_e)
    node_c.add_child(node_f)

print("Depth-First Search (DFS) traversal of the tree is:")
dfs(root)