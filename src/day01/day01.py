def solve():
    elves = []

    input_file = open('input', 'r')

    new_elf = []
    for line in input_file:
        if line == '\n':
            elves.append(sum(new_elf))

            new_elf = []
        else:
            new_elf.append(int(line))

    input_file.close()

    elves.sort()
    elves.reverse()

    print(sum(elves[:3]))


if __name__ == "__main__":
    solve()
