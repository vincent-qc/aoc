from collections import defaultdict

from util import next_line

N = 643


def solve():
    edges = defaultdict(list)

    for _ in range(N):
        [src, dst] = next_line().split(': ')
        dsts = dst.split(' ')
        edges[src] = dsts

    memo = [[{}, {}], [{}, {}]]

    def dpget(node, dac, fft):
        curmemo = memo[dac][fft]
        if node in curmemo:
            val = curmemo[node]
            return (True, val)
        else:
            return (False, None)

    def dpset(node, dac, fft, val):
        curmemo = memo[dac][fft]
        curmemo[node] = val

    def dfs(node, path):
        if node == "out":
            if "dac" in path and "fft" in path:
                return 1
            else:
                return 0

        if node in path:
            return 0

        dac = 1 if "dac" in path else 0
        fft = 1 if "fft" in path else 0
        (worked, val) = dpget(node, dac, fft)
        if worked:
            return val

        path.append(node)

        res = 0
        for nbor in edges[node]:
            res += dfs(nbor, path)

        dpset(node, dac, fft, res)

        path.pop()

        return res

    print(dfs("svr", []))


solve()
