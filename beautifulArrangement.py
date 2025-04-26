from typing import Set


class Solution:
    def countArrangement(self, n: int) -> int:
        visited: Set[int] = set()
        count = 0

        # Backtracking function to try placing numbers at position i
        def backtrack(i):
            nonlocal count
            # If all positions are filled, it's a valid arrangement
            if i > n:
                count += 1
                return

            # Try placing each number from 1 to n at index i
            for num in range(1, n + 1):
                if num not in visited and (num % i == 0 or i % num == 0):
                    visited.add(num)  # Choose the number
                    backtrack(i + 1)  # Recurse for next position
                    visited.remove(num)  # Backtrack

        backtrack(1)
        return count


if __name__ == "__main__":
    sol = Solution()
    n = 2
    print("Number of beautiful arrangements:", sol.countArrangement(n))
