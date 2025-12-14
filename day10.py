import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

from util import next_line

N = 189


def parse(cmds):
    res = []
    for cmd in cmds:
        parsed = map(int, cmd[1:-1].split(','))
        res.append(list(parsed))
    return res


def minpresses(cmds, target):
    ndim = len(target)
    ncmd = len(cmds)

    mat = np.zeros((ndim, ncmd))
    for j, cmd in enumerate(cmds):
        for pos in cmd:
            mat[pos][j] = 1

    c = np.ones(ncmd)
    b = np.array(target)
    cons = LinearConstraint(mat, b, b)
    bnds = Bounds(0, np.inf)
    integ = np.ones(ncmd)

    res = milp(c, constraints=cons, bounds=bnds, integrality=integ)
    return int(round(res.fun))


def solve():
    total = 0
    for _ in range(N):
        line = next_line().split(' ')
        cmds = parse(line[1:-1])
        jolts = list(map(int, line[-1][1:-1].split(',')))
        total += minpresses(cmds, jolts)
    print(total)


solve()
