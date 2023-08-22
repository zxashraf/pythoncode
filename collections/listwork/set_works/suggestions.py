allusers=["mohanlal","fahad","dq","nivin","asif"]
dq_friendlist=["mohanlal","fahad","asif"]

suggestions=set(allusers).difference(set(dq_friendlist))
suggestions.remove("dq")
print(suggestions)

# dq=> asif ? mutual friends
mutual_friends=["mohanlal","fahad","vijay","nivin"]
mutual_friends=(set(dq_friendlist).intersection(mutual_friends))
print("mutual_friends are",mutual_friends)