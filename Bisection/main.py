import numpy as np

import TableIT


def bisect(func, low, high, tolerance, max_iter):
    a = [low]
    b = []
    fa = [f(low)]
    fb = []

    c = (low + high) / 2.0
    low = c
    Xs = 0.3604217029603
    np.linalg.norm(low - Xs)
    itr = 0
    xp = []  # converte a raiz
    errores_Abs = []
    errores_Aprox = []
    fs = []  # converte o zero
    while ((high - low) / 2.0 > tolerance) and (itr < max_iter):
        fs.append(f(c))
        xp.append(c)
        a.append(low)
        b.append(high)
        fa.append(f(low))
        fb.append(f(high))

        if f(c) == 0:
            return c
        elif f(low) * f(c) < 0:
            high = c
        else:
            low = c
        c = (low + high) / 2.0
        itr += 1
        err_Abs = np.linalg.norm(low - Xs)
        err_Aprox = np.linalg.norm(high - low)

        errores_Abs.append(err_Abs)
        errores_Aprox.append(err_Aprox)
    return low, errores_Abs, errores_Aprox, fs, xp, a, b, fa, fb


def f(x):
    return (x ** 5) - (2 * (x ** 4)) + (x ** 2) - (3 * x) + 2


max_iter = 1000
xm, err_Abs, err_Aprox, fs, xp, a, b, fa, fb = bisect(f, -2, -1, 1e-5, max_iter)

table = [
    ['a', 'b', 'f(a)', 'f(b)', 'xms', 'f(xm)', 'error']
]

# err_Aprox.pop(0)
for i in range(len(err_Aprox)):
    table.append([])
    table[i + 1].append(round(a[i], 5))
    table[i + 1].append(round(b[i], 5))
    table[i + 1].append(round(fa[i], 5))
    table[i + 1].append(round(fb[i], 5))
    table[i + 1].append(round(xp[i], 5))
    table[i + 1].append(round(fs[i], 5))
    table[i + 1].append(round(err_Aprox[i], 5))

TableIT.printTable(table)
print('xm: {}'.format(xm), '{}'.format(f(xm)))
