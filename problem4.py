def g(x):
    return 0.5 * (x + 9.0 / x)


def fpi(g, x0, k):
    x = x0

    for i in range(k):
        x = g(x)

    return x


print(fpi(g, 1.0, 10))