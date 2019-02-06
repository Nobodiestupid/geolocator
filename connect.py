from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="ajkshdkjahjksd")
# lon = input("longitude = ")
# lat = input("latitude = ")
location = geolocator.reverse("-0.02271831, 109.32628423")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)