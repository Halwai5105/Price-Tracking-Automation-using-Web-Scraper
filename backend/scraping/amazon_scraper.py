from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Amazon URL (Modify for different products)
search_query = "laptop"
amazon_url = f"https://www.amazon.in/s?k={search_query}"

# Open Amazon Page
driver.get(amazon_url)
time.sleep(3)  # Wait for content to load

# Extract Product Details
products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

data = []
for product in products[:10]:  # Scrape first 10 products
    try:
        title = product.find_element(By.XPATH, './/h2[@class="a-text-normal"]').text
        price = product.find_element(By.XPATH, './/span[@class="a-offscreen"]').text
        link = product.find_element(By.XPATH, './/a[@class="a-link-normal"]').get_attribute("href")
        data.append({"Title": title, "Price": price, "Link": link})
    except:
        continue

# Store Data in Pandas DataFrame
df = pd.DataFrame(data)
print(df)

# Close Driver
driver.quit()
