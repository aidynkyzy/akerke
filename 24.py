days = int(input(" Input days: "))
hours = int(input("Input hours: "))
minutes = int(input("Input minutes: "))
seconds = int(input("Input seconds: "))

total_seconds = (days * 24 * 3600) + (hours* 3600)+(minutes*60) + seconds
print(" Total number of seconds: ",  total_seconds)