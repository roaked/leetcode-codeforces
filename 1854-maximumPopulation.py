"""You are given a 2D integer array logs where each logs[i] = [birth_i, death_i] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year.
The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1].
Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population."""

class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        MIN_YEAR = 1950
        MAX_YEAR = 2051 
        max_population = 0
        max_population_year = None

        for year in range(MIN_YEAR, MAX_YEAR + 1):
            population = 0
            for birth, death in logs:
                if birth <= year <= death - 1:
                    population += 1
            if population > max_population:
                max_population = population
                max_population_year = year
    
        return max_population_year
        
logs = [[1993,1999],[2000,2010]]
print(Solution().maximumPopulation(logs))
print("\n")

logs = [[1950,1961],[1960,1971],[1970,1981]]
print(Solution().maximumPopulation(logs))


