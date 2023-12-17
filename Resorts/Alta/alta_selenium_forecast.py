import json
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")


def get_alta_forecast():
    url = "https://forecast.weather.gov/MapClick.php?lat=40.589690000000076&lon=-111.63962999999995"

    # Create a Chrome WebDriver instance
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the URL
    driver.get(url)


    alta_forecast_12hr = driver.find_element(By.CSS_SELECTOR,'''
    #detailed-forecast-body > div:nth-child(1) > div.col-sm-10.forecast-text
    ''')
    alta_forecast_24hr = driver.find_element(By.CSS_SELECTOR,'''
    #detailed-forecast-body > div:nth-child(2) > div.col-sm-10.forecast-text
    ''')
    alta_forecast_12hr_text = alta_forecast_12hr.text
    alta_forecast_24hr_text = alta_forecast_24hr.text

    forecast_dict = {k: v for k, v in locals().items() if k.endswith('_text')}


    return forecast_dict

alta_forecast = get_alta_forecast()
alta_forecast_12hr = alta_forecast['alta_forecast_12hr_text']
print(alta_forecast_12hr)
# print(alta_forecast)
# alta_snow_totals = get_alta_snow_totals()
# print(alta_snow_totals)