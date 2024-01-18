"""Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally."""

class Solution:
    def divisorGame(self, n: int, cnt: int) -> bool:
        dp = []
        cnt == max(0, cnt)
        x = None
        for i in range(0, n):
            if n == 0 or n == 1:
                return True if cnt % 2 == 0 else False
            if n % i:
                x = i
                cnt += 1
            else:
                break
            self.divisorGame(n-x, cnt)
    
n, cnt = 3, 0

print(Solution().divisorGame(n, cnt))
# print(Solution().divisorGame(n = 3))