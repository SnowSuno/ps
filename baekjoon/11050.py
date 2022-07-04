def combination(n, k):
    if k == 0:
        return 1
    if k > n:
        return 0
    return combination(n-1, k-1) + combination(n-1, k)

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(combination(N, K))
