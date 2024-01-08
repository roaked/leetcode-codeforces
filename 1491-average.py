"""You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted."""

from typing import List
class Solution:
    def average(self, salary: List[int]) -> float:
        ans = 0
        for i in range(len(salary)):
            if salary[i] == max(salary) or salary[i] == min(salary):
                continue
            else:
                ans += salary[i]
        return (ans / (len(salary)-2))




print(Solution().average(salary = [4000,3000,1000,2000]))