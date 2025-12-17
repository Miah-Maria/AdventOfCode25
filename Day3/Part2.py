
final = 0
def digit(input,count):
    for digit in range(9,0,-1):
        if str(digit) in input:
            sliced = input[input.index(str(digit))+1::]
            
            if len(sliced) >= 11-count:
                return digit,sliced
            
            


with open("Day3/input.txt", "r") as f:
    for line in f:
        input = line.strip()
        total = ""
        count = 0
        while count < 12:
            amount, input = digit(input,count)
            total = total + str(amount)
            count += 1
        print(total)
        final += int(total)
        

print(final)