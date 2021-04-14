#!/usr/bin/env python

def first_duplicate(a):
    size = len(a)

    # No duplicates
    if len(set(a)) == size:
        return -1

    # There is at least one duplicate. Its largest index is the last index.
    sec_occur_index = size - 1

    for i in range(size):
        if i == sec_occur_index - 1:
            break
        for j in range(i+1, size):
            if a[j] == a[i]:
                if j < sec_occur_index:
                    sec_occur_index = j


    return a[sec_occur_index]


def main():
    a = [2, 1, 3, 5, 3, 2]
    assert first_duplicate(a) ==  3

    a = [2, 2]
    assert first_duplicate(a) == 2

    a = [2, 4, 3, 5, 1]
    assert first_duplicate(a) == -1

    print('All tests passed!')


if __name__ == '__main__':
    main()
