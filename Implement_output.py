import OpenMapQuest 
'''
What does the elevation class do? it takes another, different json response & gives
the height. then do the same shit, but with new dict.
So step 1: make new dict 
        '''
MapQuestDict = OpenMapQuest.get_Result(OpenMapQuest.build_search_url(['Irvine,CA','Los Angeles,CA']))
class Distance:
    def __init__(self, info:dict):
        distance = info['route']['distance']
        self._distance = distance

    def get_distance(self) -> str:
        return self._distance

    def display(self):
        print(self.get_distance())
        
class Steps:
    def __init__(self, info:dict):
        directions = ''
        for leg_list in info['route']['legs']:
            for maneuvers in leg_list['maneuvers']:
                directions += maneuvers['narrative'] + '\n'
        self._directions = directions

    def get_directions(self) -> str:
        return self._directions

    def display(self):
        print(self.get_directions())

class Time:
    def __init__(self, info:dict):
        time = info['route']['time']
        self._time = time

    def get_time(self) -> str:
        return self._time

    def display(self):
        print(self.get_time() + 'minutes')

class LatLong:
    def __init__(self, info:dict):
        latlng = []
        for i in info['route']['locations']:
            for d in i['latLng'].values():
                latlng.append(d)
        self._latlng = latlng
        
    def get_latLng_list(self):
        return self._latlng
    def N_or_S(self, lat:int)-> str:
         if lat> 0:
             return ('{:.2f}N'.format(lat))
         else:
             return ('{:.2f}S'.format(-1*lat))
    def E_or_W(self, lng:int) -> str:
         if lng > 0:
             return ('{:.2f}E'.format(lng))
         else:
             return ('{:.2f}W'.format(-1*lng))
                   
    def display(self):
        n = len(self.get_latLng_list())
        while n>0:
            lat_and_lng= []
            lat = ''
            lng= ''
            lnglat = '' 
            for i in range(len(self.get_latLng_list())):
                if i%2 == 0:
                    lng += self.E_or_W(self._latlng[i])+' '
                elif i%2 == 1:
                    lat += self.N_or_S(self._latlng[i]) + ' '
            n-=1
        lnglat = lat + lng
        lat_and_lng = lnglat.split()
        for i in range(len(lat_and_lng)):
            if lat_and_lng[i][-1] == 'N':
                print(lat_and_lng[i], lat_and_lng[i+2])
            else:
                pass
r= LatLong(MapQuestDict)
print(OpenMapQuest.build_elevation_url(r.get_latLng_list()))
print(r.get_latLng_list())
ElevationDict = OpenMapQuest.get_Result(OpenMapQuest.build_elevation_url(r.get_latLng_list()))
class Elevation:
    def __init__(self, info:dict):
        elevations = []
        d = 0
        for i in info['elevationProfile']:
            elevations.append((i['height']))
            #print(i)
        self._elevations = elevations
        #print(self._elevations)

    def get_elevations_list(self) -> list:
        return self._elevations
    
    def display(self):
        for i in range(len(self.get_elevations_list())):
            print(self.get_elevations_list()[i])
    
        


if __name__ == '__main__':
    x = Elevation(ElevationDict)
    x.display()
