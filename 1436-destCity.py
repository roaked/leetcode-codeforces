"""You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi.
 Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city."""

class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        destination, begin = None, []
        for sublist in paths:
            begin.append(sublist[0])
        # print(begin)
        for sublist in paths:
            # print(sublist[1])
            if sublist[1] in begin:
                continue
            else: 
                destination = sublist[1]
        return destination
    

print(Solution().destCity(paths=[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])) # destination

print(Solution().destCity(paths = [["B","C"],["D","B"],["C","A"]]))

print(Solution().destCity(paths = [["A","Z"]]))