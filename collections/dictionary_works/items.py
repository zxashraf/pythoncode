items=[
    {"name":"biriyani","price":130,"category":"nonveg"},
    {"name":"dosa","price":70,"category":"veg"},
    {"name":"vefriedrice","price":130,"category":"veg"},
    {"name":"noodles","price":130,"category":"nonveg"},
    {"name":"burger","price":130,"category":"nonveg"},
    ]

# print all items name

# items_name=list(map(lambda i:i.get("name"),items))
# print(items_name)


# name=[i.get("name") for i in items] # list coprihension
# print(name)


# map_price=list(lambda it:it.get("price"),items)
# print(map_price)

# lst_price=[it.get("price") for it in items]


veg_filter=list(filter(lambda it:it.get ("category")=="veg",items))
print(veg_filter)

list_veg=[it.get("name") for it in items if it.get("category")=="veg"]