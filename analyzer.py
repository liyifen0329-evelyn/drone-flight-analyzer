with open("data/flight_log.csv",encoding="utf-8")as f:
    lines = f.readlines()

n = 1
for line in lines:
    print(n, line.strip())
    n = n+1
print("总行数：",len(lines),"行")