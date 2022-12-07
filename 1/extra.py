with open('input.txt') as f:
    data = f.read()
    totals = []
    currentTotal = 0
    for line in data.splitlines():
        if line != '':
            currentTotal += int(line)
        else:
            totals.append(currentTotal)
            currentTotal = 0
    totals.sort(reverse=True)
    print(totals[0] + totals[1] + totals[2])
