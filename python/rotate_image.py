#!/usr/bin/env python

def rotate_image(m):
    """O(n^2) time, O(1) space."""

    N = len(m)

    # Transpose matrix
    for i in range(N):
        for j in range(i+1, N):
            m[i][j], m[j][i] = m[j][i], m[i][j]

    # Flip matrix horizontally
    for i in range(N):
        for j in range(N//2):
            tmp = m[i][j]
            m[i][j] = m[i][N-1-j]
            m[i][N-1-j] = tmp

    return m


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert rotate_image(m) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    print('All tests passed!')


if __name__ == '__main__':
    main()
