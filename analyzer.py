import sys

if len(sys.argv) < 2:
    print("用法: python3 analyzer.py 日志文件.csv")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("找不到这个文件:", filename)
    sys.exit(1)

print("正在分析:", filename)

if len(lines) < 2:
    print("这个文件是空的,或者只有表头,没有可分析的数据")
    sys.exit(1)

keys = lines[0].strip().split(",")

if len(keys) != 4:
    print("表头应该有 4 列 (time, altitude, speed, battery),实际是:", keys)
    sys.exit(1)

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

report = f"""# 无人机飞行安全报告 · {filename}

- 分析记录数：{len(rows)} 条
- 最高飞行高度： {max_altitude} 米
- 高度超限次数 (>120米): {over_count}次
结论：本次飞行共 {over_count} 次超过 120 米安全高度限制，建议复查航线规划。
"""
print(report)

with open("report.md","w",encoding="utf-8") as f:
    f.write(report)

print("报告已生成: report.md")

