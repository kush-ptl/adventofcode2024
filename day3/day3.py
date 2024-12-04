# part 1

import re

input = "input.txt"
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

total = 0

with open(input, 'r') as file:
    content = file.read()
    matches = re.finditer(pattern, content)

    for match in matches:
        x, y = map(int, match.groups())
        total += x * y

print(f"Sum of muls: {total}")

# part 2

enabled = True
total = 0

with open(input, 'r') as file:
    content = file.read()

    i = 0
    while i < len(content):
        if content[i:i+4] == 'do()':
            enabled = True
            i += 4
            continue

        if content[i:i+7] == "don't()":
            enabled = False
            i += 7
            continue

        if content[i:i+3] == 'mul':
            match = re.match(pattern, content[i:])
            if match and enabled:
                x, y = map(int, match.groups())
                total += x * y
                i += len(match.group(0))
                continue
        
        i += 1

print(f"Sum of do muls: {total}")