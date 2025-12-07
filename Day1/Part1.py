start = 50
count = 0
with open("input.txt", "r") as f:
    for line in f:
        rotation, amount = line[0], int(line[1:])
        amount = amount if rotation == 'R' else -amount
        start+= amount

        while start > 99:
            start = start - 100
        while start < 0:
            start = 100 + start

        if start == 0:
            count += 1
print(count)
