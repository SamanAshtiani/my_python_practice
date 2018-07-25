#!/usr/bin/env python3


string_list = ['adfasklakr',
                'sdkflafdal',
                'dlkadjfakd']
print('length of second strin: ', len(string_list[1]))
print('what second seq really looks in interpreter: ', repr(string_list[1]))

col_dic = {}

for i, c in enumerate(string_list[0]):
    col_list = []
    col_list.append(c)
    col_dic[i] = col_list
print(col_dic)

for i, s in enumerate(string_list):
    if i == 0:
        continue
    print('i and s: ', i, s)

    for j, c in enumerate(s):
        # print('j: ', j)
        # print(col_dic[j])  #what it prints is one iteration before the last one, hence lists of 2elements instd of 3
        col_dic[j].append(c)

print(col_dic)


final_list = []
for k, v in col_dic.items():
    freq_dic = {}
    # print(v)
    for l in v:
        freq_k = freq_dic.keys()
        if l in freq_k:
            freq_dic[l] += 1
        else:
            freq_dic[l] = 1
    final_list.append(freq_dic.items())
    print("for {}th column, frequency is: {}".format(k, freq_dic))

print(final_list)



