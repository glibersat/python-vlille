from vlille import Vlille

v = Vlille()

v.load_stations()
v.refresh_stations()

for station in v.stations:
	print station
	print station.to_json()


