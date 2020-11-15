# 1.

Xstrs = input().split()
X = [int(x) for x in Xstrs]

Ystrs = input().split()
Y = [int(x) for x in Ystrs]

# insert a list comprehension expression
Z = [(x, y) for x in X for y in Y if x < y]

for pair in Z:
    print(pair[0], pair[1])

# 2.
X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]

it_squared_mapping = zip((x*x for x in X), Y)  # insert a zip expression here

for x in it_squared_mapping:
    print(x[0], x[1])

# 3.


def binary_map(func_of_2, col1, col2):
    return (func_of_2(z[0], z[1]) for z in zip(col1, col2))


# 4.


def stringify(f):
    def new_func(X):
        Y = ''
        for x in X:
            Y += f(x)
        return Y
    return new_func
