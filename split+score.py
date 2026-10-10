scores = {}
lines = ["root 185.220.101.5", "admin 185.220.101.5", "ivan 192.168.1.10", "root 45.155.205.99", "root 185.220.101.5"]

for x in lines:
    parts = x.split()
    parts = parts[1]
    scores[parts] = scores.get(parts, 0) + 1

print(scores)