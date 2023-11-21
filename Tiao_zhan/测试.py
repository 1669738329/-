import time
s = time.time()


def find(num):
    for i in range(1, int(num**0.5)+1):
        if num == sum(int(x) ** i for x in str(num)):
            return num, i
    return num, -1


a = []
for n in range(10, 10001):
    if find(n)[1] != -1:
        a.append(find(n))
print(a)
e = time.time()
print(e-s)
