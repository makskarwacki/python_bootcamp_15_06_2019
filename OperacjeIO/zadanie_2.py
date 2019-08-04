import sys
from collections import defaultdict


if len(sys.argv) < 2:
    fname = "dane/logs.txt"
else:
    fname = sys.argv[1]


last_login = {}
total_time = defaultdict(int)

with open(fname) as f:
    for line in f:
        user, action, time_str = line.split(";")
        time = int(time_str)
        if action == "LOGIN":
            last_login[user] = time
        elif action == "LOGOUT":
            total_time[user] += time - last_login[user]

print("Czas przebywania w systemie:")
# print(total_time.items())
for user, time in sorted(total_time.items(), key=lambda x: x[1], reverse=True):
    print(f' - {user}: {time} s')

