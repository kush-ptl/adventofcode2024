# part 1

input = "input.txt"

left_list = []
right_list = []

with open(input, 'r') as file:
    for line in file:
        if line.strip():
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)

left_list.sort()
right_list.sort()

total_dist = 0
for i in range(len(left_list)):
    dist = abs(left_list[i] - right_list[i])
    total_dist += dist

print(f"Total distance: {total_dist}")

# part 2

from collections import Counter

right_counts = Counter(right_list)

total_score = 0
for num in left_list:
    score = num * right_counts.get(num, 0)
    total_score += score

print (f"Total score: {total_score}")
