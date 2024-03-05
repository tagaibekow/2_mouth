#1

# student = {'name':'Daiyrbek','age':15, 'color':'black'}
# print(student)

# print(student['age'])

# student['hobby'] = 'Dalnoboi'

# print['color'] = 'white'
# print(student)

# student.pop('hobby')
# print(student)

#set

# num = [123,123,456,876,123]
# num1 = set(num)
# print(num1)

# student = {'Kudbuhon','Nurbolot','Kukushka'}
# students = {'Aslan'}
# student.update(students)
# print(student)

# def intersection_sets(set1, set2):        
#     result_set = set1.intersection(set2)
#     return result_set

# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}

# intersection_set = intersection_sets(set_a, set_b)
# print("Пересечение множеств:", intersection_set)

# def duplicates(a_list):
#     unique = set(a_list)
#     result_list = list(unique)
#     return result_list

# original_list = [1, 2, 3, 2, 4, 5, 6, 4]
# result_list = duplicates(original_list)

# print("Список без повторяющихся элементов:", result_list)

# def is_subset(set1,set2):
#     return all(element in set2 for element in set1)

# set_a = {1,2,3}
# set_b = {1,2,3,4,5}
# result = is_subset(set_a,set_b)
# if result:
#     print('set_a является подмножество set_b.')
# else:
#     print('set_a не является подмножество set_b')



# original_set = frozenset([1,2,3,4,5])

# try:
#     original_set.add(6)
# except AttributeError as e:
#     print(f"Ошибка: {e}")

# def intersection(set1, set2):
#     return set1.intersection(set2)

#Fronzenset

# frozenset1 = frozenset([1, 2, 3, 4, 5])
# frozenset2 = frozenset([3, 4, 5, 6, 7])

# result = intersection(frozenset1, frozenset2)
# print(result)

# def compare_frozensets(set1, set2):
#     if set1 == set2:
#         return "Множества равны"
#     elif set1.issubset(set2):           #является ли множество подмножеством другого
#         return "Первое множество является подмножеством второго"
#     elif set2.issubset(set1):
#         return "Второе множество является подмножеством первого"
#     else:
#         return "Множества не пересекаются"

# # Пример использования
# frozenset1 = frozenset([1, 2, 3, 4, 5])
# frozenset2 = frozenset([3, 4, 5, 6, 7])

# result = compare_frozensets(frozenset1, frozenset2)
# print(result)

# frozen_set = frozenset([1,2,3,4,5])

# list_from_frozenset = list(frozen_set)

# print(frozen_set)
# print(list_from_frozenset)


# frozen_set1 = frozenset([1, 2, 3])
# frozen_set2 = frozenset([3, 4, 5])

# new_frozen_set = frozen_set1.union(frozen_set2)

# print("Первый frozenset:", frozen_set1)
# print("Второй frozenset:", frozen_set2)
# print("Новый frozenset (объединение):", new_frozen_set)

#Доп

# number = [1, 2, 3, 4, 5]
# numbers = [number * 2 for number in number  ]
# print(numbers)


# strings = ["apple", "banana", "cherry", "date"]
# uppercased_strings = [string.upper() for string in strings]
# print(uppercased_strings)


# words = ["apple", "banana", "cherry", "date"]
# first_letters = [word[0] for word in words]
# print(first_letters)

# words = ["apple", "banana", "cherry", "date"]
# word_lengths = [len(word) for word in words]
# print(word_lengths)
