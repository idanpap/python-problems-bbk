# 1.
def expo(a, n):
    if n == 0:
        return 1
    else:
        power_n_minus_1 = expo(a, n-1)
        result = a*power_n_minus_1
    return result


print(expo(2, 2))

# 2.


def my_sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        latter_numbers = lst[1:]
        result = lst[0] + my_sum(latter_numbers)
        return result


print(my_sum([1, 2, 3]))

# 3.


def my_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        rest_of_list = lst[1:]
        if lst[0] > my_max(rest_of_list):
            return lst[0]
        else:
            return my_max(rest_of_list)


print(my_max([3, 2, 5]))

# 4.


def rev_string(s):
    if len(s) == 0:
        return s
    else:
        return rev_string(s[1:]) + s[0]


print(rev_string("abcb"))
