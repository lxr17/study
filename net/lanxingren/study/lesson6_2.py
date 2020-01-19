def main():
    # TODO
    return


def max(*args):
    max = args[0]
    for _ in args:
        if _ > max:
            max = _

    return max


if __name__ == '__main__':
    print(max(5, 6, 3, 3, 4, 5, 6, 34, 7, 2, 1114, 567, 44))
