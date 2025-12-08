ranges = []
running_sum = 0

def is_invalid_id(num: int) -> bool:
    s = str(num)
    L = len(s)

    for block_size in range(1, L//2 + 1):
        if L % block_size != 0:
            continue

        block = s[:block_size]
        repeats = L // block_size

        if block * repeats == s and repeats >= 2:
            return True

    return False


with open("Day2/input.txt", "r") as f:
    line = f.readline().strip()
    ranges = line.split(',')

for x in ranges:
    low, high = map(int, x.split('-'))

    for number in range(low, high + 1):
        if is_invalid_id(number):
            running_sum += number

print(running_sum)
