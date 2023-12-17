import json
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

def get_alta_snow_totals():
    url = "https://www.alta.com/weather"  # Replace with the actual URL

    # Create a Chrome WebDriver instance
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the URL
    driver.get(url)

    try:
        snow_total_12hr = driver.find_element(By.CSS_SELECTOR,'''
        #snow-report > div > div > div.flex.flex-wrap.mt-8.mb-12.md\:mb-40.lg\:flex-no-wrap.lg\:mt-20.lg\:mb-72 > div:nth-child(1) > div > span.absolute.w-12.tracking-tighter.md\:-ml-1.weather-value.center-center.font-futura-pt.md\:w-auto > span
        ''')
    except NoSuchElementException:
        snow_total_12hr = driver.find_element(By.CSS_SELECTOR,'''
        #snow-report > div > div > div.flex.flex-wrap.mt-8.mb-12.md\:mb-40.lg\:flex-no-wrap.lg\:mt-20.lg\:mb-72 > div:nth-child(1) > div > span.absolute.w-12.tracking-tighter.md\:-ml-1.weather-value.center-center.font-futura-pt.md\:w-auto > div
        ''')    

    try:
        snow_total_24hr = driver.find_element(By.CSS_SELECTOR,'''
        #snow-report > div > div > div.flex.flex-wrap.mt-8.mb-12.md\:mb-40.lg\:flex-no-wrap.lg\:mt-20.lg\:mb-72 > div:nth-child(2) > div > span.absolute.w-12.tracking-tighter.md\:-ml-1.weather-value.center-center.font-futura-pt.md\:w-auto > span
        ''')
    except NoSuchElementException: 
        snow_total_24hr = driver.find_element(By.CSS_SELECTOR,'''
        #snow-report > div > div > div.flex.flex-wrap.mt-8.mb-12.md\:mb-40.lg\:flex-no-wrap.lg\:mt-20.lg\:mb-72 > div:nth-child(2) > div > span.absolute.w-12.tracking-tighter.md\:-ml-1.weather-value.center-center.font-futura-pt.md\:w-auto > div
        ''')
    print(snow_total_12hr.text, snow_total_24hr.text)

    snow_totals = {
        '12hr': snow_total_12hr.text,
        '24hr': snow_total_24hr.text
    }

# Close the browser when done
    driver.quit()

    return snow_totals

# alta_snow_totals = get_alta_snow_totals()
# print(alta_snow_totals)