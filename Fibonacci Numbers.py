"""
a function int fib(int n) that returns Fn. For example, if n = 0, then fib() should return 0.
If n = 1, then it should return 1. For n > 1, it should return Fn-1 + Fn-2
"""
def fibonacci(N):
    # Taking 1st two fibonacci nubers as 0 and 1
    f = [0, 1]
    for i in range(2, N + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[N]

N = int(input())
print(fibonacci(N))