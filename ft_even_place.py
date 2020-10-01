def ft_even_place(str):
    result = ""
    por = 0
    for i in str:
        if por % 2 == 0:
            result += i
        por += 1
    return result
