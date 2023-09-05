# creating a list
List = ['this','is', 'a', 'list']
print(List)

# creating a multidimentional list
m_list = [['this', 'is'], 'a', 'multidimentional', ['list']]
print(m_list)

# Method	    Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the first item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list

len(List)
List.append(69)
print(List)
List_b = List.copy()
print(List_b)
List_b.clear()
print(List_b)
List.extend(m_list)
print(List)
for item in m_list:
    List.remove(item)
print(List)
List.insert(10,0)
print(List)
List.remove(0)
print(List)
List.reverse()
print(List)
List.sort()   # TypeError: '<' not supported between instances of 'int' and 'str'
