# part 1

input = "input.txt"
grid = []

with open(input, 'r') as file:
    for line in file:
        if line.strip():
            grid.append(list(line.strip()))

rows = len(grid)
cols = len(grid[0])
word = 'XMAS'
count = 0

for r in range(rows):
    for c in range(cols):
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]

        for dr, dc in directions:
            if (
                0 <= r + 3*dr < rows and
                0 <= c + 3*dc < cols
            ):
                if all(
                    grid[r + i*dr][c + i*dc] == word[i]
                    for i in range(4)
                ):
                    count += 1

print(f"XMAS count: {count}")

# part 2

count = 0

for r in range(1, rows-1):
    for c in range(1, cols-1):
        diag1 = grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1]
        diag2 = grid[r-1][c+1] + grid[r][c] + grid[r+1][c-1]

        valid_mas = {'MAS', 'SAM'}
        if diag1 in valid_mas and diag2 in valid_mas:
            count += 1

print(f"X-MAS count: {count}")
