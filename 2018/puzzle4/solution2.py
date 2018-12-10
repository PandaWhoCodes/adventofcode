from datetime import datetime
from collections import Counter


def parse_line(line: str) -> tuple:
    """Given a time string, return datetime object and description string.
    Ex: [1518-11-01 00:25] wakes up -> (datetime(1518, 11, 1, 0, 25), "wakes up")"""
    timestr, description = line.split('] ')
    parsed = datetime.strptime(timestr, '[%Y-%m-%d %H:%M')
    return (parsed, description.strip().lower())


with open('input.txt') as data:
    records = sorted([parse_line(line) for line in data], key=lambda record: record[0])

guard_data = {}
curr_guard = None
sleep_time = None

for record in records:
    timestamp, desc = record

    if "guard" in desc:
        curr_guard = desc.split(' ')[1]
        guard_data.setdefault(curr_guard, {"minutes_asleep": []})

    elif "sleep" in desc:
        sleep_time = timestamp

    else:
        guard_data[curr_guard]["minutes_asleep"].extend(
            [minute for minute in range(sleep_time.minute, timestamp.minute)])

best_guard = None
best_minute = (0, 0)

for guard in guard_data:
    common_minute = Counter(guard_data[guard]["minutes_asleep"]).most_common(n=1)
    if common_minute and common_minute[0][1] > best_minute[1]:
        best_guard = guard
        best_minute = common_minute[0]
# print(best_guard)
print(int(best_guard[1:])*best_minute[0])
