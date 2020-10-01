def ft_len(str):
    num = 0
    for i in str:
        num += 1
    return num


def ft_slice_str(str, start, end):
    dlin = ft_len(str)
    result = ""
    if dlin >= end:
        for i in range(start, end):
            result += str[i]
        return result
    else:
        for i in range(start, dlin):
            result += str[i]
        return result


def ft_cmp_str(str1, str2, num):
    result = ""
    pervoe = ft_slice_str(str1, 0, num)
    vtoroe = ft_slice_str(str1, num, 99)
    result = pervoe + str2 + vtoroe
    return result
    
    
