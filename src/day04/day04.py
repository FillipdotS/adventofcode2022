def solve():
    input_file = open('input', 'r')

    total = 0

    for line in input_file:
        # Split the line by commas
        line = line.split(',')

        # Take the first element of line and split it by dashes and convert every element to an int
        first_elf = [int(x) for x in line[0].split('-')]
        second_elf = [int(x) for x in line[1].split('-')]

        # Check if the elves range overlap at all
        if first_elf[0] <= second_elf[0] <= first_elf[1] or second_elf[0] <= first_elf[0] <= second_elf[1]:
            total += 1

    input_file.close()

    print(total)


if __name__ == "__main__":
    solve()
