d1 = {
    1 : "one", 
    2 : "two", 
    3 : "three", 
    4 : "four", 
    5 : "five", 
    6 : "six", 
    7 : "seven", 
    8 : "eight", 
    9 : "nine", 
    10 : "ten", 
    11 : "eleven",
    12 : "twelve", 
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen", 
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 :"nineteen"
}
d2 = {
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy", 
    80 : "eighty",
    90 : "ninety"
}

def numbertowords(num):
    if num == 0:
        return 'zero'
    elif num < 20:
        return d1[num]
    elif num < 100:
        t = divmod(num, 10)
        return f'{d2[t[0] * 10]} {numbertowords(t[1])}'
    elif num < 1000:
        t = divmod(num, 100)
        return f'{d1[t[0]]} hundred {numbertowords(t[1])}'

def main():
    num = int(input())
    print(numbertowords(num))

main()

