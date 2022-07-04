def anagram(s1, s2):
    ht = dict()
    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1

    for i in ht:
        if ht[i] != 0:
            return False
    return True


print(anagram('fairy tales'.replace(" ", "").lower(),
              'rail safety'.replace(" ", "").lower()))
