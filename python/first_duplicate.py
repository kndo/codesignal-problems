#!/usr/bin/env python

def first_duplicate(a):
    """"O(n) time, O(n) space."""
    s = set()

    for v in a:
        if v in s:
            return v
        else:
            s.add(v)

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
