def rectangles(strings):
    count = 0
    for y in range(len(strings)):
        for x in range(len(strings[y])):
            if strings[y][x] == '+':
    for height in range(1, len(strings) - y):
        if strings[y + height][x] != '|':
            break
        for width in range(1, len(strings[y]) - x):
            if (strings[y][x + width] == '+' and
                strings[y + height][x + width] == '+' and
                all(strings[y][x + i] == '-' for i in range(1, width)) and
                all(strings[y + height][x + i] == '-' for i in range(1, width)) and
                all(strings[y + i][x] == '|' for i in range(1, height)) and
                all(strings[y + i][x + width] == '|' for i in range(1, height))):
                count += 1
            else:
                break
    return count