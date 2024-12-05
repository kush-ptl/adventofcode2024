# part 1

input = "input.txt"

rules = []
updates = []

with open(input, 'r') as file:
    for line in file:
        if line.strip():
            if '|' in line:
                before, after = map(int, line.split('|'))
                rules.append((before, after))
            if ',' in line:
                pages = list(map(int, line.split(',')))
                updates.append(pages)

def is_valid_order(pages, rules):
    for before, after in rules:
        if before in pages and after in pages:
            before_idx = pages.index(before)
            after_idx = pages.index(after)
            if before_idx > after_idx:
                return False
    return True

middle_sum = 0
for update in updates:
    if is_valid_order(update, rules):
        middle = update[len(update) // 2]
        middle_sum += middle

print(f"Valid middle numbers: {middle_sum}")

# part 2

def fix_order(pages, rules):
    result = pages.copy()
    while not is_valid_order(result, rules):
        for i in range(len(result)-1):
            for before, after in rules:
                if result[i] == after and result[i+1] == before:
                    result[i], result[i+1] = result[i+1], result[i]
    return result

middle_sum = 0
for update in updates:
    if not is_valid_order(update, rules):
        correct_order = fix_order(update, rules)
        middle = correct_order[len(update) // 2]
        middle_sum += middle

print(f"Invalid middle numbers (after corrections): {middle_sum}")