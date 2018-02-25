#!/usr/bin/env python3

"""
a function to compute the gc content of an input sequence
"""


def compute_gc(sequence):
    tg = 0
    tc = 0
    ta = 0
    tt = 0
    for c in sequence:
        if c == "G":
            tg += 1
        elif c == "C":
            tc += 1
        elif c == "A":
            ta += 1
        elif c == "T":
            tt += 1
    total = tg + tc + ta + tt
    gc_content = (tg + tc) / total
    return gc_content


"""
Make a function dist(a, b) that takes two DNA sequences of the same length and returns the Hamming distance between them, i.e., the number of symbols at the same position that differ. For example, dist('GGGAT', 'GGCCT') = 2, because GA -> CC and everything else remains the same.
"""


def dist(a, b):
    HD = 0
    zipped = zip(a, b)
    for c1, c2 in zipped:
        # print(c1, c2)
        if c1 == c2:
            continue
        else:
            HD += 1
    return HD


"""
Make a function that takes two characters as input and returns 1 if they are identical and 0 otherwise. Call it score(a,b)
"""


def score(char1, char2):
    if char1 == char2:
        return 1
    else:
        return 0


"""
Write a function that takes two strings and counts the matches.
If the strings are 'GGGAT' and 'GGCCT' the function should return 3.
"""


def match_finder(s1, s2):
    zipped = zip(s1, s2)
    # print(zipped)
    matches = 0
    for a, b in zipped:
        if a == b:
            matches += 1
    return matches


if __name__ == "__main__":
    compute_gc()
    dist("CCCAAA", "CCCTTT")
    score("a", "b")
    match_finder("GGGAT", "GGCCT")

