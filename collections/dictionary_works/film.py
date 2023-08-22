movies={"2018":5,"Keralastory":3,"neymar":4,"kgf":5,"arm":4}

# q1) print all movies name
# q2) print top rated movies
# q3) sort movies wrt rating order by desc




print(movies.keys())

print(max(movies,key=lambda k:movies.get(k)))
print(sorted(movies,key=lambda k:movies.get(k)))

mobiles=[
    {"name":"S23ULTRA","brand":"samsung","price":150000,"color":{"white","red","green"},"network":"5g"},
     {"name":"NARZO20","brand":"realme","price":15000,"color":{"black"},"network":"4g"},
       {"name":"note 9 pro","brand":"redmi","price":25000,"color":"black","network":"5g"},
        {"name":"m3pro","brand":"poco","price":15000,"color":"white","network":"5g"},
]