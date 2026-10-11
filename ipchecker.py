count = {}
accepted = set()

with open("auth.log", "r") as f:
    for x in f:
        if "Failed password" in x:
            parts = x.split()
            ip = parts[parts.index("from") + 1]
            count[ip] = count.get(ip, 0) + 1
        if "Accepted password" in x:
            parts = x.split()
            ip = parts[parts.index("from") + 1]
            accepted.add(ip)
            
            
for ip, c in count.items():
    if c >= 3 and ip in accepted:
        print(f"============\n---ATTACK---\n============\nATTACKER IP : {ip}\nFAILED TRIES : {c}\nACCEPTED : YES")
    elif c >= 3:
         print(f"Suspicious user ip : {ip}\nFailed tries : {c}")
