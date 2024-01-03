
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

def isValidSudoku(self, board: list[list[str]]) -> bool:

        def valid(arr):
            s=''.join(arr).replace('.','')
            return len(s) == len(set(s))
        
        def checkrow(): #C1
            for row in board:
                if not valid(row):
                    return False
            return True
        
        def checkcol(): #C2
            for col in zip(*board):
                if not valid(col):
                    return False
            return True
        
        def square(): #C3
            for r in range(0,9,3):
                for c in range(0,9,3):
                    nums=[board[r+i][c+j] for i in range(3) for j in range(3)]
                    if not valid(nums):
                        return False
            return True
        
        return checkrow() and checkcol() and square()