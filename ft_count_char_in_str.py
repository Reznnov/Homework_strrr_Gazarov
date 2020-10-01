def ft_сount_char_in_str(char, str):
    coll = 0
    for i in str:
        if i == char:
            coll += 1
    return coll
