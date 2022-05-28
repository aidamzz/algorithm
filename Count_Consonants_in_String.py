input_str_1 = 'abc de'
input_str_2 = 'LuCiDProGRamMiNG'

vowels = 'aiuoe'
#with loop
def count_cons(st):
    coun = 0
    for i in range(0,len(st)):
        

        if st[i].lower() not in vowels and st[i].isalpha():
            coun +=1
    return coun

#without loop

def count_cons_withoutloop(st):

    if st != '':
        if st[0].lower() not in vowels and st[0].isalpha():
            return 1+ count_cons_withoutloop(st[1:])
        else:
            return count_cons_withoutloop(st[1:])
    else:
        return 0
