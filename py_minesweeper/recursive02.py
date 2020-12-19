# 1~n까지 합 구하기
# add(n)

def add(n):
    if n == 0:
        return 0
    return n + add(n - 1)


print(add(5))
