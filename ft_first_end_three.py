def ft_len(str):
    num = 0
    for i in str:
        num += 1
    return num


def ft_first_end_three(str):
    dlin = ft_len(str)
    l = 3
    if dlin > 5:
        for i in range(dlin):
            if i <= 2 or i >= dlin - l:
                return(str[:3] + str[-3:])
    else:
        for c in range(dlin):
            return(str[0] * ft_len(str))
