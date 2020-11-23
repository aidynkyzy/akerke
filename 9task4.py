def anagram(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def main():
    s1 = input().lower().replace(' ', '')
    s2 = input().lower().replace(' ', '')
    if s1 == s2:
        return 'not anagram'
    if anagram(s1) == anagram(s2):
        return 'anagram'
    else:
        return 'not anagram'

print(main())
