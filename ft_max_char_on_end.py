def ft_max_char_on_end(str):
    nums = "0123456789"
    result = ''
    maxx = 0
    nov = 0
    for i in str:
        if i in nums:
            nov += 1
        elif i not in nums:
            if nov > maxx:
                maxx = nov
            nov = 0
        if nov > maxx:
            maxx = nov
    return maxx
