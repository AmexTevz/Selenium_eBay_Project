from selenium.webdriver.common.by import By


class Results:

    item = input("What to search for?: ") or 'computer'
    number_of_entries = int(input('how many?: ') or 10)

    product_titles = (By.CSS_SELECTOR, '.s-item__title')
    product_price = (By.CSS_SELECTOR, '.s-item__price')
    product_link = (By.CSS_SELECTOR, 'a.s-item__link')


    def __init__(self, driver):
        self.driver = driver

    def titles(self):
        titles = [i.text for i in self.driver.find_elements(*Results.product_titles)]
        return titles[1:self.number_of_entries+1]

    def prices(self):
        prices = [i.text[1:].replace(',','') for i in self.driver.find_elements(*Results.product_price)]
        return prices[1:self.number_of_entries+1]

    def links(self):
        link = [i.get_attribute('href') for i in self.driver.find_elements(*Results.product_link)]
        return link[1:self.number_of_entries+1]

