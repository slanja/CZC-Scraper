import time
import pandas as pd
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

def main():
    # you can run test on my website
    web = "https://www.czc.cz/graficke-karty/produkty"

    # setting up selenium
    options = webdriver.FirefoxOptions()
    options.headless = True

    # update drivers
    driver = webdriver.Firefox(options=options)
    driver.get(web)
    time.sleep(0.2)

    df = pd.DataFrame({
        "id": [],
        "name": [],
        "description": [],
        "price": [],
    })

    cookies = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/button[1]")
    cookies.click()
    time.sleep(2)

    while True:
        try:
            more = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[2]/div/div[11]/button")
            more.click()
            time.sleep(1)
        except:
           break

    products = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[2]/div/div[8]/div/div").text.strip(" produktů")
    print(products)

    time.sleep(1)

    for i in range(int(products)):
        try: id = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[2]/div/div[10]/div/div[1]/div[1]/span")[i].get_attribute("innerHTML")
        except: id = ""

        try: name = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[2]/div/div[10]/div/div[2]/div[1]/h5/a")[i].text
        except: name = ""

        try: description = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[2]/div/div[10]/div/div[2]/div[6]")[i].text
        except: description = ""

        try: price = driver.find_elements(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[2]/div/div[10]/div/div[2]/div[2]/div/div/span/span[2]")[i].text
        except: price = ""

        print(id)
        print(name)
        print(description)
        print(price)
        print(" ")

        df.loc[i] = [id, name, description, price]


    df.to_csv('data.csv', index=False)

    # ID produktu: /html/body/div[2]/div[3]/div[1]/div[2]/div/div[10]/div[i]/div[1]/div/span
    # Nazev produktu: /html/body/div[2]/div[3]/div[1]/div[2]/div/div[10]/div[i]/div[2]/div[1]/h5/a
    # Description: /html/body/div[2]/div[3]/div[1]/div[2]/div/div[10]/div[i]/div[2]/div[6]
    # Cena: /html/body/div[2]/div[3]/div[1]/div[2]/div/div[10]/div[i]/div[2]/div[2]/div/div/span/span[2]

    # Next button: /html/body/div[2]/div[3]/div[1]/div[2]/div/div[11]/button
    # Product number: /html/body/div[2]/div[3]/div[1]/div[2]/div/div[8]/div/div


if __name__ == '__main__':
    main()