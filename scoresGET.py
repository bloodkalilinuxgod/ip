scores = {}
names = ["root", "admin", "root", "ivan", "root", "admin"]

for x in names:
    if x == x:
        scores[x] = scores.get(x, 0) + 1

print(scores)