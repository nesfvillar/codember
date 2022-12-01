from input import INPUT


def get_next_index(length, i):
    if length > i + 1:
        return i + 1
    elif length == i:
        return 1
    else:
        return 0


def main():
    user_indexes = [i for i in range(len(INPUT))]

    i = 0
    while len(user_indexes) > 1:
        next_index = get_next_index(len(user_indexes), i)
        user_indexes.pop(next_index)
        i = next_index

    index = user_indexes[0]
    survivor = INPUT[index]
    print(f'{survivor}-{index}')


if __name__ == '__main__':
    main()
