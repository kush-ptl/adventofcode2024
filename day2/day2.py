# part 1

input = "input.txt"

def is_safe_report(levels):
    is_increasing = levels[1] > levels[0]

    for i in range(len(levels)-1):
        diff = levels[i+1] - levels[i]

        if abs(diff) < 1 or abs(diff) > 3:
            return False
        
        if is_increasing and diff <= 0:
            return False
        if not is_increasing and diff >= 0:
            return False
    
    return True

safe_count = 0

with open(input, 'r') as file:
    for line in file:
        if line.strip():
            levels = [int(x) for x in line.strip().split()]
            if is_safe_report(levels):
                safe_count += 1

print(f"Safe reports: {safe_count}")

# part 2

def is_dampened_safe(levels):
    if is_safe_report(levels):
        return True
    
    for i in range(len(levels)):
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe_report(dampened_levels):
            return True
        
    return False

dampened_safe_count = 0

with open(input, 'r') as file:
    for line in file:
        if line.strip():
            levels = [int(x) for x in line.strip().split()]
            if is_dampened_safe(levels):
                dampened_safe_count += 1

print(f"Dampened safe reports: {dampened_safe_count}")