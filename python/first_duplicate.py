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
    assert first_duplicate([2, 1, 3, 5, 3, 2]) ==  3
    assert first_duplicate([2, 2]) == 2
    assert first_duplicate([2, 4, 3, 5, 1]) == -1

    print('All tests passed!')


if __name__ == '__main__':
    main()
