import requests
from bs4 import BeautifulSoup

URL = "https://www.formula1.com/en/results.html/2021/races.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

drivers_raceresult = []
drivers_fastestlap = []
drivers_pitstopsummary = []
drivers_startinggrid = []
drivers_qualifying = []
drivers_practice3 = []
drivers_practice2 = []
drivers_practice1 = []

races = []

race_links = []  # holds the link to each race


filters = soup.find_all('ul', {'class': 'resultsarchive-filter ResultFilterScrollable'}) # grabs each list of filters (race, filters on drivers, year)

races_html = filters[2]  # grabs the html of the races filter

for race in races_html:
    races.append(race.text.strip())


# finds the table which contains data
results = soup.find('table', {'class': 'resultsarchive-table'})

# finds list of drivers who drove in race
drivers_html = soup.find_all('tr')

# strips HTML from each driver and appends to driver list
for driver in drivers_html:
    driver_firstname = driver.find('span', {'class': 'hide-for-tablet'})
    driver_lastname = driver.find('span', {'class': 'hide-for-mobile'})

    if(driver_firstname != None):
        drivers_raceresult.append(driver_firstname.text + ' ' + driver_lastname.text)
