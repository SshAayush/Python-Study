# #Nesting dictonary inside distonary
# travel_log ={
#     "France" : {"cities_visited":["Paris","Lille","Dijon"], "total_visit":12},
#     "germany" :{"cities_visited":["Berlin","Hamburg","Stuttgart"], "total_visit":13},
# }

#nesting dictoranry inside a list

travel_log = [
{
    "country" : "France",
    "cities_visited":["Paris","Lille","Dijon"] ,
    "total_visit": 12,
},
{
    "country" : "Germany",
    "cities_visited": ["Berlin","Hamburg","stuttgart"],
    "totao_visited": 13,
}
]
def add_new_country(country_visited ,times_visited,cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["total_visit"] = times_visited
    new_country["cities_visited"] = cities_visited
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
