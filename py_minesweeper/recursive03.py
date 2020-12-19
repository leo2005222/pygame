# factorial(n)
# 1~n 팩토리얼 구하기
# factorial(5) = 5*4*3*2*1

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
