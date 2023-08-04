# intializing hash map
from collections import defaultdict
city_map = {}
# OR
city_maps = dict()

cities = ["Calgary", "Vancouver", "Toronto"]

# city_map["Canada"].append(cities)
# # KeyError: 'Canada' - you get this error because no intialization how to fix is below

city_map["Canada"] = []
city_map["Canada"] += cities
{'Canada': ["Calgary", "Vancouver", "Toronto"]}

# other solution
city_map = defaultdict(list)
cities = ["Calgary", "Vancouver", "Toronto"]
city_map["Canada"] += cities

# retrieving data
# returns all keys in form of list
hashmap.keys()
# return values in form of list
hashmap.values()
# return list of all key value pairs as tuples
hashmap.items()

# example:
city_list = city_map.values()
# will return all cities
