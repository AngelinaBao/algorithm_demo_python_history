def triangles(n):
    L, index = [1], 0
    while index < n:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]
        index += 1

g = triangles(8)
for t in g:
    print(t)