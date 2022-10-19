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


def next_number(grid: list, idx: int) -> int:
    if grid[idx] != 0:
        return next_number(grid, idx+1)
    else:
        return idx


class Solver:
    def __init__(self, variable, domain, constraints) -> None:
        self.variable = variable
        self.domain = domain
        self.constraints = constraints

    def check_constraint(self, *args, **kwargs):
        result = True
        for constraint in self.constraints:
            result &= constraint(*args, **kwargs)
        return result

    def solve(self, idx=0):
        if idx == len(self.variable):
            return True

        idx = next_number(self.variable, idx)

        for v in self.domain:
            if self.check_constraint(self.variable, idx // 9, idx % 9, v):
                self.variable[idx] = v
                if self.solve(idx + 1):
                    return True
                self.variable[idx] = 0
        return False

    def get_result(self):
        return self.variable

if __name__ == '__main__':
    variable = []
    domain = list(range(1, 10))
    constraints = [constraint_check_row, constraint_check_col, constraint_check_box]

    for _ in range(9):
        variable += list(map(int, input().split()))

    solver = Solver(variable, domain, constraints)
    solver.solve()

    result = solver.get_result()

    for i in range(9):
        for j in range(9):
            print(result[i*9+j], end=' ')
        print()
