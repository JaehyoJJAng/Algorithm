import collections

my_str = input().strip()

counter = collections.Counter(my_str).most_common()
answer  = ''
for i in range(len(counter)):
    if counter[i][1] == counter[0][1]:
        answer += counter[i][0]
print("".join(sorted(list(answer))))

# ===

from collections import Counter

my_str = input().strip()
max_count = max(Counter(my_str).values())
print(''.join(sorted([k for k,v in Counter(my_str).items() if v == max_count ])))