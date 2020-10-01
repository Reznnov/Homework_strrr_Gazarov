def ft_len(str):
    num = 0
    for i in str:
        num += 1
    return num


def ft_find_str(str1, str2):
    dlin = ft_len(str1)
    chis = 0
    result = ''
    ot = 0
    prog = 0
    flag = True
    for i in str2:
        if i == str1[chis] and flag == True:
            ot = prog
            prog += 1
            flag = False
            chis += 1
            result += i
            if result == str1:
                return ot
        elif i == str1[chis] and flag == False:
            prog += 1
            chis += 1
            result += i
            if result == str1:
                return ot
        else:
            ot = 0
            flag = True
            result = ''
            chis = 0
            prog += 1
