class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
                if not grid:
        return 0

    # Get dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    visited = set()

    # Helper function to perform DFS
    def dfs(r, c):
        # Boundary checks and water or visited check
        if (r < 0 or c < 0 or r >= rows or c >= cols or 
            grid[r][c] == 'W' or (r, c) in visited):
            return
        # Mark the current cell as visited
        visited.add((r, c))
        # Explore all four directions (up, down, left, right)
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Initialize island count
    island_count = 0
    # Iterate through every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # Start a DFS if we find an unvisited land cell
            if grid[r][c] == 'L' and (r, c) not in visited:
                dfs(r, c)
                island_count += 1

    return island_count

# Example usage:
grid1 = [
    ['L', 'L', 'L', 'L', 'W'],
    ['L', 'L', 'W', 'L', 'W'],
    ['L', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W']
]

grid2 = [
    ['L', 'L', 'W', 'W', 'L'],
    ['L', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'L']
]

# To test the function:
obj = type('', (), {})()  # Creating an anonymous object to call the method
obj.getTotalIsles = getTotalIsles

print(obj.getTotalIsles(grid1))  # Output: 1
print(obj.getTotalIsles(grid2))  # Output: 3    
        return 0
