#!/usr/bin/evn python3
aa = {'A':71,
'R': 156,
'N': 114,
'D': 115,
'C': 103,
'E': 129,
'Q': 128,
'G': 57,
'H': 137,
'I': 113,
'L': 113,
'K': 128,
'M': 131,
'F': 147,
'P': 97,
'S': 87,
'T': 101,
'W': 186,
'Y': 163,
'V': 99}

min_weight = min(aa.values())
total_per_i = []
#permuts[min_weight-1] = 1    # You cannot assign to a list like lst[i] = something --->
#  "IndexError: list assignment index out of range" first populate it with n*None then assgin values
for curr_i in range(min_weight, 500):
    curr_i_list = []
    for a in aa.values():
        #total_per_a = 0
        #print(a)
        previous = curr_i - a
        if previous > 0:
            if total_per_i[previous] != 0:
                total_per_a = 1
                total_per_a += total_per_i[previous]
                curr_i_list[curr_i].append(total_per_a)   #try appending to previous list instead of updating to new value
                sum_per_i = sum(curr_i_list[curr_i])
                print(sum_per_i)


