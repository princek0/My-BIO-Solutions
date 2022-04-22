from itertools import combinations
from collections import Counter

p = int(input(""))
data = []
data_reverse = []
while (-1, -1) not in data:
    a, b = input().split(" ")
    data.append((max(int(a), int(b)), min(int(a), int(b))))
    data_reverse.append((min(int(a), int(b)), max(int(a), int(b))))

data.pop()

all = list(combinations([i for i in range(1, p+1)],2))
for i in range(len(data)):
    if data_reverse[i] in all:
        all.remove((data_reverse[i]))


for i in range(len(all)):
    if all[i] not in data:
        data.append(all[i])

data2 = []

for i in range(len(data)):
    data2.append(data[i][0])

counter = dict(Counter(data2))
for i in range(1, p+1):
    if i not in counter.keys():
        counter[i] = 0

dict2 = {k: v for k, v in sorted(counter.items(), key=lambda item: item[1])}
print(dict2)
for i in range(len(list(dict2.keys())[::-1])):
    print(list(dict2.keys())[::-1][i])
    
