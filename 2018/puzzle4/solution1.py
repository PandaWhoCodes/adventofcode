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
        guard_data.setdefault(curr_guard, {"total_sleep": 0, "minutes_asleep": []})

    elif "sleep" in desc:
        sleep_time = timestamp

    else:
        tdelta = (timestamp - sleep_time).total_seconds()
        guard_data[curr_guard]["total_sleep"] += tdelta
        guard_data[curr_guard]["minutes_asleep"].extend(
            [minute for minute in range(sleep_time.minute, timestamp.minute)])

sleepiest_guard = sorted(guard_data.items(), reverse=True, key=lambda guard: guard[1]["total_sleep"])[0]
most_common_minute = Counter(sleepiest_guard[1]["minutes_asleep"]).most_common(n=1)[0][0]
print(sleepiest_guard)
print(most_common_minute)
print("Answer:",most_common_minute * int(sleepiest_guard[0][1:]))