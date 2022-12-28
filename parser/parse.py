import cloudscraper  # A simple Python module to bypass Cloudflare's anti-bot page (also known as "I'm Under Attack Mode", or IUAM), implemented with Requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.remote.webelement import WebElement


from parser.models import Forecast

BASE_URL = "https://pogoda.meta.ua/Kyivska/Kyivskiy/Kyiv/"
SCRAPER = cloudscraper.create_scraper(
    delay=10,
    browser={
        "custom": "ScraperBot/1.0",
    },
)


def parse_day(day: WebElement) -> tuple:
    """
    Function for parse detail day info
    :param day:
    """

    day.click()

    date = day.get_property("id")
    detail_day = SCRAPER.get(f"{BASE_URL}/{date}/ajax").content

    soup = BeautifulSoup(detail_day, "html.parser")
    temperature = soup.select_one(".city__main-temp").text

    description = ", ".join(
        [el.text for el in soup.select(".city__main-image-descr > span")]
    ).replace(".", "")

    return date, temperature, description


def parse_weather() -> None:
    """
    This function scrape 6 days from pogoda.meta.ua, Kyiv city
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Remote(
        command_executor='http://192.168.112.3:4444/wd/hub',
        options=options
    )

    # driver = webdriver.Chrome() #for local testing

    driver.get(BASE_URL)

    days = driver.find_elements(By.CLASS_NAME, "city__day")

    for day in days:

        date, temperature, description = parse_day(day)

        if Forecast.objects.filter(day=date).exists(): # checking for an existing day

            day_to_update = Forecast.objects.get(day=date)
            day_to_update.description = description
            day_to_update.temperature = temperature
            day_to_update.save()

        else:
            Forecast.objects.create(
                day=date, temperature=temperature, description=description
            )
    driver.close()
