import geopy.distance, collections


def is_nearby(hotel1, hotel2):
    """
    returns true if distance between cordinates is upto 500 meters
    """
    coords_1 = (hotel1['location']['lat'], hotel1['location']['lng'])
    coords_2 = (hotel2['location']['lat'], hotel2['location']['lng'])

    distance = geopy.distance.vincenty(coords_1, coords_2).km
    distance_meter = distance*1000
    return True if (distance_meter <= 500) else False


def full_match(hotel1, hotel2):
    """
    Checks if two hotels has exactly same name and location
    """
    return (hotel1['name'].lower() == hotel2['name'].lower()
            and hotel1['location']['lat'] == hotel2['location']['lat']
            and hotel1['location']['lng'] == hotel2['location']['lng'])


def literal_check(name):
    """
    returns list of words from the name by eliminating the common business words
    """
    business_key = ('oyo', 'hotel')
    name_split = name.strip().lower().split()
    generic_words = [i for i in name_split if i not in business_key] 
    return generic_words


def partial_match(hotel1, hotel2):
    """
    checks if hotels name are matching after eliminating common business words
    """
    hotel1_literals = literal_check(hotel1['name'])
    hotel2_literals = literal_check(hotel2['name'])
    return (collections.Counter(hotel1_literals) ==
            collections.Counter(hotel2_literals))
