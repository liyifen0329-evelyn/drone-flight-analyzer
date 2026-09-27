with open("data/flight_log.csv",encoding="utf-8")as f:
    lines = f.readlines()

keys = lines[0].strip().split(",")

rows = []
max_altitude = 0
over_count = 0

for line in lines[1:]:
    value = line.strip().split(",")
    
    row = {
        keys[0]:value[0],
        keys[1]:value[1],
        keys[2]:value[2],
        keys[3]:value[3],
    }
    rows.append(row)

    altitude = int(value[1])
    if altitude > max_altitude:
        max_altitude = altitude
    if altitude > 120:
        over_count += 1
print("一共:", len(rows),"条记录")
print("最高高度：", max_altitude, "米")
print("超限次数：", over_count, "次")