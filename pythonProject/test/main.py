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


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import sqlite3

print('Welcome to the IMDb Film Scraper\n'
      'This script will return information on up to 40 films based on the '
      'range of years and ratings you specify, sorted by popularity\n'
      'The films will be stored in a database called films.db\n'
      'Please fill in all the fields:')

while True:
    try:
        startyear = int(input('Start year of your search: '))
    except ValueError:
        print('Please enter a number')
        continue
    if startyear <= 2022 and 1900 <= startyear:
        break
    else:
        print('Please enter a date between 1900 and 2022')

while True:
    try:
        endyear = int(input('End year of your search: '))
    except ValueError:
        print('Please enter a number')
        continue
    if endyear <= 2022 and 1900 <= endyear:
        if endyear >= startyear:
            break
        else:
            print('End year must not be before the start year')
            continue
    else:
        print('Please enter a date between 1900 and 2022')

while True:
    try:
        minrat = float(input('Minimum rating to consider: '))
    except ValueError:
        print('Please enter a number')
        continue
    if minrat <= 10.0 and 1.0 <= minrat:
        break
    else:
        print('Please enter a number between 1.0 and 10.0')

while True:
    try:
        maxrat = float(input('Maximum rating to consider: '))
    except ValueError:
        print('Please enter a number')
        continue
    if maxrat <= 10.0 and 1.0 <= maxrat:
        if maxrat >= minrat:
            break
        else:
            print('Maximum rating must not be lower than minimum rating')
            continue
    else:
        print('Please enter a number between 1.0 and 10.0')


URL = f'https://www.imdb.com/search/title/?title=&title_type=feature&release_date={startyear}-01-01,{endyear}-12-31&user_rating={minrat},{maxrat}&num_votes=1000,&languages=en'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(class_='lister-list')

while True:
    try:
        film_elements = results.find_all(class_='lister-item-content')
        print()
        print('Films that match your specifications:')
        print()
        break
    except AttributeError:
        film_elements = []
        print()
        print('No results found')
        break

loops = 1
films = len(film_elements)
film_id = []
film_title = []
film_year = []
film_genre = []
film_rating = []
film_runtime = []
film_certificate = []

while films > 0:
    for film_element in film_elements:
        film_id.append(loops)
        title_element = film_element.find('a')
        film_title.append(title_element.text.strip())
        year_element = film_element.find(class_='lister-item-year text-muted unbold')
        film_year.append(re.findall('\((\d+)\)', year_element.text.strip()))
        genre_element = film_element.find(class_='genre')
        film_genre.append(genre_element.text.strip())
        rating_element = film_element.find('strong')
        film_rating.append(float(rating_element.text.strip()))
        try:
            runtime_element = film_element.find(class_='runtime')
            film_runtime.append(runtime_element.text.strip())
            pass
        except AttributeError:
            film_runtime.append('N/a')
        try:
            age_element = film_element.find(class_='certificate')
            film_certificate.append(age_element.text.strip())
            pass
        except AttributeError:
            film_certificate.append('N/a')
        films -= 1
        loops += 1
        if loops == 41:
            break

    break

#data cleaning
film_years = []
for i in film_year:
    film_year_new = re.sub('(\(|\)|I| )', '', i)
    film_years.append(film_year_new)

run_time = []
for i in film_runtime:
    run_time_new = re.sub('(min| )', '', i)
    run_time.append(run_time_new)

features = {'film_id':film_id, 'title':film_title, 'year':film_years, 'genre':film_genre, 'rating':film_rating, 'runtime':run_time, 'certificate':film_certificate}
films = pd.DataFrame(features, columns = ['film_id', 'title', 'year','genre', 'rating', 'runtime', 'certificate'])

print(films.to_string(index=False))

conn = sqlite3.connect('films.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS films (film_id int, title text, year int, genre text, rating float, runtime text, certificate text)')
conn.commit()

films.to_sql('films', conn, if_exists='replace', index=False)
conn.commit()
conn.close()