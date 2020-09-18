temp = float(input("Please input temperature in celsius, less or equal 10 degrees  "))
wind = float(input("Please input wind speed in km/h less or equal 4.8  "))

if temp >= 10 or wind >=4.8:
    print("invalid value of temperature or wind speed  ")

else:
    wci = 13.12 + 0.6215*temp - 11.37* (wind**0.16) + 0.3965*temp*(wind**0.16)
    wci2 = round(wci)
    print(wci2)