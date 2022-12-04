import string


def get_priority_score(letter: string):
    if letter.isupper():
        return string.ascii_uppercase.index(letter) + 27
    else:
        return string.ascii_lowercase.index(letter) + 1


def solve():
    input_file = open('input', 'r')

    total = 0

    for line in input_file:
        all_items = list(line)

        first = all_items[:len(all_items) // 2]
        second = all_items[len(all_items) // 2:]

        item_set = set()

        for item in first:
            item_set.add(item)

        for item in second:
            if item in item_set:
                total += get_priority_score(item)
                break

    input_file.close()

    print(total)


if __name__ == "__main__":
    solve()
