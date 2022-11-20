# "109 105 100 117" -> midu
# "99 111 100 101 109 98 101 114" -> codember
# "99 111 100 101 109 98 101 114 - 109 105 100 117" -> codember midu
# "112 108 97 121 - 116 101 116 114 105 115" -> play tetris

def main():
    with open('input.txt', 'r') as f:
        words_encrypted = f.read().split()
    print(words_encrypted)


if __name__ == '__main__':
    main()