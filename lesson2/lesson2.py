#1 Take second element for sort
def takeSecond(elem):
    return elem[1]

# list of lists
list_orig = [[1, 3, 3, 4], [2, 1, 3, 5], [4, 0, 1, 7], [5, 2, 1, 0], [0, 4, 8, 3]]

# sort list with key
list_orig.sort(key=takeSecond)

# print list
print('#1 Sorted list:', list_orig)

#2 Create a dictionary
dict_of_lists = {}
 
#add keys to dictionary
for elem in list_orig:
    sec_el = elem[1]
    dict_of_lists[sec_el] = 0
# check and remove the second elements in the list
    if elem[1] in elem:
        elem.pop(1)
# add the others of the elements (first, third, fourth)
        dict_of_lists[sec_el] = elem[:]

# print dictionary    
print('#2 Dictionary:', dict_of_lists)

#3 Sorts the values ​​of the dictionary
for key in dict_of_lists:
    dict_of_lists[key].sort(reverse=True)
# print dictionary 
print('#3 Dictionary in descending order:', dict_of_lists)
# print(sorted_dict)

#4 Gets a set of all values ​​(sorted lists) of the received dictionary;
# create an empty set
set_of_values = set()

# gets all dictionary values
for lists in dict_of_lists.values():
    for values in lists:
# add all values ​​in a set      
        set_of_values.add(values)

#print a set         
print('#4 Set of all values:', set_of_values)

#5 Converts set to string
# create an empty string
string = ''
# add all values ​​in a string
for values in set_of_values:
    string += str(values)
# separate the values ​in a string
    str_of_values = ' '.join(string)
#print a string    
print('#5 String:', str_of_values)