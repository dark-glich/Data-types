# List : ordered - mutable 
list_1 = [1, 4, 2, 5, 3]
print(f"original list : {list_1}")
# .sort is used to arrange list in a asscending order
list_1.sort()
print(f".sort = {list_1}")
# insert x at y position we use .insert(y, x)
list_1.insert(5, 6)
print(f".insert = {list_1}")
# to copy a list .copy is used
list_2 =list_1.copy()
print(f".copy = {list_2}")
# to know where a certain value is
print(f".index of 5 = {list_1.index(5)}")
# list comprehension
list_3 = [x for x in range(6)]
# if statement can also be used in list comprehension
list_4 = [x for x in range (10) if x%2 == 0]
print(f"list comprehension : {list_3}")
# zip(x,y) object makes tuple of the items in the lists
l = ["name", "class", "section"]
s = ["bilal", "9", "A"]
print (f"zip func : {tuple(zip (l, s))}")

