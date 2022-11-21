# "109 105 100 117" -> midu
# "99 111 100 101 109 98 101 114" -> codember
# "99 111 100 101 109 98 101 114 - 109 105 100 117" -> codember midu
# "112 108 97 121 - 116 101 116 114 105 115" -> play tetris

def main():
    with open('input.txt', 'r') as f:
        words_encrypted = f.read().split()

    result = ""
    for word in words_encrypted:
        letters = []
        i, j = 0, 1
        while j <= len(word):
            cur_val = chr(int(word[i:j]))
            if cur_val.isalnum():
                letters.append(cur_val)
                i, j = j, j + 1
            else:
                j += 1
        result = result + ' ' + ''.join(letters)
    print(result)


if __name__ == '__main__':
    main()