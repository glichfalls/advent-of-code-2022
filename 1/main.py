with open('input.txt') as f:
    data = f.read()
    highestTotal = 0
    currentTotal = 0
    for line in data.splitlines():
        if line != '':
            currentTotal += int(line)
        else:
            if currentTotal > highestTotal:
                highestTotal = currentTotal
            currentTotal = 0
    print(highestTotal)
