import numpy as np

p = [.25, .30, .15, .30]
pk = [.25, .50, .25]
e = [[3, 4, 2, 1],[3, 1, 4, 2],[4, 3, 1, 2]]

def Bayes(p, pk, e):
    ppgivenc = []
    m = len(pk)
    n = len(p)
    q = np.zeros(n)
    pcgivenp = np.zeros((n,n))
    ppgivenc = np.zeros((n,n))
    for i in range(m):
        for j in range(n):
            q[e[i][j] - 1] = q[e[i][j] - 1] + pk[i] * p[j]
            pcgivenp[e[i][j] - 1][j] = pcgivenp[e[i][j] - 1][j] + pk[i]
    for i in range(n):
        for j in range(n):
            ppgivenc[i][j] = pcgivenp[j][i] * p[i]/q[j]
    return q, ppgivenc

Bayes(p,pk,e)
