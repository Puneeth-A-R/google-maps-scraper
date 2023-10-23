import string
import random
import helpers
from sys import exit
from time import sleep
from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
# from inspect import currentframe, getframeinfo


class business:
    """Getter method."""
    @property
    def info(self):
        return (
            self.business_name,
            self.url,
            self.phone,
            self.address,
            self.website)
    """Setter method."""
    @info.setter
    def info(self, business_name, url,
             phone="", address="", website=""):
        self.business_name = business_name
        self.url = url
        self.phone = phone
        self.address = address
        self.website = website


def fetch_reviews(driver):
    """Fetch reviews from right panel, below the big bold business name."""
    try:
        exists = driver.find_element(
            By.XPATH,
            value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/c-wiz[1]/div[2]/div[1]/div/div[1]/div[1]")
        return (exists.text)
    except BaseException:
        return (colored("ERROR: Unable to fetch review status.","light_red"))


def fetch_reviews_qty(driver, i):
    """Fetch number of reviews for a given business from right panel, next to stars."""
    try:
        qty = driver.find_element(By.XPATH, value=f"/html/body/c-wiz/div/div[3]/div/div/div[1]/div[3]/div[3]/c-wiz/div/div/div[1]/c-wiz/div/div[{i}]/div[1]/div/div/div/div[2]/div[2]/div[1]/div[2]")
        return(int(qty.get_attribute("aria-label").removesuffix(" reviews").replace(",", "")))
    except:
        return(colored("NOTE: Unable to fetch No. of reviews", "light_red"))

def fetch_latest_review(driver, i):
    helpers.LOG("ERROR", "t1", driver)
    helpers.LOG("WARNING", "t2")
    helpers.LOG("INFO", "t3")
    try:
        reviews_panel = driver.find_element(By.XPATH, value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/div[3]/div/div[1]/div/div/span/button[3]")
        if reviews_panel.get_attribute("aria-controls") == "reviews-panel":
            reviews_panel.click()
        else:
            try:
                reviews_panel = driver.find_element(By.XPATH, value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/div[3]/div/div[1]/div/div/span/button[2]")
                if reviews_panel.get_attribute("aria-controls") == "reviews-panel":
                    reviews_panel.click()
            except:
                driver.save_screenshot(f"screenshots2/new_panel{i}.png")
                return(colored("ERROR: Unable to locate reviews panel.", "light_red"))
        #return(colored("SUCCESS", "light_green"))
    except:
        driver.save_screenshot(f"screenshots2/new_panel{i}.png")
        return(colored("ERROR: Unable to locate reviews panel.", "light_red"))

    try:
        newest = driver.find_element(By.XPATH, value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/div[3]/div/div[4]/span/c-wiz/div[2]/div/g-scrolling-carousel/div[1]/div/div/div[2]")
        newest.click()
        #return(colored("SUCCESS: Found the `new reviews` button.", "light_green"))
    except:
        try:
            newest = driver.find_element(By.XPATH, value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/div[3]/div/div[3]/span/c-wiz/div[2]/div/g-scrolling-carousel/div[1]/div/div/div[2]")
            newest.click()
            #return(colored("SUCCESS: Found the `new reviews` button.", "light_green"))
        except:
            pass
            #driver.save_screenshot(f"screenshots2/pic{i}.png")
            #return(colored("ERROR: Unable to find `new reviews` button.", "light_red"))

    try:
        latest_review_age = driver.find_element(By.XPATH, value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/div[3]/div/div[4]/span/c-wiz/div[2]/div/div[4]/div[1]/div[1]/div[2]/span")
        return(latest_review_age.text)
    except:
        try:
            latest_review_age = driver.find_element(By.XPATH, value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/div[3]/div/div[3]/span/c-wiz/div[2]/div/div[4]/div[1]/div[1]/div[2]/span")
            return(latest_review_age.text)
        except:
            try:
                latest_review_age = driver.find_element(By.XPATH, value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/div[3]/div/div[3]/span/c-wiz/div[2]/div/div[2]/div/div[1]/div[2]/span")
                return(latest_review_age.text)
            except:
                try:
                    latest_review_age = driver.find_element(By.XPATH, value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/div[3]/div/div[4]/span/c-wiz/div[2]/div/div[2]/div/div[1]/div[2]/span")
                    return(latest_review_age.text)
                except:
                    driver.save_screenshot(f"screenshots2/pic{i}.png")
                    return(colored("ERROR: Unable to fetch age of latest review", "light_red"))


def fetch_name(driver):
    """Fetch business name from right panel heading."""
    try:
        name = driver.find_element(
            By.XPATH,
            value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/c-wiz[1]/div[1]/c-wiz/div")
        return ("\n\n" + name.text)
    except BaseException:
        res = ''.join(
            random.choices(
                string.ascii_lowercase +
                string.digits,
                k=10))
        driver.save_screenshot(f"screenshots/{str(res)}.png")
        print(f"Screenshot saved as {res}")
        return (colored("ERROR: Unable to fetch business name.", "light_red"))


def fetch_phone(driver):
    """Fetch phone number from right panel details."""
    try:
        phone = driver.find_element(
            By.XPATH,
            value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/div[3]/div/div[2]/span/div[2]/div/div/div[2]/a/div[2]")
        return (phone.text)
    except BaseException:
        try:
            phone = driver.find_element(
                By.XPATH,
                value="/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/div[3]/div/div[2]/span/div[2]/div/div/div[1]/a/div[2]")
            return (phone.text)
        except BaseException:
            res = ''.join(
                random.choices(
                    string.ascii_lowercase +
                    string.digits,
                    k=10))
            driver.save_screenshot(f"screenshots/{str(res)}.png")
            print(f"Screenshot saved as {res}")
        return (colored("NOTE: Phone number doesn't exist.", "light_yellow"))


def fetch_address(driver):
    """Fetch address from the list of details in the right panel."""
    it = 6
    while True:
        try:
            address = driver.find_element(By.XPATH, value=f"/html/body/c-wiz/div/div[3]/div/div/div[2]/div[3]/div[1]/c-wiz/div/c-wiz/div/div/div[3]/div[3]/div/div[2]/span/div[2]/div/div/div[{it}]/div/a/div/div[2]/span")
            return (address.text)
        except BaseException:
            it -= 1
            if it == 0:
                break
    res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    driver.save_screenshot(f"screenshots/{str(res)}.png")
    print(f"Screenshot saved as {res}")
    return (colored("ERROR: Unable to fetch business address.", "light_red"))


def fetch_website(driver, i):
    try:
        """Fetch website from left panel button."""
        website = driver.find_element(By.XPATH, value=f"/html/body/c-wiz/div/div[3]/div/div/div[1]/div[3]/div[3]/c-wiz/div/div/div[1]/c-wiz/div/div[{i}]/div[2]/div/div/div/div/div/div[1]/a")
        return (website.get_attribute("href"))
    except BaseException:
        try:
            website = driver.find_element(By.XPATH, value=f"/html/body/c-wiz/div/div[3]/div/div/div[1]/div[3]/div[3]/c-wiz/div/div/div[1]/c-wiz/div/div[{i}]/div[2]/div/div/div/div/div/div[2]/a")
            return (website.get_attribute("href"))
        except BaseException:
            res = ''.join(
                random.choices(
                    string.ascii_lowercase +
                    string.digits,
                    k=10))
            driver.save_screenshot(f"screenshots/{str(res)}.png")
            print(f"Screenshot saved as {res}.png")
            return (colored("NOTE: Doesn't have a website.", "light_yellow"))


def main():
    try:
        driver = initDriver()
        print(type(driver))
        try:
            driver.get("https://www.google.com/localservices/prolist?g2lbs=ANTchaPeyoFcguuMKJ60Tkhs80p-baOCW0qyJ8z2ONLddkKg3PknsjzJDCErnL0qQWhSOWFihdU1Z9RTsK44JBpVQyt69wnFJ0jM0jhvo-Jcop8JCTyRAsWUDApFUXMreo3Vc7PFFp3L&hl=en-IN&gl=in&ssta=1&q=tennessee%20gyms&oq=tennessee%20gyms&slp=MgA6HENoTUl5SmppaHFudWdRTVZnVGFEQXgzZVVBeGdSAggCYACSAa0CCg0vZy8xMWd4c2c0MGRiCg0vZy8xMWYxMm5qNjVzCg0vZy8xMWI3ZjM3ejFzCg0vZy8xMWdqa3c5NHh4Cg0vZy8xMWI2bndwNTZ2Cg0vZy8xMXI2emprZmp0CgsvZy8xdGgwYzU0agoML2cvMTJobGw5MGdiCgwvZy8xcHR5bmoycjUKDS9nLzExYjZucV9oYnoKDS9nLzExYjZma2QwdjkKDC9nLzExX3FjYmN3OQoML2cvMXE1Ym15MDQxCg0vZy8xMWg4YmhybnpnCg0vZy8xMWRkdDQyN21tCgwvZy8xMmhwX3c1eHMKCy9nLzF0a3M3MTE0CgwvZy8xcTY5cXJsMTcKDS9nLzExYnR4a3gyeGMKDC9nLzFoaG1mbjRqeRIEEgIIARIECgIIAZoBBgoCFxkQAA%3D%3D&src=2&serdesk=1&sa=X&ved=2ahUKEwi0ldyGqe6BAxVyTmwGHXBDDhMQjGp6BAgTEAE&scp=CghnY2lkOmd5bRJQEhIJA8-XniNLYYgRVpGBpcEgPgMaEgkLNjLkhLXqVBFCt95Dkrk7HCIOVGVubmVzc2VlLCBVU0EqFA13-NkUFXG2K8odVqjcFSX4q1XPMAAaBGd5bXMiDnRlbm5lc3NlZSBneW1zKgNHeW0%3D")
        except BaseException:
            exit(colored("ERROR: Unable to get web page.", "light_red"))
        title = driver.title
        print(title)
        driver.implicitly_wait(5.5)
        first_only = True
        pages = 1
        no_of_businesses_fetched = 0
        while True:
            for i in range(1, 40, 2):
                try:
                    business = driver.find_element(By.XPATH, value=f"/html/body/c-wiz/div/div[3]/div/div/div[1]/div[3]/div[3]/c-wiz/div/div/div[1]/c-wiz/div/div[{i}]/div[1]/div/div")
                except BaseException:
                    print(colored("End of business listings.", "light_yellow"))
                    print(
                        colored(
                            f"No. of pages scanned: {pages}, No. of businesses fetched: {no_of_businesses_fetched}",
                            "light_green"))
                    return
                business.click()
                sleep(1.25)
                print(fetch_name(driver))
                #print(driver.current_url)
                #print(fetch_phone(driver))
                #print(fetch_address(driver))
                #print(fetch_website(driver, i))
                #print(fetch_reviews(driver))
                #print(fetch_reviews_qty(driver, i))
                print(fetch_latest_review(driver, i))
                no_of_businesses_fetched += 1
            """Fetching the `next` button in the first page."""
            if first_only:
                try:
                    first_next = driver.find_element(
                        By.XPATH,
                        value="/html/body/c-wiz/div/div[3]/div/div/div[1]/div[3]/div[3]/c-wiz/div/div/div[2]/div/div/button")
                    first_only = False
                    first_next.click()
                    sleep(3)
                except BaseException:
                    print(colored("ERROR: Button not found", "light_red"))
                    print(
                        colored(
                            f"No. of pages scanned: {pages}, No. of businesses fetched: {no_of_businesses_fetched}",
                            "light_green"))
                    driver.quit()
            # Fetching the `next` button in all subsequent pages.
            else:
                try:
                    next = driver.find_element(
                        By.XPATH,
                        value="/html/body/c-wiz/div/div[3]/div/div/div[1]/div[3]/div[3]/c-wiz/div/div/div[2]/div[2]/div/button")
                    next.click()
                    sleep(3)
                except BaseException:
                    print(
                        colored(
                            "SUCCESS: Reached the end of listings",
                            "light_green"))
                    print(
                        colored(
                            f"No. of pages scanned: {pages}, No. of businesses fetched: {no_of_businesses_fetched}",
                            "light_green"))
                    driver.quit()
                    return
            pages += 1
    except KeyboardInterrupt:
        pause_execution()


def initDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    """`--disable-dev-shm-usage` flag is used inside docker container to make
    partition bigger for memory.

    See: https://stackoverflow.com/questions/67294395/selenium-docker-crashes-on-windows-unknown-error-devtoolsactiveport-file-doesn
    """
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.set_window_position(1920, 0)
    return driver


if __name__ == "__main__":
    main()
