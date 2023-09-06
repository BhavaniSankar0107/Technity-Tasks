import math

n, m, a = map(int, input().split())

length_flagstones = math.ceil(n / a)

width_flagstones = math.ceil(m / a)

total_flagstones = length_flagstones * width_flagstones

print(total_flagstones)
