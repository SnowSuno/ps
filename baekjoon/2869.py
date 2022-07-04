import math

def calculateTime(increment, decrement, total):
    return math.ceil((total - increment) / (increment - decrement)) + 1


if __name__ == '__main__':
    A, B, V = map(int, input().split())

    print(calculateTime(A, B, V))
