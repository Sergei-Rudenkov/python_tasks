def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def main():
    print(reduce(lambda x, y: int(x) + int(y), [char for char in str(factorial(100))]))


if __name__ == '__main__':
    main()