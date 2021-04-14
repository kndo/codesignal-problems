#!/usr/bin/env python

def first_not_repeating_character(s):
    """O(2n) time, O(n) space."""

    d = {}
    for v in s:
        d[v] = d.get(v, 0) + 1

    for v in s:
        if d[v] == 1:
            return v

    return '_'


def main():
    assert first_not_repeating_character('abacabad') == 'c'
    assert first_not_repeating_character('abacabaabacaba') == '_'


if __name__ == '__main__':
    main()
