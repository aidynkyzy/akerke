d = {
    'A': 'Newfoundland',
    'B': 'Nova Scotia',
    'C': 'Prince Edward Island',
    'E': 'New Brunswick',
    'G': 'Quebec', 'H': 'Quebec', 'J': 'Quebec',
    'K': 'Ontario', 'L': 'Ontario', 'M': 'Ontario', 'N': 'Ontario', 'P': 'Ontario',
    'R': 'Manitoba',
    'S': 'Saskatchewan',
    'T': 'Alberta',
    'V': 'British Columbia',
    'X': 'Nunavut',
    'X': 'Northwest Territories',
    'Y': 'Yukon',
}

def main():
    s = input().upper()
    if s[0] not in d or s[1] not in '0123456789':
        return 'invalid'
    ans = ''
    if s[0] == '0':
        ans += 'rural'
    else:
        ans += 'urban'
    print('%s address in %s' % (ans, d[s[0]]))

main()
