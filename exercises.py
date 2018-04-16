#!/usr/bin/env python3

with open("all.txt", 'r') as fh:
    entries = {}
    for l in fh:
        # print(l.strip())
        l = l.strip()
        if l.startswith(">"):
            header = l[1:]
            temp_str = ""
            entries[header] = temp_str
        else:
            temp_str += l
            entries[header] = temp_str
for k, v in entries.items():
    print(k, v)



