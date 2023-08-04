# intializing hash map
city_map = {}
# OR
city_maps = dict()

cities = ["Calgary", "Vancouver", "Toronto"]

# city_map["Canada"].append(cities)
# # KeyError: 'Canada' - you get this error because no intialization how to fix is below

city_map["Canada"] = []
city_map["Canada"] += cities
{'Canada': ["Calgary", "Vancouver", "Toronto"]}
