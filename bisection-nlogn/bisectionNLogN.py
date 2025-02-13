import math

def nlogn(c):
    lower = 0
    upper = 10e200
    while True:
        middle = (lower+upper)/2
        if lower == middle or middle == upper:
            return middle
        if middle*math.log(middle, 2) > c:
            upper = middle
        else:
            lower = middle

print("n log2(n) equals to:")
print(nlogn(float(input())))