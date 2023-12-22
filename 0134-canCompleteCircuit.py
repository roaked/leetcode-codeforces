"""There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction,
 otherwise return -1. If there exists a solution, it is guaranteed to be unique"""

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        
        total_gas = 0
        total_cost = 0
        for idx in range(len(gas)):
            total_gas += gas[idx]
            total_cost += cost[idx]
                
        if total_gas < total_cost:
            return -1
            
        station, fuel = 0, 0 #station 0
        for idx in range(len(gas)):
            fuel += gas[idx] - cost[idx] #condition for moving on
            if fuel < 0: 
                fuel, station = 0, idx+1
        return station
    
print(Solution().canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
print('\n')
print(Solution().canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]))
