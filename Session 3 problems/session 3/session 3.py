# 2.
s = input()
a = list(map(int, s.split()))
i = 1

for i in range(1, len(a)):
    if a[i] * a[i-1] > 0:
        print(str(a[i - 1]), str(a[i]))
        break
    elif i == len(a)-1:
        print("")

# 3.


def numb_of_distinct(L):
    i = 1
    quantity = 1
    for i in range(1, len(L)):
        if L[i] != L[i-1]:
            quantity += 1
    return (quantity)


# 4.
s = input()
a = list(map(int, s.split()))
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))

# 5.
s = input()
a = list(map(int, s.split()))

max = a.index(max(a))
min = a.index(min(a))
a[max], a[min] = a[min], a[max]
print(a)

# 6.
s = input()
a = list(map(int, s.split()))

t = input()
b = list(map(int, t.split()))

res = []
for element in a:
    if element not in b:
        res.append(element)

res.sort()
print(res)

# 7.


def word_count(s):
    return (s.count(' ') + 1)


# 8.
s = input()

if s.count("f") >= 2:
    print(s.find("f"), s.rfind("f"))
elif s.find("f") == 0:
    print(s.find("f"))
else:
    print(s.find("f"))

# 9.


def distinct_nums(t):
    return len(set(t))


# 10.
s = input()
a = list(map(int, s.split()))

t = input()
b = list(map(int, t.split()))

count = len(set(a) & set(b))
print(count)

# 11.
s = set(input().split())

finished = False
c = False
while finished == False:
    print()
    s1 = input()
    if s1 != 'END':
        if c == False:
            delete_values = s1.split()
            for deleting in delete_values:
                if deleting in s:
                    s.remove(deleting)
        else:
            add_values = s1.split()
            for adding in add_values:
                if adding not in s:
                    s.add(adding)
        c = not c
    else:
        finished = True
        print(sorted(s))

# 12.
rounds = int(input())
d = dict()
i = 0
while i < rounds:
    pairs = input().split(' ')
    d[pairs[0]] = pairs[1]
    i += 1
print(d.get(input()))

# 13.

s = input().split(' ' or "  ")
d = dict()
for word in s:
    if word not in d:
        d[word] = 0
        print(d[word])
    else:
        d[word] = d[word] + 1
        print(d[word])

# 14.
rounds = int(input())
d = dict()
i = 0
while i < rounds:
    pairs = input().split(' ')
    d[pairs[1]] = pairs[0]

city = input()

country = d[city]
print(list(d.values()).count(country))

# 15.


def word_count(L):
    count = dict()
    words = L.split()

    for word in words:
        if word not in count:
            count[word] = 1

    return (list(count.values()).count(1))
