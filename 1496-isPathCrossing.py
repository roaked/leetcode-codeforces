"""Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. 
You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited.
 Return false otherwise."""

class Solution:
    def isPathCrossing(self, path: str) -> bool:

        visited = {(0, 0): True}
        xc, yc = 0, 0
        for direction in path:
            if direction == 'N':
                yc += 1
            elif direction == 'E':
                xc += 1
            elif direction == 'S':
                yc -= 1
            elif direction == 'W':
                xc -= 1

            if (xc, yc) in visited:
                return True

            visited[(xc, yc)] = True

        return False
    
print(Solution().isPathCrossing(path = "NES"))

print('\n')
print(Solution().isPathCrossing(path = "NESWW"))