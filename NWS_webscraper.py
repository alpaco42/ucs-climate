import selenium
from selenium import webdriver
from multiprocessing import Pool
import pandas as pd
from selenium.webdriver.common.by import By

DOWN = webdriver.common.keys.Keys.ARROW_DOWN

TEST_WEATHER_WARNINGS = list({
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.319609f0d7192e3dd779ae5192d64460f6e9fe18.001.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.319609f0d7192e3dd779ae5192d64460f6e9fe18.001.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.319609f0d7192e3dd779ae5192d64460f6e9fe18.002.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.319609f0d7192e3dd779ae5192d64460f6e9fe18.003.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.417f4e8e65ff59a607507df5116223c16451f79e.001.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.417f4e8e65ff59a607507df5116223c16451f79e.001.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.417f4e8e65ff59a607507df5116223c16451f79e.001.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.417f4e8e65ff59a607507df5116223c16451f79e.001.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.417f4e8e65ff59a607507df5116223c16451f79e.001.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.417f4e8e65ff59a607507df5116223c16451f79e.001.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.60bca550da65b9b1dd3701bfd9fc133ca4de8c73.003.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.60bca550da65b9b1dd3701bfd9fc133ca4de8c73.003.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.60bca550da65b9b1dd3701bfd9fc133ca4de8c73.003.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.60bca550da65b9b1dd3701bfd9fc133ca4de8c73.004.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.60bca550da65b9b1dd3701bfd9fc133ca4de8c73.004.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.955bb533f789fb9051a013cb07aea4524cf33974.002.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.955bb533f789fb9051a013cb07aea4524cf33974.002.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.a8a16334c2a6d05b3385606cfb8e6d8e3e55ce74.002.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.a8a16334c2a6d05b3385606cfb8e6d8e3e55ce74.002.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.a8a16334c2a6d05b3385606cfb8e6d8e3e55ce74.002.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.a8a16334c2a6d05b3385606cfb8e6d8e3e55ce74.002.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.a8a16334c2a6d05b3385606cfb8e6d8e3e55ce74.002.1',
    'https://alerts-v2.weather.gov/#/?id=urn:oid:2.49.0.1.840.0.a8a16334c2a6d05b3385606cfb8e6d8e3e55ce74.003.1'
})


class Webpage:

    def __init__(self):
        self.driver = webdriver.Firefox(executable_path='/Users/pacopoler/Desktop/ucs-climate/geckodriver')

    def close(self):
        self.driver.close()

    def get_warning_text(self, warning_url):
        self.driver.get(warning_url)

        # probably a more elegant way to do this but just trying over and over to scrape until the page actually loads
        while True:
            try:
                warning_message = self.driver.find_elements(By.TAG_NAME, 'article')[4]
                break
            except IndexError:  # fewer than 5 'article' elements if the page hasn't finished loading
                pass

        # taking the whole block for now but very easy to pick out just one bullet later
        message_text = warning_message.find_elements(By.TAG_NAME, 'div')[5].text

        return message_text


test_page = Webpage()
weather_warnings = [test_page.get_warning_text(warning_url) for warning_url in TEST_WEATHER_WARNINGS]
test_page.close()
