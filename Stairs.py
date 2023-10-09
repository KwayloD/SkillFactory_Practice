def stairs(n):
    for i in range(n, 0, -1):
        print("*" * i)
    for u in range(1, n+1):
        print("*" * u)
stairs(6)
