def check(d):
    sum = 0
    for k in d:
        for i in range(5):
            sum += d[k][i]
        if sum == 0:
            return True

    sum = 0
    for i in range(5):
        for k in d:
            sum += d[k][i]
        if sum == 0:
            return True

    sum = i = 0
    for k in d:
        sum += d[k][i]
        i += 1
    if sum == 0:
        return True
       
    sum = 0
    i = 4
    for k in d:
        sum += d[k][i]
        i -= 1
    if sum == 0:
        return True

    return False

d = {
    'B': [15, 14, 4, 10, 7],
    'I': [22, 21, 30, 19, 17],
    'N': [35, 37, 39, 45, 41],
    'G': [53, 48, 55, 52, 57],
    'O': [61, 67, 70, 72, 63]
}

print(check(d))
