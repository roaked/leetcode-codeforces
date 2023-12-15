
def printTree(root):
    def printNodes(nodes):
        return [node.val if node else None for node in nodes]

    if not root:
        print("Empty tree")
        return
    
    queue = [root]
    
    while queue:
        level_vals = printNodes(queue)
        print(level_vals)
        next_level = []
        
        for node in queue:
            if node:
                next_level.append(node.left)
                next_level.append(node.right)
        
        queue = next_level