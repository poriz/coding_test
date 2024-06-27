import sys

a,b = map(int,sys.stdin.readline().split())

from math import gcd

print(gcd(a,b))
print(int(a*b/gcd(a,b)))