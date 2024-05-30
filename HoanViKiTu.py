from itertools import permutations
perm = permutations(input())
for x in list(perm):
    print(''.join(x))