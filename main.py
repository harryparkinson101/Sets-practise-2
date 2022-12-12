my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}



#.difference()

#this prints the difference your_set doesnt have 1,2,3, so prints {1,2,3} 

#print(my_set.difference(your_set))

#.discard()

#this finds the value 5 within the set and removes it

#my_set.discard(5)

# prints {1,2,3,4}
#print(my_set)


#.difference_update()

#my_set.difference_update(your_set)

#prints {1,2,3} because 1,2,3 are not in your set and 4,5 get removed so my set is now {1,2,3}
#print(my_set)

#.interscetion()

# this prints the common data in both sets -> {4,5}
#print(my_set.intersection(your_set))

#shorthand

#print(my_set & your_set)

#.isdisjoint()
# This prints False becasue my_set and your_set share some of the same data 
#print(my_set.isdisjoint(your_set))

set1 = {1,2,3}
set2 = {4,5,6}
#this prints True because set1 has none of the same data as set2
#print(set1.isdisjoint(set2))
#.issubset()

list_1 = {4,5}
list_2 = {4,5,6,7,8}
#This prints True becasue the entire of list_1 is a subset of list_2 so issubset -> True
print(list_1.issubset(list_2))

#.issuperset()
#this will print False because list_1 is a subset and list_2 is a superset 
print(list_1.issuperset(list_2))
# this will print True because list 2 is a superset containing the subset list_1
print(list_2.issuperset(list_1))

#.union()
#this will join set1 with set 2 -> {1,2,3,4,5,6} it will remove any duplicates too.
#print(set1.union(set2))

#shorthand way

#print(my_set | your_set)