import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3

#print('Welcome to the IMDb Film Web Scraper (Please fill in all the fields)')

while True:
    try:
        startyear = int(2015)
        # startyear = int(input('Start year of your search: '))
    except ValueError:
        print('Please enter a number')
        continue
    if startyear <= 2022 and 1900 <= startyear:
        break
    else:
        print('Please enter a date between 1900 and 2022')

while True:
    try:
        endyear = int(2020)
        # endyear = int(input('End year of your search: '))
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
        minrat = float(5)
        # minrat = float(input('Minimum rating to consider: '))
    except ValueError:
        print('Please enter a number')
        continue
    if minrat <= 10.0 and 1.0 <= minrat:
        break
    else:
        print('Please enter a number between 1.0 and 10.0')

while True:
    try:
        maxrat = float(10)
        # maxrat = float(input('Maximum rating to consider: '))
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
        break
    except AttributeError:
        film_elements = []
        print('No results found')
        break

loops = 1
films_len = len(film_elements)
film_id = []
film_title = []
film_year = []
film_genre = []
film_rating = []
film_runtime = []
film_certificate = []
while films_len > 0:
    for film_element in film_elements:
        film_id.append(f'{loops}')
        title_element = film_element.find('a')
        film_title.append(f'{title_element.text.strip()}')
        year_element = film_element.find(class_='lister-item-year text-muted unbold')
        film_year.append(f'{year_element.text.strip()}')
        genre_element = film_element.find(class_='genre')
        film_genre.append(f'{genre_element.text.strip()}')
        rating_element = film_element.find('strong')
        film_rating.append(f'{rating_element.text.strip()}')
        try:
            runtime_element = film_element.find(class_='runtime')
            film_runtime.append(f'{runtime_element.text.strip()}')
            pass
        except AttributeError:
            film_runtime.append('N/a')
        try:
            age_element = film_element.find(class_='certificate')
            film_certificate.append(f'{age_element.text.strip()}')
            pass
        except AttributeError:
            film_certificate.append('N/a')
        films_len -= 1
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

#github- want it on new repository
#https://datatofish.com/pandas-dataframe-to-sql/
#change data type of number columns so sql recognises them as integers

features = {'Film_id':film_id, 'Title':film_title, 'Year':film_years, 'Genre':film_genre, 'Rating':film_rating, 'Runtime (minutes)':run_time, 'Certificate':film_certificate}
films = pd.DataFrame(features, columns = ['Film_id', 'Title', 'Year','Genre', 'Rating', 'Runtime (minutes)', 'Certificate'])

conn = sqlite3.connect('films.db')
films.to_sql('films', conn, if_exists='replace', index=False)
c = conn.cursor()

c.execute('''SELECT * FROM films where Year >2018''')
#try some sums here to see if they can sum even though they are registered as text
conn.commit()

for row in c.fetchall():
    print(row)

conn.close()