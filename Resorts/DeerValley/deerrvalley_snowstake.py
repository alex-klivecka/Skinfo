from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

def get_dv_snowstake():
    url = "https://www.deervalley.com/explore-the-mountain/webcams"

    # Create a Chrome WebDriver instance
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the URL
    driver.get(url)

    time.sleep(2)

    driver.execute_script("window.scrollTo(0, 4768);")

    time.sleep(3)

    element = driver.find_element(By.CSS_SELECTOR,"#main-content > div.main-content")

    location = element.location
    size = element.size
    driver.save_screenshot('screenshot.png')

    x_var = 560
    y_var = 201
    width_var = 560+880
    height_var = 201+655

    im = Image.open('screenshot.png')
    im = im.crop((int(x_var), int(y_var), int(width_var), int(height_var)))
    im.save('screenshot.png')

    # Show the cropped image
    im.show()

    # Close the browser when done
    driver.quit()

    return 

driver = webdriver.Chrome(options=chrome_options)# or webdriver.Chrome(), depending on your browser
driver.get('https://www.deervalley.com/explore-the-mountain/webcams')  # replace with your URL

time.sleep(2)

driver.execute_script("window.scrollTo(0, 4768);")

time.sleep(3)

element = driver.find_element(By.CSS_SELECTOR,"#main-content > div.main-content")

location = element.location
size = element.size
driver.save_screenshot('screenshot.png')

x_var = 560
y_var = 201
width_var = 560+880
height_var = 201+655

im = Image.open('screenshot.png')
im = im.crop((int(x_var), int(y_var), int(width_var), int(height_var)))
im.save('screenshot.png')

# Show the cropped image
im.show()

driver.quit()