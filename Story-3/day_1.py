from aoc import *

"""
These are edited minorly afterwards to put into different functions
since each part is a different input and it errors
theres a better way to do this by organising it better but while actually solving
code is all over the place and commented out and its not worth organising it
"""

def part_1(data):
    total = 0
    for line in data.splitlines():
        left, middle, right = line.split()
        num, left = left.split(':')
        num = int(num)
        binaryL = [0 if c.islower() else 1 for c in left]
        binaryM = [0 if c.islower() else 1 for c in middle]
        binaryR = [0 if c.islower() else 1 for c in right]
        numL = sum(b * (2 ** i) for i, b in enumerate(reversed(binaryL)))
        numM = sum(b * (2 ** i) for i, b in enumerate(reversed(binaryM)))
        numR = sum(b * (2 ** i) for i, b in enumerate(reversed(binaryR)))
        if numM > numL and numM > numR:
            total += num

    print(total)


def part_2(data):
    total = 0
    cs = []
    for line in data.splitlines():
        left, middle, right, rightright = line.split()
        num, left = left.split(':')
        num = int(num)
        binaryL = [0 if c.islower() else 1 for c in left]
        binaryM = [0 if c.islower() else 1 for c in middle]
        binaryR = [0 if c.islower() else 1 for c in right]
        binaryRR = [0 if c.islower() else 1 for c in rightright]
        numL = sum(b * (2 ** i) for i, b in enumerate(reversed(binaryL)))
        numM = sum(b * (2 ** i) for i, b in enumerate(reversed(binaryM)))
        numR = sum(b * (2 ** i) for i, b in enumerate(reversed(binaryR)))
        numRR = sum(b * (2 ** i) for i, b in enumerate(reversed(binaryRR)))
        cs.append((num, numL, numM, numR, numRR))

    maxrr = max(c[4] for c in cs)
    cs = [c for c in cs if c[4] == maxrr]
    print(min(cs, key=lambda c: c[1]+c[2]+c[3])[0])


def part_3(data):
    groups = {
        (0, 0): [],
        (0, 1): [],
        (1, 0): [],
        (1, 1): [],
        (2, 0): [],
        (2, 1): []
    }

    for line in data.splitlines():
        left, middle, right, rightright = line.split()
        num, left = left.split(':')
        num = int(num)
        binaryL = [0 if c.islower() else 1 for c in left]
        binaryM = [0 if c.islower() else 1 for c in middle]
        binaryR = [0 if c.islower() else 1 for c in right]
        binaryRR = [0 if c.islower() else 1 for c in rightright]
        numL = sum(b * (2 ** i) for i, b in enumerate(reversed(binaryL)))
        numM = sum(b * (2 ** i) for i, b in enumerate(reversed(binaryM)))
        numR = sum(b * (2 ** i) for i, b in enumerate(reversed(binaryR)))
        numRR = sum(b * (2 ** i) for i, b in enumerate(reversed(binaryRR)))
        if 30 < numRR < 33:
            continue
        max_num = max(numL, numM, numR)
        if numL == numM and numL == max_num or numM == numR and numM == max_num or numL == numR and numL == max_num:
            continue
        groups[max(0, 1, 2, key=lambda i: [numL, numM, numR][i]), numRR < 31].append(num)

    key = max(groups, key=lambda k: len(groups[k]))
    print(sum(groups[key]))


if __name__ == "__main__":
    data = import_input(1)