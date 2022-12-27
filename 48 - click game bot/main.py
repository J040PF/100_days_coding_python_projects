from selenium import webdriver

drive = webdriver.Chrome(executable_path='chromedriver.exe')

c = drive.get('https://www.python.org/')
price = drive.find_elements_by_css_selector('.event-widget time')
for x in price:
    print(x.text)
