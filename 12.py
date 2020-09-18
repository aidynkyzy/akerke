from math import radians, cos, sin, asin, sqrt
 
print("Enter the latitude and longitude of two points on the Earth in degrees:")
lat1 = float(input(" Latitude 1: "))
lat2 = float(input(" Latitude 2: "))
lon1 = float(input(" Longitude 1: "))
lon2 = float(input(" Longitude 2: "))
 
dlon = lon2 - lon1 
dlat = lat2 - lat1 
a = sin(dlat/2)*2 + cos(lat1) * cos(lat2) * sin(dlon/2)*2
c = 2 * asin(sqrt(a)) 
r = 6371 
print("Distance is: ",c*r,"Kilometers")