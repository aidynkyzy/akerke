def reverselookup(d, v):
    l = []
    for k in d:
        if d[k] == v:
            l.append(k)
    return l

d = {'world': 'hello', 'hi': 'hello', 'python': 'hello'}
v = input()
print(reverselookup(d, v))

