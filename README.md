# AI2022-2

## Code

### Sudoku

constraints
```python
def constraint_check_row(grid: list, row: int, col: int, new_val: int) -> bool:
    return new_val not in grid[row*9:row*9+9]


def constraint_check_col(grid: list, row: int, col: int, new_val: int) -> bool:
    for i in range(9):
        if new_val == grid[i*9+col]:
            return False
    return True


def constraint_check_box(grid: list, row: int, col: int, new_val: int) -> bool:
    row = row // 3 * 3
    col = col // 3 * 3

    for i in range(3):
        for j in range(3):
            if new_val == grid[(row+i)*9+col+j]:
                return False
    return True
```

### Nonogram

constraints
```python
def constraint_check_row(grid: list, row: int, col: int, row_cond: list, col_cond: list) -> bool:
    cpy = grid[row][:]
    neighbor = calc_neighbor(cpy)

    # 한 row의 입력이 끝났을때 주어진 입력과 동일한지 검증
    if len(cpy)-1 == col:
        if neighbor != row_cond[row]:
            return False

    # 입력의 이웃은 주어진 이웃보다 많아질 수 없음
    if len(neighbor) > len(row_cond[row]):
        return False

    # 입력의 인접 이웃은 주어진 인접 이웃보다 많아 질 수 없음
    for c, n in zip(row_cond[row], neighbor):
        if c < n:
            return False
    return True


def constraint_check_col(grid: list, row: int, col: int, row_cond: list, col_cond: list) -> bool:
    cpy = [grid[x][col] for x in range(len(grid))]
    neighbor = calc_neighbor(cpy)

    # 입력의 이웃은 주어진 이웃보다 많아질 수 없음
    if len(neighbor) > len(col_cond[col]):
        return False

    # 입력의 인접 이웃은 주어진 인접 이웃보다 많아 질 수 없음
    for c, n in zip(col_cond[col], neighbor):
        if c < n:
            return False
    return True
```

## Results

### Sudoku
```
python3 sudoku.py

0 4 0 0 0 0 0 0 0
0 0 1 0 3 4 6 2 0
6 0 3 0 0 0 0 7 0
0 0 0 4 8 3 5 0 7
0 0 0 0 5 0 0 6 0
0 0 0 0 0 9 0 4 0
0 0 5 0 0 0 0 0 1
8 0 0 5 4 7 3 9 6
0 0 0 0 2 1 0 0 0
2 4 8 6 7 5 1 3 9 
7 5 1 9 3 4 6 2 8 
6 9 3 2 1 8 4 7 5 
9 2 6 4 8 3 5 1 7 
1 8 4 7 5 2 9 6 3 
5 3 7 1 6 9 8 4 2 
4 7 5 3 9 6 2 8 1 
8 1 2 5 4 7 3 9 6 
3 6 9 8 2 1 7 5 4 
```

### Nonogram
```
python3 nonogram.py

10 10
1 1 
2 2 
5 
1 1 1 
7
5 2 
3 1 
3 1 
4 2 
7 
1 
6 
2 6 
8 
2 6 
6 2 
1 1 
1 
1 2 
4
 *   *    
 ** **    
 *****    
 * * *    
*******   
 *****  **
  ***    *
  ***    *
  ****  **
  ******* 
```
