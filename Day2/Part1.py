ranges = []
running_sum = 0

with open("Day2/input.txt", "r") as f:
    line = f.readline().strip()
    ranges.append(line.split(','))

for x in ranges[0]:


    inner = x.split('-')
    low, high = int(inner[0]), int(inner[1])

    for number in range(low, high + 1):
        strNumber = str(number)
        mid = len(strNumber)//2 + len(strNumber)%2
        split1 = strNumber[:mid]
        split2 = strNumber[mid:]
        if split1 == split2:

            running_sum += number

print(running_sum)