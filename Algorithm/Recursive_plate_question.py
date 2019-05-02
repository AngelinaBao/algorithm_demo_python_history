def move(m, A, B, C):
    if m == 1:
        print(A, 'to', B)  # 最后一个盘子从A移到B
    else:
        move(m - 1, A, C, B) #剩下的盘子从A移到C
        move(1, A, B, C)
        move(m - 1, C, B, A) #从A移到C的盘子，再从C移到B

move(3, 'A', 'B', 'C')

