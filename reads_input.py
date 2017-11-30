#Manasi Shingane 12382221 Lab Section 10 12:30- 1:50 
import OpenMapQuest
import implementoutput
import urllib


def input_locations(location_amount)-> list:
    '''
    Prompts the user for as many location inputs as they had specified
    '''
    location_list = []
    for i in range(0, location_amount):
        place = input()
        location_list.append(place)
    return location_list


def desired_outputs(output_amount: int)-> list:
    '''
    Prompts the user for as many desired
    '''
    output_list = []
    for i in range(0,output_amount):
        outputs = input()
        output_list.append(outputs)
    return output_list

def objects_list(outputs: list, info:dict) -> list:
    '''
    adds the appropriate object to the list depending on the input 
    '''
    objects = []
    for i in outputs:
        if i.upper() == 'STEPS':
           objects.append(implementoutput.Steps(info))
        elif i.upper() == 'TOTALDISTANCE':
            objects.append(implementoutput.TotalDistance(info))
        elif i.upper() == 'TOTALTIME':
            objects.append(implementoutput.TotalTime(info))
        elif i.upper() == 'LATLONG':
            objects.append(implementoutput.LatLong(info)) 
        elif i.upper() == 'ELEVATION':
            ElevationDicts = []
            r = implementoutput.LatLong(info)
            for i in range(len(r.get_latLng_reversed())):
                ElevationDicts.append(OpenMapQuest.get_Result(OpenMapQuest.build_elevation_url(r.get_latLng_reversed()[i])))
            objects.append(implementoutput.Elevation(ElevationDicts))
    return objects
        
        
def print_results(objects:list):
    '''
    uses duck typing to display the results
    '''
    for i in objects:
        i.display()

def UI():
    '''
    user interface 
    '''
    try:
        location_amount = int(input())
        MapQuestDict = OpenMapQuest.get_Result(OpenMapQuest.build_search_url(input_locations(location_amount)))
        output_amount = int(input())
        print_results(objects_list(desired_outputs(output_amount),MapQuestDict))

    except KeyError:
        print()
        print('NO ROUTE FOUND')
    except urllib.error.HTTPError :
        print()
        print('MAPQUEST ERROR')
        return
    except urllib.error.URLError:
        print()
        print('MAPQUEST ERROR')
        return
    except:
        while True:
            print('invalid, try again')
            UI()

    else:
        print("Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors")

if __name__ == '__main__':
    UI()
              


    
        
'''
you need to take the input, put what they want in a list, and then use that list
to duck type
'''
