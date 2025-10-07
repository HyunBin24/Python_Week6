#3_p.32
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print(smallest)

#3_p.33
a = [38, 21, 53, 62, 19]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(largest)

#3_p.34
a = [38, 21, 53, 62, 19]
a.sort()
print(a[0], " and ", a[-1])

#3_p.35
a = [38, 21, 53, 62, 19]
min_value = min(a)
max_value = max(a)
print(min_value, " and ", max_value)

#3_p.36
a = [38, 21, 53, 62, 19]
result = 0
for i in a:
    result += i
print(result)

a = [38, 21, 53, 62, 19]
result = sum(a)
print(result)

#3_p.37
a = [i for i in range(10)]
b = list(i for i in range(10))
print(a)
print(b)

#3_p.38
a = [i + 5 for i in range(10)]
b = list(i * 2 for i in range(10))
print(a)
print(b)

#3_p.39
a = [i for i in range(10) if i % 2 == 0]
print(a)

#3_p.40
a = [i + 5 for i in range(10) if i % 2 == 1]
print(a)

#3_p.41
a = [i * j for j in range(2, 10) for i in range(1, 10)]
print(a)

#3_p.42
a = [i * j for j in range(2, 10)
            for i in range(1, 10)]
print(a)

#3_p.43
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)

#3_p.44
a = list(map(str, range(10)))
print(a)

#3_p.45
a = list(map(int, input().split()))
print(a)

#3_p.46
a = (38, 21, 53, 62, 19, 53)
b = a.index(53)
print(b)

#3_p.47
a = (10,20, 30, 15, 20, 40)
b = a.count(20)
print(b)

#3_p.48
a = (38, 21, 53, 62, 19)
for i in a:
    print(i, end=' ')

#3_p.49
a = tuple(i + 5 for i in range(10) if i % 2 == 1)
print(a)

#3_p.50
a = tuple(1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)

a = (38, 21, 53, 62, 19)
print(min(a), max(a), sum(a))

#3_p.56
a = [[10, 20], [30, 40], [50, 60]]
b = [[10, 20],
     [30, 40],
     [50, 60]]
print(a)
print(b)

#3_p.57
a = [[10, 20],
     [30, 40],
     [50, 60]]
print(a[1][0])
print(a[0][1])
a[2][1] = 100
print(a)

#3_p.58
a = [[10, 20],
     [30, 40],
     [50, 60]]
for x, y in a:
    print(x, y)

#3_p.59
a = [[10, 20],
     [30, 40],
     [50, 60]]

for x in a:
    print(x)
    for y in x:
        print(y, end=' ')
    print()
    