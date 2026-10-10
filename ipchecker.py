counts = {}
with open("auth.log") as f:
    for line in f:
        if "Failed password" in line:
            parts = line.split()
            pos = parts.index("from")
            ip = parts[pos + 1]
            counts[ip] = counts.get(ip, 0) + 1  

print(counts)

for ip, count in counts.items():
    if count >= 3:
        print(f" {ip} — {count} fails")