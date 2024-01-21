lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Fred", "Tamara", "Hughdahlia", "Audra", "Nikhil"] 

print(friends[0])

# friends.extend(lucky_numbers)
# print(friends)

#add individual elements to a list, always goes the end of the list
friends.append("Creed")
print(friends)

#insert function| takes TWO parameter, 1st: index position, 2nd: the name
friends.insert(0, "Aaron")
print(friends)

#remove function
friends.remove("Aaron")
print(friends)

#clear function, remove every item in the list
# lucky_numbers.clear()
# print(lucky_numbers)

#pop function
friends.pop()
print(friends)

#find the index position of a list
print(friends.index("Nikhil"))

#sort function
friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

#reverse function order
lucky_numbers.reverse()
print(lucky_numbers)

#count function
friends.append("Nikhil")
print(friends)

print(friends.count("Nikhil"))

#copy function
friends2 = friends.copy()
print(friends)

friends2.append("Sam")
print(friends2)
