import re

FIELDS = {'usr', 'eme', 'psw', 'age', 'loc', 'fll'}


def main():
    with open('input.txt', 'r') as f:
        reader = f.read()
        users_raw = [re.split('[\n ]', user) for user in reader.split('\n\n') if user]

    count = 0
    last_usr = last_usr_tmp = ''
    for user in users_raw:
        user_contains = set()
        for pair_raw in user:
            key, _, val = pair_raw.partition(':')
            user_contains.add(key)
            if key == 'usr':
                last_usr_tmp = val
        if not FIELDS.difference(user_contains):
            count += 1
            last_usr = last_usr_tmp
    print(f"{count}{last_usr}")


if __name__ == '__main__':
    main()
