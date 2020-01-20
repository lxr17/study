def aaa():
    x = 200


def bbb():
    global x
    x = 300


def ccc():
    x = 400

    def ddd():
        nonlocal x
        x = 500

    ddd()

    print(x)


def eee():
    x = 600

    def fff():
        global x
        x = 700

        def ggg():
            x = 800

            def hhh():
                nonlocal x

                print(x)

                x = 900

            hhh()
            print(x)

        ggg()
        print(x)

    fff()
    print(x)


# 这个会报错
# def test():
#     global x
#     x = 200
#
#     def test2():
#         nonlocal x
#         x = 300
#
#     test2()


if __name__ == '__main__':
    x = 100
    aaa()
    print(x)

    x = 100
    bbb()
    print(x)

    x = 100
    ccc()
    print(x)

    x = 100
    eee()
    print(x)

    # 这个会报错
    # x = 100
    # test()
    # print(x)
