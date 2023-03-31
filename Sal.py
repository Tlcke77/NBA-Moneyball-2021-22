import requests
from bs4 import BeautifulSoup
import csv

url = 'https://hoopshype.com/salaries/players/2021-2022/'

# create a list to store all the data
data = []

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# find the table with the player data
table = soup.find('table', class_='hh-salaries-ranking-table')

# loop through all the rows in the table
for row in table.find_all('tr'):
    # find the player name and salary amount
    cols = row.find_all('td')
    if len(cols) == 4:
        player_name = cols[1].text.strip().split(',')[0]
        salary = cols[2].text.strip().replace('$', '').replace(',', '')
        data.append([player_name, salary])

# save the data to a CSV file
with open('nba_salaries.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Player Name', 'Salary'])
    for row in data:
        writer.writerow(row)
