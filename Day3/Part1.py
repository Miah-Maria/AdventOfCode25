total = 0
with open("Day3/input.txt", "r") as f:
    for line in f:
        for digit in range(9,0,-1):
            if str(digit) in line:
                sliced = line[line.index(str(digit))+1::]
                if len(sliced) == 1:
                    continue
                total += int(str(digit)+max(sliced))
                break
print(total)