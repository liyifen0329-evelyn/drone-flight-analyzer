with open("data/flight_log.csv",encoding="utf-8")as f:
    lines = f.readlines()

keys = lines[0].strip().split(",")

rows = []
for line in lines[1:]:
    value = line.strip().split(",")
    
    row = {
        keys[0]:value[0],
        keys[1]:value[1],
        keys[2]:value[2],
        keys[3]:value[3],
    }
    rows.append(row)
print("一共:", len(rows),"条记录")
print(rows[0])