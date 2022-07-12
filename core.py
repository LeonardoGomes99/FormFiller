from lib2to3.pgen2 import driver
from selenium import webdriver
import random
import time
import json

chromeDriverLocation = 'chromedriver.exe'
driver = webdriver.Chrome(chromeDriverLocation)

def main():
    with open('testes.json') as json_file:
        data = json.load(json_file)
        testName = 'fillForm'
        print(data[testName]['url'])

        #  Caminho Para Percorrer
        for a in data[testName]['url']:
            driver.get(a)
        
        # Carregar Components e preencher [INPUTS, RADIOS, CHECKBOX...ETC]
        for b in data[testName]['components']:
            if(b['input'] > 0):
                fillInputs()
            if(b['radio'] > 0):
                checkRadios()
            if(b['checkbox'] > 0):
                checkCheckbox()
            if(b['selectQnty'] > 0):
                for key, value in b['select'].items():
                    checkSelect(key,value)

            time.sleep(8)
            submitForm()

def generateString():
    first_names=('John','Andy','Joe')
    last_names=('Johnson','Smith','Williams')

    group=" ".join(random.choice(first_names)+" "+random.choice(last_names) for _ in range(3))

    return group

def fillInputs():
    inputs = driver.find_elements_by_xpath('//input[@type="text"]')
    for input in inputs:
        text = generateString()
        input.send_keys(text)

def checkRadios():
    radios = driver.find_elements_by_xpath('//input[@type="radio"]')
    for radio in radios:
        radio.click()

def checkCheckbox():
    checkboxes = driver.find_elements_by_xpath('//input[@type="checkbox"]')
    for checkbox in checkboxes:
        checkbox.click()

def checkSelect(selectName, option):
    print(selectName)
    print(option)
    driver.find_element_by_xpath("//select[@name='"+selectName+"']/option[text()='"+option+"']").click()

def submitForm():
    buttonsSubmit = driver.find_elements_by_xpath('//button[@type="submit"]')
    for buttonSubmit in buttonsSubmit:
        buttonSubmit.click()
        break

if __name__ == "__main__":
    main()

# Pegar Elemento dentro de outro
# driver.FindElements(By.Xpath("//div[@class='tabs']/button[.='Users']"));
