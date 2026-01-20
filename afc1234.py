def fp(n,m,path="",i=0, j=0):
    if i == n - 1 and j == m - 1:
        print(path)
        return
    if i < n - 1:
        fp(n, m, path + "D", i + 1, j)
    if j < m - 1:
        fp(n, m, path + "R", i, j + 1)
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
fp(rows, cols)