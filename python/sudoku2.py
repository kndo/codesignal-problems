#!/usr/bin/env python

def sudoku2(grid):
    """O(n^2) time, O(1) space."""

    N = len(grid)

    seen = set()

    for i in range(N):
        for j in range(N):
            curr_val = grid[i][j]
            if curr_val != '.':
                if f'{curr_val} found in row {i}' in seen:
                    return False
                else:
                    seen.add(f'{curr_val} found in row {i}')

                if f'{curr_val} found in col {j}' in seen:
                    return False
                else:
                    seen.add(f'{curr_val} found in col {j}')

                if f'{curr_val} found in sub box ({i//3}, {j//3})' in seen:
                    return False
                else:
                    seen.add(f'{curr_val} found in sub box ({i//3}, {j//3})')

    return True


def main():
    grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
            ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
            ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
            ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
            ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
            ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
            ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
    assert sudoku2(grid) == True

    grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
            ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
            ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
            ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
            ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
            ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
            ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
            ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
    assert sudoku2(grid) == False

    print('All tests passed!')


if __name__ == '__main__':
    main()
