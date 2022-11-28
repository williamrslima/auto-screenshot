from selenium import webdriver
import chromedriver_autoinstaller
import pyautogui
import json

chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

dataFile = open('data.json')
data = json.load(dataFile)
for site in data['sites']:
    driver.get(site['url'])

    print(site['nome'])
    input("Pressione para continuar ")

    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'screenshots/' + site['nome'] + '.png')

driver.close()