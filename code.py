# numbers = [2, 3, 5, 6, 1, 4]
# numbers.append(10) # adding value to the list
# numbers.insert(1, 34) # adding value to list with index (x, 0)
# numbers.remove(3) # removing value
# numbers.clear() # empty list
# numbers.pop() # removes last value
#
#
# numbers.sort() # sorting values in the list
# numbers.reverse() # sorting - descending order
# numbers2 = numbers.copy() # creating another independent copy of the list (adding value to the list will not affect this copy)
#
# print(numbers.index(1)) # prints index od first occurrence of value
# print(50 in numbers) # prints T/F if 50 is in the list
# print(numbers.count(5)) # prints number of ' 5 ' values inside
# print(numbers)

numbers = [5, 6, 4, 2, 4, 10, 3]
uniques = []


for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


