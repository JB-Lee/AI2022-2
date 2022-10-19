def calc_neighbor(array: list) -> list:
    '''
    인접 이웃 계산
    '''
    cnt = 0
    result = []
    for x in range(len(array)):
        if array[x]:
            cnt += 1
        elif cnt:
            result += [cnt]
            cnt = 0
    if cnt:
        result += [cnt]
    return result


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


class Solver:
    def __init__(self, variable, domain, constraints, row_cond, col_cond, size) -> None:
        self.variable = variable
        self.domain = domain
        self.constraints = constraints

        self.row_cond = row_cond
        self.col_cond = col_cond

        self.size = size

    def check_constraint(self, *args, **kwargs):
        result = True
        for constraint in self.constraints:
            result &= constraint(*args, **kwargs)
        return result

    def solve(self, idx=0):
        row = idx // self.size[0]
        col = idx % self.size[0]

        for v in self.domain:
            tmp = self.variable[row][col]
            self.variable[row][col] = v
            if self.check_constraint(self.variable, row, col, self.row_cond, self.col_cond):
                if idx == self.size[0]*self.size[1]-1 or self.solve(idx + 1):
                    return True
            self.variable[row][col] = tmp
        return False

    def get_result(self):
        return self.variable


if __name__ == '__main__':
    h, w = list(map(int, input().split()))

    variable = [[False for _ in range(w)] for _ in range(h)]
    domain = [True, False]
    constraints = [constraint_check_row, constraint_check_col]

    row_cond = [list(map(int, input().split())) for _ in range(h)]
    col_cond = [list(map(int, input().split())) for _ in range(w)]

    solver = Solver(variable, domain, constraints, row_cond, col_cond, (h, w))
    solver.solve()

    result = solver.get_result()

    for i in range(h):
        for j in range(w):
            print('*' if result[i][j] else ' ', end='')
        print()
