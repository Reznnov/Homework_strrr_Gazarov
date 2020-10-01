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
                print(str[i])
    else:
        for c in range(dlin):
            print(str[0])
