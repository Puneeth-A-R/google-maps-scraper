import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from inspect import currentframe, getframeinfo


class business:
    """Getter method"""
    @property
    def info(self):
        return (
            self.business_name,
            self.url,
            self.phone,
            self.address,
            self.website)
    """Setter method"""
    @info.setter
    def info(self, business_name, url,
             phone="", address="", website=""):
        self.business_name = business_name
        self.url = url
        self.phone = phone
        self.address = address
        self.website = website


def main():
    driver = initDriver()
    driver.get("https://www.google.com/localservices/prolist?g2lbs=ANTchaPeyoFcguuMKJ60Tkhs80p-baOCW0qyJ8z2ONLddkKg3PknsjzJDCErnL0qQWhSOWFihdU1Z9RTsK44JBpVQyt69wnFJ0jM0jhvo-Jcop8JCTyRAsWUDApFUXMreo3Vc7PFFp3L&hl=en-IN&gl=in&ssta=1&q=tennessee%20gyms&oq=tennessee%20gyms&slp=MgA6HENoTUl5SmppaHFudWdRTVZnVGFEQXgzZVVBeGdSAggCYACSAa0CCg0vZy8xMWd4c2c0MGRiCg0vZy8xMWYxMm5qNjVzCg0vZy8xMWI3ZjM3ejFzCg0vZy8xMWdqa3c5NHh4Cg0vZy8xMWI2bndwNTZ2Cg0vZy8xMXI2emprZmp0CgsvZy8xdGgwYzU0agoML2cvMTJobGw5MGdiCgwvZy8xcHR5bmoycjUKDS9nLzExYjZucV9oYnoKDS9nLzExYjZma2QwdjkKDC9nLzExX3FjYmN3OQoML2cvMXE1Ym15MDQxCg0vZy8xMWg4YmhybnpnCg0vZy8xMWRkdDQyN21tCgwvZy8xMmhwX3c1eHMKCy9nLzF0a3M3MTE0CgwvZy8xcTY5cXJsMTcKDS9nLzExYnR4a3gyeGMKDC9nLzFoaG1mbjRqeRIEEgIIARIECgIIAZoBBgoCFxkQAA%3D%3D&src=2&serdesk=1&sa=X&ved=2ahUKEwi0ldyGqe6BAxVyTmwGHXBDDhMQjGp6BAgTEAE&scp=CghnY2lkOmd5bRJQEhIJA8-XniNLYYgRVpGBpcEgPgMaEgkLNjLkhLXqVBFCt95Dkrk7HCIOVGVubmVzc2VlLCBVU0EqFA13-NkUFXG2K8odVqjcFSX4q1XPMAAaBGd5bXMiDnRlbm5lc3NlZSBneW1zKgNHeW0%3D")
    title = driver.title
    print(title)
    driver.implicitly_wait(5.5)
    driver.save_screenshot("screenshots/before.png")
    business = driver.find_element(
        By.XPATH,
        value='/html/body/c-wiz/div/div[3]/div/div/div[1]/div[3]/div[3]/c-wiz/div/div/div[1]/c-wiz/div/div[1]/div[1]/div/div')
    business.click()
    driver.implicitly_wait(10.5)
    business_info = driver.find_element(
        By.XPATH,
        value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]")
    js_code = "arguments[0].scrollIntoView();"
    driver.execute_script(js_code, business_info)
    business_info.screenshot('screenshots/element.png')
    phone = driver.find_element(
        By.XPATH,
        value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/div[3]/div/div[2]/span/div[2]/div/div/div[2]/a/div[2]")
    print(phone.text)
    name = driver.find_element(
        By.XPATH,
        value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/c-wiz[1]/div[1]/c-wiz/div")
    print(name.text)
    address = driver.find_element(
        By.XPATH,
        value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/div[3]/div/div[2]/span/div[2]/div/div/div[4]/div/a/div/div[2]/span")
    print(address.text)
    share = driver.find_element(
        By.XPATH,
        value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/c-wiz[2]/div/div/div[3]/div/div/a/div/div/button")
    share.click()
    driver.implicitly_wait(5.5)
    try:
        url = driver.find_element(
            By.XPATH, value='//*[@id="yDmH0d"]/div[5]/div/div[2]/span/div/div/div[4]/a')
        print(url.txt)
    except BaseException as exp:
        print(type(exp))
        print("URL not yet generated")
    print(driver.current_url)
    driver.save_screenshot("screenshots/after.png")
    try:
        website = driver.find_element(
            By.XPATH,
            value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/c-wiz[2]/div/div/div[1]/a")
        print(website.text)
    except BaseException:
        print("Doesn't have a website!")
    print(getframeinfo(currentframe()).lineno)

    driver.quit()


def initDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    """`--disable-dev-shm-usage` flag is used inside docker container to make
    partition bigger for memory.

    See: https://stackoverflow.com/questions/67294395/selenium-docker-crashes-on-windows-unknown-error-devtoolsactiveport-file-doesn
    """
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.set_window_position(1920, 0)
    return driver


if __name__ == "__main__":
    main()

# attrs1 = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', share)
# print(attrs1)
# attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', phone)
# print(attrs)
