
# a / b = c / d
# => ad = bc
# 1 / 2 = 4 / 8
# => 1*8 = 2*4 == true!

# 1 / 2 = 4 / 8 = 3 / 6
# => 1*8 = 2*4
# => 4*6 = 8*3

from itertools import permutations, combinations
count = 0

pool = permutations("987654321",9)
# print(f"Size of pool is {size}")

for permutation in pool:
    count=count+1
    # print(permutation)
    l = list(permutation)
    a = int(l.pop(0))
    b = int(l.pop(0))

    # a must be larger than b - as a shortcut to skip some
    if (b < a):
        continue

    c = int(l.pop(0))
    de = int(l.pop(0)) * 10 + int(l.pop(0))
    fg = int(l.pop(0)) * 10 + int(l.pop(0))
    hi = int(l.pop(0)) * 10 + int(l.pop(0))

    # print(f"a={a} b={b} c={c} de={de} fg={fg} hi={hi}")

    # If equation 1 doesn't work, continue...
    if (a * de != b * c):
        continue

    # If second equation doesn't work, continue...
    if (c * hi != de * fg):
        # print(f"eq1 worked: a={a}, b={b}, c={c}, de={de}, but not eq2")
        continue

    print(f"SOLVED after {count} tries...")
    print (f"a={a}, b={b}, c={c}, de={de}, fg={fg}, hi={hi}")
    break

print (f"Done in {count} permutations")
