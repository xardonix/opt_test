class Functions:
    def func1(x):
        return 4 * pow((x[0] - 5), 2) + pow((x[1] - 6), 2)

    def func2(x):
        return pow(x[0] * x[0] + x[1] - 11, 2) + pow(x[0] + x[1] * x[1] - 7, 2)

    def func3(x):
        return (100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2 + 90 * (x[3] - x[2] ** 2) ** 2 + (
                    1 - x[2]) ** 2 + 10.1 * (
                        (x[1] - 1) ** 2 + (x[3] - 1) ** 2) + 19.8 * (x[1] - 1) * (x[3] - 1))

    def func4(x):
        return ((x[0] + 10 * x[1]) ** 2 + 5 * (x[2] - x[3]) ** 2 + (x[1] - 2 * x[2]) ** 4 + 10 * (x[0] - x[3]) ** 4)

