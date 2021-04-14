#!/usr/bin/env python

def first_duplicate(a):
    size = len(a)

    for i in range(size):
        for j in range(i+1, size):
            if a[j] == a[i]:
                try:
                    if j < min_index:
                        min_index = j
                except NameError:
                    min_index = j

    try:
        return a[min_index]
    except NameError:
        return -1


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
