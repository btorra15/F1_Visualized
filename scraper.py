import requests
from bs4 import BeautifulSoup

URL = "https://www.formula1.com/en/results.html/2021/races/1102/united-states/race-result.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


# finds the table which contains data
results = soup.find('table', {'class': 'resultsarchive-table'})

# finds list of drivers who drove in race
drivers_html = soup.find_all('tr')
drivers = []  # holds list of drivers

# strips HTML from each driver and appends to driver list
for driver in drivers_html:
    driver_firstname = driver.find('span', {'class': 'hide-for-tablet'})
    driver_lastname = driver.find('span', {'class': 'hide-for-mobile'})

    if(driver_firstname != None):
        drivers.append(driver_firstname.text + ' ' + driver_lastname.text)

for i in range(len(drivers)):
    print(drivers[i])
