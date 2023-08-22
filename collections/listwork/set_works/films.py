movies=[
    {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
    {"language":"malayalam","name":"aadujeevitham","rating":5,"year":2023,"genres":["fiction","drama"]},
    {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
    {"language":"malayalam","name":"sunny","rating":4,"year":2023,"genres":["drama","thriller"]},
    {"language":"malayalam","name":"12thy man","rating":3,"year":2022,"genres":["drama","thriller"]},
    {"language":"tamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
    {"language":"tamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
    {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
    {"language":"telungu","name":"kgf","rating":5,"year":2018,"genres":["action","romance","thriller"]},
]

# for movie in movies:
#     print(movie.get("name") and movie.get("genres")[0]=="mystery")

# movie_names=[m.get("name") for m in movies]
# print(movie_names)

# for m in movies:
#     if "mystery" in m.get("genres"):
#         print(m.get("name"))

print(max(movies,key=lambda k:k.get("rating")))


movie_names=[m.get("names") for m in movies]
genres_movies=[m.get("nmaes") for m in movies if "mystery" in m.get ("genres")]
top_rated_movies=max(movies,key=lambda m:m.get("rating"))
year_filter=[m.get("name") for m in movies if m.get ("year")==2023]
print(year_filter)


# sort movies wrt rating order by desc

movie_sort=sorted(movies,reverse=True,key=lambda m:m.get("rating"))
print(movie_sort)

# print malayalam movie names

malayalam_movie=[m.get("name")for m in movies if m.get("language")=="malayalam"]
print(malayalam_movie)