# ===========================================
# Lists in python - Dynamic Arrays Equivalent
# ===========================================

# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)

mixed_list = [1, "Hello", 3.14, True]
print("Mixed List:", mixed_list)

empty_list = []
print("Empty List:", empty_list)

# Accessing elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])
print("Slicing (first three elements):", my_list[:3])

# updating elements
my_list[0] = 10
print("Updated List:", my_list)

# Adding elements
my_list.append(6)
print("After appending 6:", my_list)

my_list.insert(1, 100)
print("After inserting 100 at index 1:", my_list)

my_list.insert(-1, 100)
print("After inserting 100 at index -1:", my_list)

# Removing elements
my_list.remove(100)
print("After removing 100:", my_list)

popped_element = my_list.pop()
print("Last element popped:", popped_element)

print("After popping last element:", my_list)
my_list.pop(2)
print("After popping element at index 2:", my_list)

# List length

print("Length of the list:", len(my_list))
print("Max element in the list:", max(my_list))
print("Min element in the list:", min(my_list))

my_list.sort()
print("Sorted List:", my_list)

my_list.reverse()
print("Reversed List:", my_list)

# Iterating over a list
print("Iterating with values")
for element in my_list:
    print("Element:", element)

print("Iterating with index")
for index, element in enumerate(my_list):
    print(index, element)

# List Comprehension

squares = [x*x for x in range(3)]
print("List of Squares :" , squares)

even_list = [x for x in range(10) if x % 2 == 0]
print("Even numbers from 0 to 9:", even_list)

# Copy list 
copied_list = my_list.copy()
print("Copied List:", copied_list)

copied_list = my_list[:]
print("Copied List using slicing:", copied_list)


