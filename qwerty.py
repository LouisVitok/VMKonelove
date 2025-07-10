def cod(x):
    if x <= 25:
        return x
    elif x < 10 and x >= 0:
        return 26 + x
    else:
        return 36


def encode(x):
    if x >= 0 and x < 26:
        return chr(ord('A') + x)
    elif x >= 26 and x < 36:
        return str(x - 26)
    else:
        return '_'


def f(x):
    return (19 * x * x + 19) % 37


if __name__ == '__main__':
    for i in range(37):
        print(f'{encode(i)} - {encode(f(i))}')