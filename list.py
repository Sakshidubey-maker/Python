friends=["sakshi","shiva","radha","gopal"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends[2:4])

# updating values
friends[0]="parwati"
print(friends[0:2])

# list functions

# append add in last element in list
friends.append("rukmani")
print("append: ",friends)

# insert add element or insert element at specific position
friends.insert(2,"sakshi")
print("insert: ",friends)

# sort the element in alphabetical order
friends.sort()
print("sort: ",friends)

# extend function extend or add on the other list set
lucky_numbers=[28,44,24,23,42]
print(lucky_numbers)
lucky_numbers.sort()
print("sort: ",lucky_numbers)
lucky_numbers.reverse()
print("reverse: ",lucky_numbers)
friends.extend(lucky_numbers)  
print("extend: ",friends)
# pop remove last element from list
friends.pop()
print("pop: ",friends)
# search element index position
print("index: ",friends.index("radha"))

# remove delete the specified element from list
friends.remove("sakshi")
print("remove: ",friends)
# clear empty the list
friends.clear()
print("clear: ",friends)




