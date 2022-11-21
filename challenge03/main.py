from input import INPUT


def main():
    i = 1
    max_count = count = 1 if INPUT[0] == INPUT[1] else 2
    color_end = INPUT[0]
    while i < len(INPUT) - 1:
        last_color, current_color, next_color = INPUT[i - 1], INPUT[i], INPUT[i + 1]
        if current_color != next_color:
            if last_color == next_color:
                count += 1
            else:
                count = 2
        else:
            count = 1
        if count >= max_count:
            max_count = count
            color_end = next_color
        i += 1
    print(f'{max_count}@{color_end}')


if __name__ == '__main__':
    main()
