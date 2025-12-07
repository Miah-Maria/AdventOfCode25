start = 50
count = 0
with open("input.txt", "r") as f:
    for line in f:
        rotation, amount = line[0], int(line[1:])
        step = 1 if rotation == 'R' else -1

        for x in range(amount):
            start += step

            if start > 99:
                start = 0
            elif start < 0:
                start = 99

            if start == 0:
                count += 1

        print(str(count) + ": " + str(start))
