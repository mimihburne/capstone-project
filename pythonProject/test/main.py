def count_hobby_words(hobbies, word):
    counter = 0
    for hobby in hobbies:
        if word in hobby.split():
            counter += 1
    return counter

#print(count_hobby_words(['Tennis', 'Table Tennis'], 'Tennis'))

# def find_unique_numbers(numbers):
#     for i in numbers:
#         if numbers.count(i) >=2:
#             while (numbers.count(i)):
#                 numbers.remove(i)
#     return numbers

# def find_unique_numbers(numbers):
#     returned = []
#     for i in numbers:
#         if numbers.count(i) == 1:
#             returned.append(i)
#     return returned
# from collections import Counter
# def find_unique_numbers(numbers):
#     returned = []
#     newval = Counter(numbers)
#     print(newval)
#     for i in numbers:
#         if newval[i] == 1:
#             returned.append(i)
#     return returned
#
#
# if __name__ == "__main__":
#     print(find_unique_numbers([1, 2, 1, 3]))
#
# number_list1=[1,2,3,4]
#
# def get_even_numbers(number_list):
#     evens = []
#     for i in number_list:
#         if i % 2 == 0:
#             evens.append(i)
#     return evens
# print(get_even_numbers(number_list1))
import re

string = '(2019)'
new = re.sub('(\(|\))', '', string)
print(new)
