from math import radians, cos, sin, asin, sqrt
 
print("Enter the latitude and longitude of two points on the Earth in degrees:")
lt1 = float(input(" Latitude 1: "))
lt2 = float(input(" Latitude 2: "))
ln1 = float(input(" Longitude 1: "))
ln2 = float(input(" Longitude 2: "))
 
dln = ln2 - ln1 
dlt = lt2 - lt1 
a = sin(dlt/2)*2 + cos(lt1) * cos(lt2) * sin(dln/2)*2
c = 2 * asin(sqrt(a)) 
r = 6371 
print("Distance is: ",c*r,"Kilometers")
