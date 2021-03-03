from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup
import time
import csv

browser = webdriver.Chrome(executable_path="C://ProgramData/chromedriver.exe")
browser.get("https://exoplanets.nasa.gov/discovery/exoplanet-catalog/")

time.sleep(10)

def scrape():
  headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
  planet_data = []

  for i in range(428):
    soup = BeautifulSoup(browser.page_source, "html.parser")

    for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
      li_tags = ul_tag.find_all("li")
      temp = []

      for index, li_tag in enumerate(li_tags):
        if index==0:
          temp.append(li_tag.find_all("a")[0].contents[0])

        else:
          try:
            temp.append(li_tag.contents[0])
          except:
            temp.append("")

      planet_data.append(temp)

    xpath = '//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a'
    WebDriverWait(browser, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))
    browser.find_element_by_xpath(xpath).click()
  
  with open("data.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)

scrape()