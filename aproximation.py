import numpy as np
def divided_diffs(x: np.ndarray, f):
    y = f(x)
    diffs = []
    diff = y.tolist()
    for i in range(len(x) - 1):
        diffs.append(diff)
        diff = []
        for j in range(len(diffs[i]) - 1):
            d_f = diffs[i][j + 1] - diffs[i][j]
            d_x = x[j + i + 1] - x[j]
            diff.append(d_f / d_x)
    diffs.append(diff)
    return diffs

def back_interpolation(points: np.ndarray, f):
    diffs = divided_diffs(points, f)
    def newton_formula(x):
        s = 0
        for i in range(len(points) - 1, -1, -1):
            a = diffs[len(points) - i - 1][i]
            for j in range(len(points) - 1 - i):
                a *= x - points[len(points) - 1 - j]
            s += a
        return s
    return newton_formula

def f(x):
    return x ** 3
if __name__ == '__main__':
    # arr = divided_diffs(np.array([1, 2, 3]), f)
    # for el in arr:
    #     print(*el)
    newton = back_interpolation(np.array([1, 2, 3]), f)
    print(newton(2.2))
