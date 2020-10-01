def ft_percent_lower_uppercase(str):
    a = "qwertyuiopasdfghjklzxcvbnm"
    b = "QWERTYUIOPASDFGHJKLZXCVBNM"
    per = 0
    vto = 0
    result = 0
    for i in str:
        if i in a:
            per += 1
        elif i in b:
            vto += 1
    result = vto / per
    return result
