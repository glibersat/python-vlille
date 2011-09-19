from vlille import Vlille

v = Vlille()

v.load_stations()
v.refresh_stations()

print v.stations
