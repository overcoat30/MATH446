import math

c = 246886422468.0
d = 13579.0

direct = math.sqrt(c * c + d) - c
rearranged = d / (math.sqrt(c * c + d) + c)

print(direct)
print(rearranged)