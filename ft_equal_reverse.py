def ft_len(str):
    num = 0
    for i in str:
        num += 1
    return num


def ft_reverse_str(str):
    dlin = ft_len(str)
    isi = dlin - 1
    result = ""
    for i in range(dlin):
        result += str[isi]
        isi -= 1
    return result


def ft_equal_reverse(str):
    dlin = ft_len(str)
    perevorot = ft_reverse_str(str)
    if str == perevorot:
        return True
    else:
        return False
