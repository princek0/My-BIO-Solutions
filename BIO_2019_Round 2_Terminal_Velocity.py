from itertools import combinations
from collections import Counter

p = int(input(""))
collisions = []
collisions_reversed = []
while (-1, -1) not in collisions:
    a, b = input().split(" ")
    collisions.append((max(int(a), int(b)), min(int(a), int(b))))
    collisions_reversed.append((min(int(a), int(b)), max(int(a), int(b))))

collisions.pop()

combinations = list(combinations([i for i in range(1, p + 1)], 2))
for i in range(len(collisions)):
    if collisions_reversed[i] in all:
        combinations.remove((collisions_reversed[i]))

for i in range(len(combinations)):
    if combinations[i] not in collisions:
        collisions.append(combinations[i])

collisions_birds = []

for i in range(len(collisions)):
    collisions_birds.append(collisions[i][0])

counter = dict(Counter(collisions_birds))
for i in range(1, p + 1):
    if i not in counter.keys():
        counter[i] = 0

counter_reversed = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1])}

for i in range(len(list(counter_reversed.keys())[::-1])):
    print(list(counter_reversed.keys())[::-1][i], sep=' ', end=' ', flush=True)
