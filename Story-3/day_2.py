from aoc import *

data = import_input(2)


def part_1(data):
    total = 0
    start = None
    end = None
    for r, row in enumerate(data.splitlines()):
        for c, ch in enumerate(row):
            if ch == '@':
                start = (r, c)
            elif ch == '#':
                end = (r, c)

    visited = set()
    dirs = [iup, iright, idown, ileft]
    s = 0
    cur = start
    while cur != end:
        visited.add(cur)
        d = dirs[s % 4]
        s += 1
        ncur = vector_add(cur, d)
        if ncur not in visited:
            cur = ncur
            total += 1


    print(total)


def part_2(data):
    total = 0
    start = None
    end = None
    for r, row in enumerate(data.splitlines()):
        for c, ch in enumerate(row):
            if ch == '@':
                start = (r, c)
            elif ch == '#':
                end = (r, c)


    visited = {start, end}
    dirs = [iup, iright, idown, ileft]
    s = 0
    cur = start

    while True:
        visited.add(cur)
        d = dirs[s % 4]
        s += 1
        ncur = vector_add(cur, d)
        if ncur not in visited:
            cur = ncur
            visited.add(cur)
            total += 1
            if trapped(visited, end):
                break

    print(total)


def flood(walls, start):
    seen = {start}
    q = collections.deque([start])
    maxc = max(c for r, c in walls)
    minc = min(c for r, c in walls)
    maxr = max(r for r, c in walls)
    minr = min(r for r, c in walls)
    while q:
        cur = q.popleft()
        for d in dirs4:
            ncur = vector_add(cur, d)
            nr, nc = ncur
            if ncur in seen or ncur in walls:
                continue
            if minc <= nc <= maxc and minr <= nr <= maxr:
                seen.add(ncur)
                q.append(ncur)
            if nc < minc or nc > maxc or nr < minr or nr > maxr:
                return set()
    return seen


def trapped(walls, start):
    sr, sc = start
    crossings = 0
    maxc = max(c for r, c in walls)
    minc = min(c for r, c in walls)
    flag = False
    for c in range(sc + 1, maxc + 2):
        if (sr, c) in walls != flag: 
            if flag:
                crossings += 1
            flag = (sr, c) in walls
    return crossings % 2 == 1


def render(end, visited):
    for r in range(-10, 67):
        for c in range(-10, 67):
            if (r, c) == end:
                print_("#", end="")
            elif (r, c) in visited:
                print_("+", end="")
            else:
                print_(" ", end="")
        print_()


if __name__ == "__main__":
    data = import_input(2)
