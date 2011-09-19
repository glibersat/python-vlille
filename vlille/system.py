import urllib2 as urllib
import xml.etree.ElementTree

from .station import Station

class Vlille(object):
    """
    The whole system, with stations, bikes, ...
    """
    def __init__(self):
        self.stations = []

    def load_stations(self):
        self.stations = []

        handler = urllib.urlopen("http://vlille.fr/stations/xml-stations.aspx")
        stations_xml = handler.read()

        # replace encoding, since it's wrong !
        stations_xml = stations_xml.replace('utf-16', 'utf-8')

        element = xml.etree.ElementTree.fromstring(stations_xml)

        # Get all stations
        for marker in element.findall('marker'):
            id = marker.get('id')
            lat = marker.get('lat')
            lng = marker.get('lng')
            name = marker.get('name')

            self.stations.append(Station(id, name, lat, lng))


    def refresh_stations(self):
        return [station.refresh() for station in self.stations]






