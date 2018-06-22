def main():
    grid = [['s','f','f','f',]
            ['f','h','f','h',],
            ['f','f','f','h',]
            ['h','f','f','g',]]
    for c in grid:
        row = ""
        for r in c:
            row += r
            print(row)

main()