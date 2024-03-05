
#1
# a = "output.txt"
# c = input("Введите текст для сохранение в файл: ")
# with open("output.txt",'w') as file:
#     file.write(c)
#     print(f"Текст успешно сохранен в файл 'output.txt'.")
    
#2
# def count_lines(file_path):
#     with open(file_path,'r') as file:
#         line_count = sum(1 for line in file)
#         print(f'Количество строк в файле {file_path}:{line_count}')
# file_path = 'example.txt'
# count_lines(file_path)

#3
# def search_word(file_path):
#     with open(file_path,'r'):
#         content = file.read()
#         if target_word in content:
#             print(f"Слово '{target_word}' найдено в файле {file_path}.")
#         else:
#             print(f"Слово '{target_word}' не найдено в файле {file_path}.")

# file_path = 'example.txt' 
# target_word = 'qwerty'   
# search_word(file_path, target_word)")





# #5
# def main(about_path, example_path):
#     with open(about_path, 'r')as a:
#         count = a.read()
#     with open(example_path,'w')as b:
#         b.write(count)

#     print(f"ваш файл успешно сохранено из '{about_path}' в '{example_path}'.")
# a_path = "about.txt"
# b_path = "example.txt"


# main(a_path,b_path)

# #6
# def count_words(file_path):
#     with open(file_path,'r')as file:
#         count = file.read()
#         word = count.split()
#         word_count = len(word)
#         print(f"количество слов в файле {file_path}: {word_count}")
          

# file_path = "about.txt"
# count_words(file_path)

# #7

# def main(file_path,new_content):
#     with open(file_path, 'w')as file:
#         file.write(new_content)
#     print(f'содержимое файла "{file_path}" успешно перезаписано. ')

# file_path = 'about.txt'
# new_content ="dfdfdth"
# main(file_path, new_content)
